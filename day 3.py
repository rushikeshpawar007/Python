#courses = ['History', 'Science', 'Maths','physics']
#courses_2 = ['Art','Education']
#nums = [1, 5, 4, 3]


#courses.append('Art')
#courses.insert(0,'Art')
#courses.insert(0,courses_2)

#courses.extend(courses_2)
#courses.append(courses_2)
#print(courses[0])
#print(courses[-1])
#print(courses[2])
#print(courses[1])

#print(courses[0:3])
#print(courses[:3])

#courses.remove('History')
#popped = courses.pop()

#courses.reverse()
#courses.sort(reverse=True)
#nums.sort(reverse=True)

#sorted_courses = sorted(courses)

#print(sorted_courses)
#print(min(nums))
#print(max(nums))
#print(sum(nums))

#print(courses.index('Maths'))
#print(courses.index('physics'))

#print('Arts' in courses)

#print('Maths' in courses)

#for item in courses:
#	print(item)

#for index, course in enumerate(courses, start=1):
#print(index, course)

#courses = ['History', 'Science', 'Maths','physics']

#course_str = ', '.join(courses)
#course_str = '-'.join(courses)

#new_list = course_str.split('-')
#print(course_str)
#print(new_list)

#list are mutable, Tuple are not

#Sets are random values 
cs_courses = {'History', 'Science', 'Maths','physics'}
art_course = {'History', 'Maths', 'Art', 'Design'}


print(cs_courses.intersection(art_course))
print(cs_courses.difference(art_course))
print(cs_courses.union(art_course))
