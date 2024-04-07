people_courses = {}
def func(**kwargs):
  for name, courses in kwargs.items():
    if name in people_courses:
      people_courses[name] = people_courses[name] + courses
    else:
      people_courses[name] = courses


def display_courses():
  for name, courses in people_courses.items():
    print(f'Name: {name} is taking courses: {courses}')

func(Bob=['Math', 'Physics', 'Chemistry'], Alice=['Math', 'Chemistry', 'Physics'], Tom=['Math', 'Physics'])
func(Bob=['Python'])

display_courses()
