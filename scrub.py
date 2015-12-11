import urllib.request
from bs4 import BeautifulSoup


NYER_LINK = "http://www.newyorker.com/magazine"


def save_html(address):
    htmlSource = urllib.request.urlopen(address).read().decode()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    return soup


def find_links(someSoup, section):
    urlsBySect = {}
    idOfDiv = "#" + section + "-issue-featured"
    divs = someSoup.select(idOfDiv+" > div > div")
    for div in divs:
        sectTitle = div.select("h5")[0].text.lower()
        urlsBySect[sectTitle] = []
        listATags = div.select(".stories > article > section > h2 > a")
        for aTag in listATags:
            urlsBySect[sectTitle].append(aTag['href'])
    return urlsBySect


def get_article_from_url(artUrl):
    artHtml = urllib.request.urlopen(artUrl).read().decode()
    artSoup = BeautifulSoup(artHtml, 'html.parser')
    container = artSoup.select("#main > article > div")
    allPs = container[0].select("p")
    artText = ""
    for p in allPs:
        artText += p.text
    return artText





def send_email():
    pass


def save_articles_as_txt():
    nySoup = save_html(NYER_LINK)
    mainDict = find_links(nySoup, "main")
    secDict = find_links(nySoup, "secondary")
    mainDict.update(secDict)
    for seg, artList in mainDict.items():
        for link in artList:
            artContent = get_article_from_url(link)
            artTitle = link.split("/")[-1]
            savedAs = 'articles/' + seg + "_" + artTitle + ".txt"
            artTxt = open(savedAs, 'w')
            artTxt.write(artContent)
            artTxt.close()




if __name__ == "__main__":
    save_articles_as_txt()
    




"""
mainDict = find_main_links(nySoup, "main")
print(mainDict)
{'fiction': ['http://www.newyorker.com/magazine/2015/08/03/five-arrows'],
 'reporting': ['http://www.newyorker.com/magazine/2015/08/03/underworld-monte-reel',
  'http://www.newyorker.com/magazine/2015/08/03/the-children-of-strangers',
  'http://www.newyorker.com/magazine/2015/08/03/the-greek-warrior',
  'http://www.newyorker.com/magazine/2015/08/03/how-to-take-a-nature-walk-part-one'],
 'shouts & murmurs': ['http://www.newyorker.com/magazine/2015/08/03/apocalypse-shouts-and-murmurs-jack-handey']}
"""

# find_second_links(nySoup, "secondary")