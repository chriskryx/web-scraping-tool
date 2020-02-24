from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_county = (input("Which county? ex. Timis\n(Press Enter if you don't want to specify):\n")).lower()

if my_county:

    my_city = (input("Which city? ex. Timisoara\n(Press Enter if you don't want to specify):\n")).lower()

    if my_city:
        page_num = input("Which page number? (50 businesses per page):\n")
        my_url = "https://www.romanian-companies.eu/{county}/{city}/o{page_num}.htm".format(county= my_county, city= my_city, page_num= page_num)
    else:
        page_num = input("Which page number? (50 businesses per page):\n")
        my_url = "https://www.romanian-companies.eu/{county}/j{page_num}.htm".format(county= my_county, page_num= page_num)
else:
    page_num = input("Which page number? (50 businesses per page):\n")
    my_url = "https://www.romanian-companies.eu/pagini/p{page_num}.htm".format(page_num= page_num)

# Opening up the connection, grabbing the page

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("td", {"class":"clickable-row"})

filename = (input("Choose your Excel filename:\n")) + ".csv"

f = open(filename, 'w')
headers = "Name, Link, Location\n"
f.write(headers)

for container in containers:

    name = container.a["title"]

    link = "https://www.listafirme.ro/" + container.a["href"]

    import get_link

    website_link = get_link.func2(link)

    location_container = container.text

    county_city = "Jud. {county}, Loc. {city}".format(county= my_county.upper() , city= my_city.upper())

    location = location_container.replace(name,"").replace(county_city, "").strip()

    ### You can comment these out
    print("name: " + name)
    print("website_link: " + website_link)
    print("location: " + location)

    f.write(name + "," + website_link + "," + location + "\n")