case = int(input())  # 케이스 수

for i in range(case):
    score = list(map(int, input().split()))  # 학생들의 점수
    student_num = int(score[0])
    avr = sum(score[1:])/student_num
    count = 0
    for j in score[1:]:
        if j > avr:
            count += 1
    print(str('%.3f%%' % float((count/student_num)*100)) + '%')
