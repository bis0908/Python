students = ['a', 'b', 'c', 'd', 'e']

# for number, name in enumerate(students):
    # print ("{}번의 이름은 {}이다.".format(number+1, name))

students_dict = {"{}번".format(number+1): name for number, name in enumerate(students)}

print(students_dict)

scores = [85, 75, 15, 95, 56]

for x, y in zip(students, scores):
    print(x, y)

score_dic = {student: score for student, score in zip(students, scores)}

print(score_dic)