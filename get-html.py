from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "http://www.filmeonline.biz/"
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

urls = [url]
visited = [url]
added = []

file = open('movies.txt', 'a')

while len(urls)>0:
	try:
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