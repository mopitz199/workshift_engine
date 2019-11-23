import copy

from datetime import timedelta, datetime
from assignation.operators.range_operator import RangeOperator
from utils.range import Range


class AssignationOperator(object):
    """A class with method to operate assignation proxies."""

    @staticmethod
    def are_neighbors(assign1, assign2):
        """
        To check if two assignations intersect or are next to the other.

        :param assign1: an assignation proxy object
        :type assign1: AssignationProxy
        :param assign2: an assignation proxy object
        :type assign2: AssignationProxy

        :rtype: Boolean
        """

        return RangeOperator.are_neighbors(
            assign1.range_obj,
            assign2.range_obj)

    @staticmethod
    def are_intersection(assign1, assign2):
        """
        To check if two assignations intersect.

        :param assign1: an assignation proxy object
        :type assign1: AssignationProxy
        :param assign2: an assignation proxy object
        :type assign2: AssignationProxy

        :rtype: Boolean
        """

        return RangeOperator.are_intersection(
            assign1.range_obj,
            assign2.range_obj)

    @staticmethod
    def are_multiple_neighbors(assign, assigns):
        """
        To check how many assigns are neighbor of the given assign

        :param assign: an assignation proxy object
        :type assign: AssignationProxy
        :param assigns: An iterator of assigns to check
        :type assigns: Iterator

        :rtype: List<AssignationProxy>
        """

        resp = []
        for aux_assign in assigns:
            if AssignationOperator.are_neighbors(aux_assign, assign):
                resp.append(aux_assign)
        return resp

    @staticmethod
    def get_min_starting_date(assigns):
        """
        To get the minimun starting date from all the given assigns.

        :param assigns: An iterator with assigns
        :type assigns: Iterator

        :rtype: AssignationProxy
        """

        min_date = datetime(2090, 1, 1).date()
        resp = None
        for assign in assigns:
            if assign.range_obj.starting_date < min_date:
                resp = assign
                min_date = assign.range_obj.starting_date
        return resp

    @staticmethod
    def get_max_ending_date(assigns):
        """
        To get the maximum ending date from all the given assigns.

        :param assigns: An iterator with assigns
        :type assigns: Iterator

        :rtype: AssignationProxy
        """

        max_date = datetime(1900, 1, 1).date()
        resp = None
        for assign in assigns:
            if assign.range_obj.ending_date > max_date:
                resp = assign
                max_date = assign.range_obj.ending_date
        return resp

    @staticmethod
    def get_assignation_generator(assign_list):
        """
        To transform an assign list into an iterator

        :param assign_list: A list of assigns
        :type assigns: List

        :rtype: Generator
        """

        def assignation_generator():
            for assignation in assign_list:
                yield assignation
        return assignation_generator()

    @staticmethod
    def are_compatible(assign1, assign2):
        """
        To check if two assignments are compatible to be joined

        :param assign1: An assign proxy object
        :type assign1: AssignationProxy
        :param assign2: An assign proxy object
        :type assign2: AssignationProxy

        :rtype: Boolean
        """

        has_same_workshift = assign1.workshift_id == assign2.workshift_id
        has_same_person = assign1.person_id == assign2.person_id

        if has_same_workshift and has_same_person:

            if (assign1.starting_day or assign2.starting_day) is None:
                return True

            assign_generator = AssignationOperator.get_assignation_generator(
                [assign1, assign2])

            assign = AssignationOperator.get_min_starting_date(
                assign_generator)

            other_assign = assign2 if assign == assign1 else assign1

            simulated_starting_day = AssignationOperator.simulate_starting_day(
                assign, other_assign.starting_date)

            return simulated_starting_day == other_assign.starting_day
        else:
            return False

    @staticmethod
    def can_be_joined(assign1, assign2):
        """
        To check if two assignments can be joined. For that
        we considerer that are compatible and are intersection or
        next to the other

        :param assign1: An assign proxy object
        :type assign1: AssignationProxy
        :param assign2: An assign proxy object
        :type assign2: AssignationProxy

        :rtype: Boolean
        """

        return (AssignationOperator.are_neighbors(assign1, assign2) and
                AssignationOperator.are_compatible(assign1, assign2))

    @staticmethod
    def are_multiple_compatible(assign, assigns):
        """
        To check of how many assigns are compatable with the given assign

        :param assign: An assign proxy object
        :type assign: AssignationProxy
        :param assigns: A list of assigns
        :type assigns: Iterator

        :rtype: List<AssignationProxy>
        """

        resp = []
        for aux_assign in assigns:
            if AssignationOperator.can_be_joined(assign, aux_assign):
                resp.append(aux_assign)
        return resp

    @staticmethod
    def get_biggest_assign(assigns):
        """
        To get the assign with the more quantity of days

        :param assigns: A list of assigns
        :type assigns: Iterator

        :rtype: AssignationProxy
        """

        biggest = None
        for assign in assigns:
            if not biggest:
                biggest = assign
            else:
                biggest = assign if len(assign) > len(biggest) else biggest
        return biggest

    @staticmethod
    def get_candidates(assign, assigns):
        """
        Get all the other canididates and the best canidate from a given
        list of assignments

        :param assign: An assign proxy object
        :type assign: AssignationProxy
        :param assigns: A list of assigns
        :type assigns: Iterator

        :rtype: (AssignationProxy, List<AssignationProxy>)
        """

        candidates = AssignationOperator.are_multiple_compatible(
            assign,
            assigns)

        best_candidate = AssignationOperator.get_biggest_assign(candidates)
        if best_candidate:
            candidates.remove(best_candidate)
        return best_candidate, candidates

    @staticmethod
    def simulate_starting_day(assign, date_obj):
        """
        To simulate an starting_day in an specific date

        :param assign: An assign proxy object
        :type assign: AssignationProxy
        :param date_obj: The date which want to simulate
        :type date_obj: date

        :rtype: Int
        """

        if assign.starting_day:
            starting_date = assign.range_obj.starting_date
            delta = timedelta(days=assign.starting_day - 1)
            aux_starting_date = starting_date - delta

            range_days = (date_obj - aux_starting_date).days + 1
            total_days = assign.workshift.total_workshift_days

            return (range_days % total_days) or total_days
        else:
            return None

    @staticmethod
    def copy(assign):
        """
        To create a deep copy of a given assign

        :param assign: An assign proxy object
        :type assign: AssignationProxy

        :rtype: AssignationProxy
        """
        copied = copy.copy(assign)
        copied.obj = copy.deepcopy(assign.obj)
        copied.range_obj = copy.deepcopy(assign.range_obj)
        copied.workshift = assign.workshift
        copied.person = assign.person
        copied.obj.id = None
        return copied

    @staticmethod
    def remove(assign, starting_date, ending_date):
        """
        Function to remove a range from a given assignation

        :param assign: An assign proxy object
        :type assign: AssignationProxy
        :param starting_date: The starting date from
            where you want to start removing
        :type starting_date: AssignationProxy

        :rtype: Dict
        """

        resp = {'delete': None, 'update': None, 'create': None}
        copy_range_obj = copy.copy(assign.range_obj)
        other_range_obj = Range(starting_date, ending_date)
        updated_range, new_range = copy_range_obj - other_range_obj

        if not updated_range:
            resp['delete'] = assign
        elif new_range:
            new_assign = AssignationOperator.copy(assign)
            new_assign.range_obj = new_range
            assign.range_obj = updated_range

            if new_assign.starting_date > assign.starting_date:
                new_assign.starting_day = AssignationOperator.\
                    simulate_starting_day(
                        assign,
                        new_assign.range_obj.starting_date)
            else:
                assign.starting_day = AssignationOperator.simulate_starting_day(
                    new_assign,
                    assign.range_obj.starting_date)

            resp['update'] = assign
            resp['create'] = new_assign
        elif updated_range.starting_date > assign.starting_date:
            new_starting_day = AssignationOperator.simulate_starting_day(
                assign,
                updated_range.starting_date)
            assign.range_obj = updated_range
            assign.starting_day = new_starting_day
            resp['update'] = assign
        elif updated_range.ending_date < assign.ending_date:
            assign.range_obj = updated_range
            resp['update'] = assign
        else:
            pass
        return resp

    @staticmethod
    def sort_asc_starting_date(assigns):

        def get_starting_date(assign):
            return assign.starting_date

        assigns.sort(key=get_starting_date)
        return assigns

    @staticmethod
    def sort_desc_starting_date(assigns):

        def get_starting_date(assign):
            return assign.starting_date

        assigns.sort(key=get_starting_date, reverse=True)
        return assigns

    @staticmethod
    def get_ranges_of_assigns(assigns):
        response = []
        for assign in assigns:
            response.append(assign.range_obj)
        return response
