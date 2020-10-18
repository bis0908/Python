# from indeed import get_jobs as get_indeed_jobs
# from job_korea import get_jobs as get_jk_jobs
# from save_csv import save_to_file
# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jk_jobs = get_jk_jobs()
# jobs = jk_jobs
# save_to_file(jobs)

from so import get_jobs
from flask import Flask, render_template, request, redirect, send_file
from exporter import save_to_file

app = Flask("NextScrapper")

db = {} #fake DB

@app.route("/")
def home(): #user는 home으로 이동.
    return render_template("potato.html")   #home의 html 파일

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower() #사용자의 잘못된 입력을 대비해 format 해주는 것.
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word) #so.py의 get_jobs 함수로 보낸다.
            db[word] = jobs
    else:
        return redirect("/") #word를 입력하지 않으면 리다이렉트 (home으로)
    return render_template("report.html", 
                            searchingBy=word, 
                            resultsNum=len(jobs),
                            jobs=jobs
                            )

@app.route("/export")
def export():
    try:
        word = request.args.get('word') #export로 간다면 첫번째로 해당 word가 url에 있는지 체크.
        if not word:
            raise Exception()
        word = word.lower() #검색어를 소문자로 만들어준다.
        jobs = db.get(word) #fake DB에 저장.
        if not jobs:        #word에 해당하는 jobs값이 없으면 홈으로 redirect
            raise Exception()
        save_to_file(jobs)  #jobs가 fake DB에 있으면 save_to_file 함수를 실행
        return send_file("jobs.csv", as_attachment=True)
    except:
        return redirect("/")

# @app.route("/<username>")  #'@' 골뱅이 = 데코레이터: 바로 아래 함수를 찾는다.
# 오직 함. 수. 만!!!! a = "hello" 이런거 입력하면 에러난다는 의미.
# def tomato(username):
    # return f"Hello {username}, how are you?"

app.run(host="127.0.0.1") #괄호 안에 주소를 넣어주면 사이트를 공개한다.