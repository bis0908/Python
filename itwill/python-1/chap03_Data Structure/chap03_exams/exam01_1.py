'''
step01 문제

문1) 키보드로 5명의 학생 성적을 입력받아서 리스트에 저장하고,
     5명 학생의 성적의 평균을 구하고, 80점 이상 성적을 받은
     학생의 숫자를 계산하여 출력하시오.

<출력 예시>
성적을 입력하시요: 50
성적을 입력하시요: 85
성적을 입력하시요: 60
성적을 입력하시요: 55
성적을 입력하시요: 82
성적 평균은 66.4 입니다.
80점 이상 성적을 받은 학생은 2 명입니다.
'''
score = []
cnt = 0
while len(score) < 5:
    score.append(int(input('성적을 입력하시오: ')))

    if len(score) == 5:
        avg = sum(score) / len(score)
        print('성적 평균은 {} 입니다'.format(avg))
        for i in range(len(score)):
            if score[i] >= 80:
                cnt += 1
        print('80점 이상 성적을 받은 학생은 {} 명 입니다'.format(cnt))