from requests import get
from bs4 import BeautifulSoup
from extractors.weworkremotely import extract_jobs
# 파일 경로 import function
jobs = extract_jobs("python")
print(jobs)
