# requests

from requests import get
# get은 function, 이동한 다음에 말 그대로 website를 가져오는것

websites=(
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://instagram.com"
)

# for website in websites:
#     if website.startswith("https://"):
#         print("good to go")
#     else:
#         print("we have to fix it")

# for website in websites:
#     if not website.startswith("https://"):
#         print("we have to fix it")
#     else:
#         print("good to go")

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)