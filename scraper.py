import requests as rq
import soupsieve
from bs4 import BeautifulSoup

#new attempt: beautiful soup crawler method
links = ["https://www.metacritic.com/browse/movie/netflix/"]
while len(links) != 0:
    cur = links.pop()
    response = rq.get(cur)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select("a[href]")
    for i in elements:
        url = elements['href']
        if "https://www.metacritic.com/browse/movie/netflix/" in i:
            links.append(i)

