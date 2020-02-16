from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
    create_proxy_day_off_assignation,
    create_assignations
)

from database.assignation_db import AssignationDB
from database.day_off_assignation_db import DayOffAssignationDB
from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy
from proxies.day_off_assignation_proxy import DayOffAssignationProxy

from collisions.services import check_collisions


class AssignationMoves:

    def build_workshift_db(self):
        workshifts_data = self.data['workshifts']
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)
        return workshift_db

    def build_days_off_db(self):
        days_off_data = self.data['days_off']
        day_off_assignations = create_proxy_day_off_assignation(days_off_data)
        day_off_assignations_db = DayOffAssignationDB(
            day_off_assignations,
            DayOffAssignationProxy
        )
        return day_off_assignations_db

    def build_assignations_db(self):
        assignations_database_data = self.data['assignations_database']
        database_assignations = create_assignations(
            assignations_database_data,
            self.workshift_db,
            self.day_off_assignations_db
        )
        assignation_db = AssignationDB(database_assignations, None)
        return assignation_db

    def get_moves(self):
        return self.data['moves']

    def create_assignations(self):
        assignations_data = self.moves['assignations']
        assignations = create_assignations(
            assignations_data,
            self.workshift_db,
            self.day_off_assignations_db
        )
        return assignations

    def create_deallocates(self):
        deallocates_data = self.moves['deallocates']
        deallocates = create_assignations(
            deallocates_data,
            self.workshift_db,
            self.day_off_assignations_db
        )
        return deallocates

    def deallocate(self):
        for deallocate in self.deallocates:
            self.assignation_db.unassign(deallocate)

    def assign(self):
        for assignation in self.assignations:
            if not check_collisions(assignation, self.assignation_db):
                self.assignation_db.assignate(assignation)
            else:
                # Tiene colisiones, entonces lo ignoramos
                pass

    def build_response(self):
        response = {
            'create': [],
            'update': [],
            'delete': []
        }
        for new_assignation in self.assignation_db.to_be_created:
            response['create'].append({
                'person_id': new_assignation.person_id,
                'workshift_id': new_assignation.person_id,
                'starting_date': f"{new_assignation.starting_date}",
                'ending_date': f"{new_assignation.ending_date}",
                'starting_day': new_assignation.starting_day,
            })
        for update_assignation in self.assignation_db.to_be_updated:
            response['update'].append({
                'id': update_assignation.id,
                'starting_date': f"{update_assignation.starting_date}",
                'ending_date': f"{update_assignation.ending_date}",
            })
        for delete_assignation in self.assignation_db.to_be_deleted:
            response['delete'].append(delete_assignation.id)

        return response

    def __init__(self, data):
        self.data = data
        self.workshift_db = self.build_workshift_db()
        self.day_off_assignations_db = self.build_days_off_db()
        self.assignation_db = self.build_assignations_db()
        self.moves = self.get_moves()
        self.assignations = self.create_assignations()
        self.deallocates = self.create_deallocates()

    def run(self):
        self.deallocate()
        self.assign()
        response = self.build_response()
        return response
