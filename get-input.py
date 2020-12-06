#! python3.9

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


day = (datetime.today() - datetime(2020, 12, 1)).days + 1
print(f"Today is day {day}")

dayDir = f"day{day}"
if not os.path.exists(dayDir):
    os.makedirs(dayDir)
    print(f"Created directory {dayDir}")

os.chdir(dayDir)

cookies = dict(session=os.getenv("AOC_SESSION"))
url = f"https://adventofcode.com/2020/day/{day}/input"
response = requests.get(url, cookies=cookies)
response.raise_for_status()
with open(os.path.realpath(f"input.txt"), "wb") as file:
    file.write(response.content)

print(f"Written [{url}] to [{file.name}]")
