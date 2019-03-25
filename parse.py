#Blank_doc_update


from bs4 import BeautifulSoup
import re
import unicodedata
raw_html =  open('oracle.html').read() # Opening file for reading
soup = BeautifulSoup(raw_html, 'lxml') # Parse the HTML as a string
table = soup.find_all('table') # Grab the first table

for i in range(len(table)):
    con = table[i].find_all('tr')
    # print con[0]
    vendor_name = con[0].find_all('td')[0].find_all('b')[0].contents
    # print vendor_name[0].string
    # print vendor_name[0].decode('utf-8') + vendor_name [1].decode('utf-8')
    p=unicodedata.normalize("NFKD", vendor_name[0].string)
    p1=unicodedata.normalize("NFKD", vendor_name[1].string)
    print '\n' + p.decode('utf-8') + p1.decode('utf-8')
    for j in range(1,len(con)):
        td = con[j].find_all('td')
        # print td
        # print td[0].find_all('b')[0]
        name = td[0].find_all('b')[0].contents
        if td[1].find('a'):
            value = td[1].find('a').contents
            if len(value) == 0:
                print name[0].decode('utf8') + ' : '
        else:
            value = td[1].contents
            print name[0].decode('utf-8') + ' : ' + value[0].decode('utf-8')
