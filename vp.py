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
            r.html.render(timeout=30)
            if r.status_code == 404:
                raise Exception
            success = 1
        except:
            print('Invalid URL. Please try again.')

    text = []
    soup = bs4.BeautifulSoup(r.html.html, "lxml")

    article = soup.body.find("div", class_="post").find("div", class_="article")

    text.append(article.find("div", class_="header").find("h2").text.strip())

    content = article.find("div", class_="news-text-wrap")

    body = content.find_all("p")

    for p in body:
        text.append(p.text.strip())

    with open(f'var/vp_article_{index}.txt', 'w', encoding='utf8') as fout:
        for line in text:
            fout.write('\n'+line)
        print('Scraped content to: ' + f'var/vp_article_{index}.txt')

    con = 0 if input("\nDo you want to get another article (y/n)?") != 'y' else 1
    print()

