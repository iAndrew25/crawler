from bs4 import BeautifulSoup
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

f = open("movies.txt","r")

for line in f:
	soup = BeautifulSoup(br.open(line), "html.parser")
	iframe = soup.findAll('iframe')

	if len(iframe) > 0:
		print "Title: " + soup.title.string.encode('utf-8') + ' - ' + str(len(iframe))