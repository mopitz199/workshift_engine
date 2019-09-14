from datetime import datetime
from collisions.resolvers.cycle_to_week_resolver import CycleToWeeklyColission
from collisions.facades.cycle_assignation_facade import CycleAssignationFacade
from collisions.facades.weekly_assignation_facade import WeeklyAssignationFacade


assignation1 = {
  'starting_day': None,
  'starting_date': datetime(2019, 7, 2).date(),
  'ending_date': datetime(2019, 7, 10).date(),
  'workshift': {
    'total_days': 7,
    'days': {
      'monday': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
      'tuesday': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
      'wednesday': {
        'starting_time': datetime.strptime('19:00', '%H:%M').time(),
        'ending_time': datetime.strptime('03:00', '%H:%M').time()
      },
      'thursday': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
      'friday': {
        'starting_time': datetime.strptime('22:30', '%H:%M').time(),
        'ending_time': datetime.strptime('05:00', '%H:%M').time()
      },
      'saturday': {
        'starting_time': None,
        'ending_time': None
      },
      'sunday': {
        'starting_time': None,
        'ending_time': None
      }
    }
  }
}

assignation2 = {
  'starting_day': 2,
  'starting_date': datetime(2019, 7, 2).date(),
  'ending_date': datetime(2019, 7, 10).date(),
  'workshift': {
    'total_days': 5,
    'days': {
      '0': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
      '1': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
      '2': {
        'starting_time': None,
        'ending_time': None
      },
      '3': {
        'starting_time': datetime.strptime('22:00', '%H:%M').time(),
        'ending_time': datetime.strptime('05:00', '%H:%M').time()
      },
      '4': {
        'starting_time': datetime.strptime('08:00', '%H:%M').time(),
        'ending_time': datetime.strptime('19:00', '%H:%M').time()
      },
    }
  }
}


def check():
    cycle_facade = CycleAssignationFacade(assignation2)
    weekly_facade = WeeklyAssignationFacade(assignation1)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    resolver.cycle_to_weekly_colision()

check()