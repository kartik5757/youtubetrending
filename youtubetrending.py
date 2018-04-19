import time
import requests
from bs4 import BeautifulSoup
tstart  = time.time()
url = 'http://www.youtube.com/feed/trending'
tsouptime = time.time()
soup  = BeautifulSoup(requests.get(url).text,'lxml')
print "Time taken to parse: ",time.time()-tsouptime
items = soup.findAll('div',{'class':"expanded-shelf-content-item"})
#print len(items)
count  = 1
for item in items:
   text = item.findAll('div',{'class':'yt-lockup-content'})[-1].findAll('h3',{'class':'yt-lockup-title'})[-1].text
   print count
   count = count  +  1
   print 'Title = ',text[0:len(text)-len(' - Duration: 5:45')]
   print text[-len('Duration: 5:45')-2:-1]
   lis = item.findAll('div',{'class':'yt-lockup-content'})[-1].findAll('div',{'class':'yt-lockup-meta'})[-1].findAll('ul',{'class':'yt-lockup-meta-info'})[-1].findAll('li')
   print 'posted:',lis[0].text
   print 'views:',lis[1].text 
   print '\n'


print 'executiontime:',time.time()-tstart
