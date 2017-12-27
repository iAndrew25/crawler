import urlparse
import mechanize
from bs4 import BeautifulSoup

url = "http://www.filmeonline.biz/"
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

urls = [url]
visited = [url]

nodups = []

file = open('movies.txt', 'a')

j = 0

#while len(urls) > 0:
while j < 1000:
	currentUrl = br.open(urls[0])
	urls.pop(0)

	for link in br.links():
		newurl =  urlparse.urljoin(link.base_url,link.url)

		if newurl.endswith('.html'):
			newPage = br.open(newurl)
			if newPage:
				soup = BeautifulSoup(newPage, "html.parser")
				iframe = soup.findAll('iframe')

				if len(iframe) > 0 and newurl not in nodups:
					file.write("Title: " + soup.title.string.encode('utf-8') + "\n\n")
					file.write("START IFRAMES =====================\n")
					for i in iframe:
						file.write(str(i) + "\n")
					file.write("END IFRAMES =======================\n\n\n")
					nodups.append(newurl)

		if newurl not in visited and url in newurl:
			visited.append(newurl)
			urls.append(newurl)
	j += 1

print "Movies added " + str(len(nodups))