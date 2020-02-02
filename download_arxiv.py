import re
import urllib.request
from bs4 import BeautifulSoup
import feedparser
import time

url = 'http://export.arxiv.org/api/query?'
sufix = 'search_query=cat:'
cat = ['astro-ph.GA', 'math.DG', 'quant-ph', 'stat.ML', 'cs.CL', 'q-bio.NC']
max_results = 500
for i in range(6):
    j = 1
    for start in range(0,5500,500):
        query = url + sufix + cat[i] + '&start=' + str(start) + '&max_results=' + str(max_results)
        query += '&sortBy=relevance&sortOrder=ascending'
        #print(query)
        API_response = urllib.request.urlopen(query)
        feed = feedparser.parse(API_response)
        for entry in feed.entries:
            f = open('/home/simona/PycharmProjects/PRACTICA/{0}/art_{1}.txt'.format(cat[i],j), 'w')
            j += 1
            f.write(entry.title + '\n' + entry.summary)
            f.close()
        time.sleep(3.0)
