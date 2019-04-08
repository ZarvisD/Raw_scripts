from bs4 import BeautifulSoup
import re
import unicodedata

raw_html =  open('adobe.html').read() # Opening file for reading
soup = BeautifulSoup(raw_html, 'lxml') # Parse the HTML as a string
table = soup.find_all('table') # Grab the first table
for t in range(len(table)):

    tr0= table[t].find_all('tr')
    vendor_name = tr0[0].find_all('td')[0].find_all('b')[0].contents
    p=unicodedata.normalize("NFKD", vendor_name[0].string)
    p1=unicodedata.normalize("NFKD", vendor_name[1].string)
    print '\n' + p.decode('utf-8') + p1.decode('utf-8')
    for s in range(1,len(tr0)):
        td = tr0[s].find_all('td')
        # print td
        name = str(td[0].find_all('b')[0].contents[0])
        value = td[1]
        # print value
        if value.find('a'):
            # print len(value.find('a').contents)
            if len(value.find('a').contents) == 0:
                value = 'null'
                print name + ' : ' + value
            else:
                value = value.find('a').contents[0]
                # print value
                print name + ' : ' + value
        else:
            value = str(td[1].contents[0])
            print name + ' : ' + value
