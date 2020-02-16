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


#  Agregar varias licencias
def assignation_moves(data):
    workshifts_data = data['workshifts']
    workshifts = create_proxy_workshifts(workshifts_data)
    workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

    days_off_data = data['days_off']
    day_off_assignations = create_proxy_day_off_assignation(days_off_data)
    day_off_assignations_db = DayOffAssignationDB(
        day_off_assignations,
        DayOffAssignationProxy
    )

    assignations_database_data = data['assignations_database']
    database_assignations = create_assignations(
        assignations_database_data,
        workshift_db,
        day_off_assignations_db
    )
    assignation_db = AssignationDB(database_assignations, None)

    moves = data['moves']

    assignations_data = moves['assignations']
    assignations = create_assignations(
        assignations_data,
        workshift_db,
        day_off_assignations_db
    )

    deallocates_data = moves['deallocates']
    deallocates = create_assignations(
        deallocates_data,
        workshift_db,
        day_off_assignations_db
    )

    for deallocate in deallocates:
        assignation_db.unassign(deallocate)

    for assignation in assignations:
        if not check_collisions(assignation, assignation_db):
            assignation_db.assignate(assignation)
        else:
            # Tiene colisiones, entonces lo ignoramos
            pass

    response = {
        'create': [],
        'update': [],
        'delete': []
    }
    for new_assignation in assignation_db.to_be_created:
        response['create'].append({
            'person_id': new_assignation.person_id,
            'workshift_id': new_assignation.person_id,
            'starting_date': f"{new_assignation.starting_date}",
            'ending_date': f"{new_assignation.ending_date}",
            'starting_day': new_assignation.starting_day,
        })
    for update_assignation in assignation_db.to_be_updated:
        response['update'].append({
            'id': assignation.id,
            'starting_date': f"{update_assignation.starting_date}",
            'ending_date': f"{update_assignation.ending_date}",
        })
    for delete_assignation in assignation_db.to_be_deleted:
        response['delete'].append(delete_assignation.id)

    return response


# Eliminar varias licencias

# Editar varias licencias

{
    'workshifts': [
        {
            'id': 6,
            'total_workshift_days': 5,
            'workshift_type': 'cyclic',
            'days': [
                {
                    'day_number': 0,
                    'starting_time': '08:00',
                    'ending_time': '19:00'
                },
                {
                    'day_number': 1,
                    'starting_time': '08:00',
                    'ending_time': '19:00'
                },
                {
                    'day_number': 2,
                    'starting_time': None,
                    'ending_time': None
                },
                {
                    'day_number': 3,
                    'starting_time': '08:00',
                    'ending_time': '19:00'
                },
                {
                    'day_number': 4,
                    'starting_time': '08:00',
                    'ending_time': '19:00'
                }

            ]
        },
    ],
    'days_off': [
        {
            'person_id': 1,
            'starting_date': '2019-9-4',
            'ending_date': '2019-9-4',
            'starting_time': '19:00',
            'ending_time': '19:00'
        },
        {
            'person_id': 1,
            'starting_date': '2019-9-10',
            'ending_date': '2019-9-10',
            'starting_time': '08:00',
            'ending_time': '19:00'
        }
    ],
    'assignations_database': [
        {
            'starting_date': '2019-2-14',
            'ending_date': '2019-2-16',
            'workshift_id': 6,
            'person_id': 1,
            'starting_day': 5
        },
        {
            'starting_date': '2019-2-14',
            'ending_date': '2019-2-16',
            'workshift_id': 6,
            'person_id': 1,
            'starting_day': 5
        }
    ],
    'moves': {
        'assignations': [
            {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            }
        ],
        'deallocates': [
            {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            }
        ]
    }
}
