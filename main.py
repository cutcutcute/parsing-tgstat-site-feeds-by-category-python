
import requests
from bs4 import BeautifulSoup 
import lxml 
import time

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

url = "https://tgstat.ru/tag/digital-marketing"
response = requests.get(url, headers = headers)
print(f"status code - {response.status_code}")
soup = BeautifulSoup(response.text, "lxml")
channel_list = []

all = soup.find_all("a", class_ = "text-body")

for i in all:
	try:
		link = i.get("href")
		if link.startswith("https://tgstat.ru/channel/@"):
			channel_list.append(link.replace("https://tgstat.ru/channel/@", "").strip() +"\n")
	except Exception as ex:
		time.sleep(0)

with open("reult.txt", 'a', encoding = "UTF-8") as file:
	file.write("".join(channel_list))

print("Successfully")
print("check result.txt")
