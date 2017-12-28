from bs4 import BeautifulSoup
from get_elements_from_html import getElementsFromHTML

import urlparse
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def getAllPagesFromWebsite(url):
	urls = [url]
	visited = [url]
	added = []

	file = open('movies.txt', 'a')

	while len(urls) > 0:
		try:
			print len(urls)
			
			br.open(urls[0])
			urls.pop(0)
			for link in br.links():
				newurl =  urlparse.urljoin(link.base_url,link.url)

				if newurl.endswith('.html') and newurl not in added:
					visited.append(newurl)
					added.append(newurl)
					file.write(newurl + "\n")
				else:
					if newurl not in visited and url in newurl:
						visited.append(newurl)
						urls.append(newurl)
		except:
			print "error"
			urls.pop(0)

def getElementsFromHTML(brws):
	f = open("movies.txt","r")

	for line in f:
		soup = BeautifulSoup(brws.open(line), "html.parser")
		iframe = soup.findAll('iframe')

		if len(iframe) > 0:
			print "Title: " + soup.title.string.encode('utf-8') + ' - ' + str(len(iframe))


website = "http://www.filmeonline.biz/"
getAllPagesFromWebsite(website)
getElementsFromHTML(br)