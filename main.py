from requests_html import HTMLSession
import bs4

con = 1
index = 0

while con == 1:
    index += 1
    URL = input("Insert URL: ")
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()

    text = []
    soup = bs4.BeautifulSoup(r.html.html, "lxml")

    article = soup.body.find("div", class_="content").find("div", class_="article")

    text.append(article.find("h1").text)
    text.append(article.find("h2").text)

    content = article.find("article")

    body = content.find("div", class_="body").find_all("p")

    for p in body:
        text.append(p.text)

    with open(f'var/article_{index}.txt', 'w', encoding='utf8') as fout:
        for line in text:
            fout.write(line)

    another = input("Do you want to get another article (y/n)? ")

    if another == 'n':
        con = 0

