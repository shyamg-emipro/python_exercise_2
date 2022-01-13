from operator import itemgetter
from functools import reduce

emp_dict = {
    101: {'name': 'Anupriya Roy',
          'depart_id': 1,
          'attendances': [{'date': 1, 'hours': [3.5, 4.5]}, {'date': 2, 'hours': [3.2, 4.5]},
                          {'date': 3, 'hours': [3.2, 4.6]},
                          {'date': 4, 'hours': [3.0, 4.5]}, {'date': 5, 'hours': [2.5, 4.5]},
                          {'date': 6, 'hours': [1.5, 4.5]},
                          {'date': 7, 'hours': [2, 3]}, {'date': 8, 'hours': [0, 4.5]}, {'date': 9, 'hours': [2, 3.5]},
                          {'date': 10, 'hours': [4, 3.5]}],
          'leaves': [{'date': 7, 'no_of_hours': 1.5}, {'date': 7, 'no_of_hours': 1.5}, {'date': 8, 'no_of_hours': 3}]
          },
    102:
        {'name': 'Kadambari Sharma',
         'depart_id': 1,
         'attendances': [{'date': 1, 'hours': [0, 4.5]}, {'date': 2, 'hours': [3.2, 0]},
                         {'date': 3, 'hours': [3.2, 4.6]},
                         {'date': 4, 'hours': [1, 4.5]}, {'date': 5, 'hours': [2.5, 2]}, {'date': 6, 'hours': [1.5, 1]},
                         {'date': 7, 'hours': [2, 4]}, {'date': 8, 'hours': [1, 4.5]}, {'date': 9, 'hours': [2, 2]},
                         {'date': 10, 'hours': [2, 3.5]}],
         'leaves': [{'date': 1, 'no_of_hours': 3.5}, {'date': 2, 'no_of_hours': 2}, {'date': 2, 'no_of_hours': 2}]
         },
    103:
        {'name': 'Abhishek Verma',
         'depart_id': 1,
         'attendances': [{'date': 3, 'hours': [3.2, 4.6]}, {'date': 4, 'hours': [1, 4.5]},
                         {'date': 5, 'hours': [2.5, 2]},
                         {'date': 6, 'hours': [1.5, 1]}, {'date': 7, 'hours': [2, 4]}, {'date': 8, 'hours': [1, 4.5]},
                         {'date': 9, 'hours': [2, 2]}, {'date': 10, 'hours': [2, 3.5]}
                         ],
         'leaves': [{'date': 1, 'no_of_hours': 3}, {'date': 2, 'no_of_hours': 2}, {'date': 2, 'no_of_hours': 3}]
         }
}


def attendance_hours(day):
    return reduce(lambda a, b: a + b, day['hours'])


def leave_hours(day):
    return day['no_of_hours']


def emp_details(emp):
    employee = emp_dict[emp]
    total_attendance_hours = sum(list(map(attendance_hours, employee['attendances'])))
    total_leave_hours = sum(list(map(leave_hours, employee['leaves'])))
    return {'employee_id': emp,
            'employee_name': employee['name'],
            'total_attendance_hours': total_attendance_hours,
            'total_leave_days': total_leave_hours
            }


def filter_days(attendances):
    return list(filter(lambda day: True if sum(day['hours']) < 8 else False, attendances))


def get_dates(days):
    return days['date']


def get_hours(days):
    return sum(days['hours'])


def emp_attendance_record(emp):
    employee = emp_dict[emp]
    return {
        emp: {
            'date': list(map(get_dates, filter_days(employee['attendances']))),
            'total_hrs': list(map(get_hours, filter_days(employee['attendances'])))
        }
    }


employee_record = list(map(emp_details, emp_dict))
print("\n", employee_record)
employee_work_hours_record = list(map(emp_attendance_record, emp_dict))
print("\n\n", employee_work_hours_record)
