from requests_html import HTMLSession
import bs4

con = 1
index = 0

while con == 1:
    index += 1

    success = 0
    while success == 0:
        URL = input("Insert URL: ")
        session = HTMLSession()

        try:
            r = session.get(URL)
            r.html.render()
            if r.status_code == 404:
                raise Exception
            success = 1
        except:
            print('Invalid URL. Please try again.')

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
        print('Scraped content to: ' + f'var/article_{index}.txt')

    another = input("\nDo you want to get another article (y/n)?")
    print()

    if another == 'n' or index >= 1000:
        con = 0