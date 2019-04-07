from datetime import timedelta, datetime

class AssignationOperator(object):
    """A class with method to operate assignation mappers.
    Is importante to know that every list that some function will recieve
    as a assignation list, it must be sorted by staring_date from min to max"""

    @staticmethod
    def are_neighbors(assign1, assign2):
        """
        .. function:: are_neighbors(assign1, assign2)

            To check if two assignations intersect or are next to the other.

            :param assign1: an assignation mapper object
            :type assign1: AssignationMapper
            :param assign2: an assignation mapper object
            :type assign2: AssignationMapper

            :rtype: True or False
        """
        aux_ending_date = assign2.ending_date + timedelta(days = 1)
        aux_starting_date = assign2.starting_date - timedelta(days = 1)

        return (assign1.starting_date <= aux_ending_date and
            assign1.ending_date >= aux_starting_date)

    @staticmethod
    def are_multiple_neighbors(assign, assigns):
        """
        .. function:: are_multiple_neighbors(assign, assigns)

            To check how many assigns are neighbor of the given assign

            :param assign: an assignation mapper object
            :type assign: AssignationMapper
            :param assigns: An iterator of assigns to check
            :type assigns: Iterator

            :rtype: A list of neigbors
        """

        max_date = assign.ending_date + timedelta(days = 1)
        resp = []
        for aux_assign in assigns:
            if aux_assign.starting_date > max_date:
                return resp
            else:
                if AssignationOperator.are_neighbors(aux_assign, assign):
                    resp.append(aux_assign)
        return resp


    @staticmethod
    def get_min_starting_date(assigns):
        """
        .. function:: get_min_starting_date(assigns)

            To get the minimun starting date from all the given assigns.

            :param assigns: An iterator with assigns
            :type assigns: Iterator

            :rtype: the assign with the minimum starting date
        """

        min_date = datetime(2090, 1, 1).date()
        resp = None
        for assign in assigns:
            if assign.starting_date < min_date:
                resp = assign
                min_date = assign.starting_date
        return resp

    @staticmethod
    def get_max_ending_date(assigns):
        """
        .. function:: get_max_ending_date(assigns)

            To get the maximum ending date from all the given assigns.

            :param assigns: An iterator with assigns
            :type assigns: Iterator

            :rtype: the assign with the maximum ending date
        """

        max_date = datetime(1900, 1, 1).date()
        resp = None
        for assign in assigns:
            if assign.ending_date > max_date:
                resp = assign
                max_date = assign.ending_date
        return resp

    @staticmethod
    def get_assignation_generator(assign_list):
        """
        .. function:: get_assignation_generator(assign_list)

            To transform an assign list into an iterator

            :param assign_list: A list of assigns
            :type assigns: List

            :rtype: the generator
        """

        def assignation_generator():
            for assignation in assign_list:
                yield assignation
        return assignation_generator()

    @staticmethod
    def are_compatible(assign1, assign2):
        """
        .. function:: are_compatible(assign1, assign2)

            To check if two assignments are compatible to be joined

            :param assign1: An assign mapper object
            :type assign1: AssignationMapper
            :param assign2: An assign mapper object
            :type assign2: AssignationMapper

            :rtype: a True or False
        """

        has_same_workshift = assign1.workshift == assign2.workshift
        has_same_person = assign1.person == assign2.person

        if (AssignationOperator.are_neighbors(assign1, assign2) and
            has_same_workshift and has_same_person):

            if (assign1.start_day or assign2.start_day) is None: return True

            assign_generator = AssignationOperator.get_assignation_generator(
                [assign1, assign2])

            assign = AssignationOperator.get_min_starting_date(assign_generator)

            other_assign = assign2 if assign == assign1 else assign1

            simulated_start_day = AssignationOperator.simulate_starting_day(
                assign, other_assign.starting_date)

            return simulated_start_day == other_assign.start_day
        else:
            return False

    @staticmethod
    def are_multiple_compatible(assign, assigns):
        """
        .. function:: are_multiple_compatible(assign, assigns)

            To check of how many assigns are compatable with the given assign

            :param assign: An assign mapper object
            :type assign: AssignationMapper
            :param assigns: A list of assigns
            :type assigns: Iterator

            :rtype: a list with the compatible assigns
        """

        resp = []
        for aux_assign in assigns:
            if AssignationOperator.are_compatible(assign, aux_assign):
                resp.append(aux_assign)
        return resp

    @staticmethod
    def get_biggest_assign(assigns):
        """
        .. function:: get_biggest_assign(assigns)

            To get the assign with the more quantity of days

            :param assigns: A list of assigns
            :type assigns: Iterator

            :rtype: An assignation mapper
        """

        biggest = None
        for assign in assigns:
            if not biggest: biggest = assign
            else:
                biggest = assign if len(assign) > len(biggest) else biggest
        return biggest

    @staticmethod
    def get_candidates(assign, assigns):
        """
        .. function:: get_candidates(assign, assigns)

            Get all the other canididates and the best canidate from a given
            list of assignments

            :param assign: An assign mapper object
            :type assign: AssignationMapper
            :param assigns: A list of assigns
            :type assigns: Iterator

            :rtype: An assignation mapper and a list of assignation mappers
        """

        candidates = AssignationOperator.are_multiple_compatible(assign, assigns)
        best_candidate = AssignationOperator.get_biggest_assign(candidates)
        candidates.remove(best_candidate)
        return best_candidate, candidates

    @staticmethod
    def simulate_starting_day(assign, date_obj):
        """
        .. function:: simulate_starting_day(assign, date_obj)

            To simulate an start_day in an specific date

            :param assign: An assign mapper object
            :type assign: AssignationMapper
            :param date_obj: The date which want to simulate
            :type date_obj: date

            :rtype: the simulated start_day
        """

        if assign.start_day:
            aux_starting_date = assign.starting_date - timedelta(days = assign.start_day - 1)

            range_days = (date_obj - aux_starting_date).days + 1
            total_days = assign.total_workshift_days
            
            return (range_days % total_days) or total_days
        else:
            return None

    @staticmethod
    def get_removing_type(assign, starting_date, ending_date):
        """
        .. function:: get_remove_type(assign, starting_date, ending_date)

            To determine the removing type to handle an resize of an assignment

            :param assign: An assign mapper object
            :type assign: AssignationMapper
            :param starting_date: The starting date of remove
            :type starting_date: Date
            :param ending_date: The ending date fo remove
            :type ending_date: Date

            :rtype: the removing type
        """
        if assign.starting_date >= starting_date and assign.ending_date <= ending_date:
            return "complete"
        elif assign.starting_date < starting_date and assign.ending_date > ending_date:
            return "middle"
        else:
            return "one_side"