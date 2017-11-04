from bs4 import BeautifulSoup
import urllib.request
import html5lib
website = input("Choose your website: ")
source = urllib.request.urlopen(website).read()
soup = BeautifulSoup(source, 'html.parser')


target = input("Choose tag, css selector, id, class: ")
for strong_tag in soup.find_all(target):
    print (strong_tag.text)