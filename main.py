from requests import get
from bs4 import BeautifulSoup
# https://beautiful-soup-4.readthedocs.io/en/latest/#

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    # beautifulsoup에게 html을 보내준다고 말하는 것
    jobs = soup.find_all('section', class_="jobs")
    # html class는 class_로 작성
    # *현재 html class = jobs의 섹션을 불러옴
    # print(len(jobs))
    # len은 list 나 tuple의 크기를 줄인다라고 말했지만 사용결과 해당 find의 결과물의 갯수가 나옴
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop(-1)
        # 각 jobs의 job_section으로 html list를 job_posts로 지정 하고 마지막 요소는 지정 제거
        for post in job_posts:
            anchors = post.find_all('a')
        # 또 그 job_posts를  각 post 마다 html anchor 를 찾고 anchors라 지칭
            anchor = anchors[1]
        # list 안에 있는 모든 anchor들 중에 2번째 것 내가 찾고자 하는 것
            link = anchor["href"]
        # beautifulsoup는 html을 파이썬의 dictionary처럼 쓸 수 있게 해줌
            company, kind, region = anchor.find_all('span', class_="company")
        # 지정된 anchor 안의 classname company의 span들을 company, kind, region으로 차례로 지정
            titles = anchor.find('span', class_="title")
            job_data = {
                'link': f"https://weworkremotely.com{link}",
                'company': company.string,
                'region': region.string,
                'position': titles.string
            }
            results.append(job_data)
    for result in results:
        print(result)
        print("///////////")
