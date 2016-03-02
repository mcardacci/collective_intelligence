from bs4 import BeautifulSoup
import urllib2
import re

chare=re.compile(r'[!-\.&]')
itemowners={}

# Words to remove
dropwords=['a', 'new', 'some', 'more', 'my', 'own', 'the', 'many', 'other', 'another']

currentuser=0
for i in range(1,51):
	# URL for the want search page
	---------------------------------------------------------------
	c=urllib2.urlopen('http://member.zebo.com/Main?event_key=USERSEARCH&wiowiw=wiw&keyword=car&page=%d')