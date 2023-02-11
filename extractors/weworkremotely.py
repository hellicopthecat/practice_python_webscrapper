from requests import get
from bs4 import BeautifulSoup
# https://beautiful-soup-4.readthedocs.io/en/latest/#


def extract_jobs(keyword):
    # extract_jobs는 키워드를 받게 될것이다.
    # 작업했던 내용을 copy paste 해준다
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    # search_term = "python"
    # keyword는 search term을 대체할 것이다.

    response = get(f"{base_url}{keyword}")
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
                company, kind, region = anchor.find_all(
                    'span', class_="company")
            # 지정된 anchor 안의 classname company의 span들을 company, kind, region으로 차례로 지정
                titles = anchor.find('span', class_="title")
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string,
                    'region': region.string,
                    'position': titles.string
                }
                results.append(job_data)
        return results
        # for result in results:
        #     print(result)
        #     print("///////////")
        #     # 여기서 print만 하려고 한것이 아니기 때문에 이 데이터를 가지고 파일에 넣어주기 위해
        #     # for result in results말고 return results로 바꾼다.

        # 먼저 이 코드를 삭제하기는 싫고 코드를 재사용 하고 싶으면
        # 별도의 파일로 이동시키고 function안에 넣기 위해 main.py에 공간을 만들어줘야한다.
        # 일단 extractors라는 폴더를 만들어주고 관련 python 파일을 만든다
