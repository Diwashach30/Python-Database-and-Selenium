import time
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(browser.page_source, "html.parser")


## find all elements with class "ipc - title__text"

movies = soup.find_all("h3", class_="ipc-title__text")

## Extract and store text content

movie_titles = [movie.get_text(strip=True) for movie in movies]

## Print movie titles
for title in movie_titles:
    print(title)
    
    
## Save all titles to a text file

with open("movies.txt", "w", encoding="utf-8") as f:
    for title in movie_titles:
        f.write(title + "\n")
    



