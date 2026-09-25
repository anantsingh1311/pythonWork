import requests
from bs4 import BeautifulSoup



response = requests.get("https://stackoverflow.com/questions",params={"order": "desc", "sort": "creation", "site": "stackoverflow"})

soup = BeautifulSoup(response.text,"html.parser")

# questions = soup.select(".s-post-summary--content")

print(soup.get_text())
# print(soup.prettify())





# print(response.text)