import requests
from bs4 import BeautifulSoup

url = f"http://www.jobkorea.co.kr/Search/?stext=%EC%9E%90%EB%B0%94&local=B150%2CB180%2CB190%2CB200%2CB201"

def get_last_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "tplPagination newVer short clear"}).find_all("span")
    last_page = pages[-1].get_text(strip=True)
    return int(1)


def extract_job(html):
    title = html.find("div", {"class": "post"}).find_all("a")
    location = html.find("div", {"class": "post"}).find("p").find_all("span")
    title = title[1].get_text(strip=True)
    location = location[-2].get_text(strip=True)
    company = html.find("div", {"class": "post"}).find("a")["title"]
    job_id = html.find("div", {"class": "post"}).find("a")["href"]
    return {
            'title': title, 
            'company': company, 
            'location':location, 
            'appny_link' : f"http://www.jobkorea.co.kr{job_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Searching Java jobs in Jobkorea.com... page: {page}")
        result = requests.get(f"{url}&tabType=recruit&Page_No={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("li", {"class": "list-post"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
    
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs