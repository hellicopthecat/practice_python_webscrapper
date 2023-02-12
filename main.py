# from requests import get
from bs4 import BeautifulSoup
# from extractors.weworkremotely import extract_jobs
# 파일 경로 import function
# jobs = extract_jobs("python")
# print(jobs)
from selenium import webdriver
# 셀리늄 설치 후 webdriver를 import / webdriver는 파이선에서 브라우저를 시작할 수 있는 방법
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# webdriver_manager도 설치해야함

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
# 크롬 드라이버 최신 유지

browser.get(
    "https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=1015284880e2ff62")

soup = BeautifulSoup(browser.page_source, "html.parser")
jobs_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = jobs_list.find_all('li', recursive=False)
# print(len(jobs))
# beautifull soup은 li속에 있는 li까지 찾아내기 때문에 바로 아래 있는 것만 검색해주길 원한다고 말해줘야한다.
# 그러기 위해선 recursive=False를 작성
for job in jobs:
    print(job)
    print("/////////")
