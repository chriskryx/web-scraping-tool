def func1(link):
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup

    uClient = uReq(link)

    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    containers = page_soup.find("span", {"style": "color:blue"})

    return containers.text


def func2(link):
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup

    uClient = uReq(link)

    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    containers = page_soup.find("td", {"style": "vertical-align:middle"})
    try:
        the_link = containers.a['href']
    except:
        the_link = ""
    if the_link == "web-site.htm":
        return func1(link + the_link)
    else:
        return the_link
