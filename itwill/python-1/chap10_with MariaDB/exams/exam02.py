'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 :
'''
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3307,
    'charset': 'utf8',
    'use_unicode': True}

def select(table):
    cur.execute(f'select * from {table}')
    dataset = cur.fetchall()
    print('code\t name\t qty\t amount')
    print('-'*40)
    for row in dataset:
        print("{0}      {1}     {2}    {3}".format(
            row[0], row[1], row[2], row[3]))

    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))

try:
    # db 연결 객체 생성
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성
    cur = conn.cursor()

    while True:  # 무한루프
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu = int(input('\t메뉴번호 입력 : '))

        if menu == 1:
           select('goods')

        elif menu == 2:
            code = int(input('code input : '))
            name = input('name input : ')
            qty = int(input('qty input : '))
            amount = int(input('amount input : '))
            sql = f"insert into goods values({code},'{name}',{qty},{amount})"
            cur.execute(sql)
            conn.commit()  # db 반영
            select('goods')

        elif menu == 3:
            code = int(input('code input : '))
            name = input('name input : ')
            qty = int(input('qty input : '))
            amount = int(input('amount input : '))

            sql = f'''update goods set
                name = '{name}',
                qty = {qty},
                amount = {amount}
                where code = {code}'''
            cur.execute(sql)
            conn.commit()  # db 반영
            select('goods')

        elif menu == 4:
            code = int(input('삭제할 코드 입력 : '))

            # 1) 해당 레코드 조회
            cur.execute(f"select * from goods where code = {code}")
            row = cur.fetchone()  # 검색 레코드 1개 경우

            # 1) 해당 레코드 삭제
            if row:  # row != null
                sql = f"delete from goods where code = {code}"
                cur.execute(sql)
                conn.commit()  # db 반영
            else:
                print('해당 레코드 없음')
            select('goods')

        elif menu == 5:
            print('프로그램 종료')
            break  # 반복 exit
        else:
            print('해당 메뉴는 없습니다.')

# DB 연결 예외 처리
except Exception as e:
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cur.close()
    conn.close()
