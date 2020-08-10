import requests
import random
import json
import re
from random import randint

from bs4 import BeautifulSoup


def randomjokesDotcom():
    url = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://official-joke-api.appspot.com/jokes/random",
    ]
    url = random.choices(url)[0]
    req = requests.get(url).json()
    joke = f"\n{req['setup']}\n\n{req['punchline']}"
    return joke


def jokesYouDotcom():
    urlToRead = "http://www.jokesyou.com/"
    handle = requests.get(urlToRead)
    htmlGunk = handle.content
    soup = BeautifulSoup(htmlGunk, "html.parser")
    joke = soup.findAll("div", {"class": "right"})[0].findAll("p")[0]
    joke = str(joke)
    # Regex replace
    joke = re.sub(r"<p>", r"", joke)
    joke = re.sub(r"</p>|<br/>", r"\n", joke)
    return joke


whichSite = randint(1, 2)
if whichSite == 1:
    print(jokesYouDotcom())
    print("\nSource - jokesyou.com")

elif whichSite == 2:
    print(randomjokesDotcom())
    print("\nSource - randomjoke.com")
