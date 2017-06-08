# imports

from bs4 import BeautifulSoup
import requests
from operator import itemgetter

def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

def main():
    d = {}
    fobj = open('heise-data.txt', 'w')     

    for site in range(0,4):

        url = "https://www.heise.de/thema/https?seite="+str(site)

        content = getPage(url).find("div", {"class" : "keywordliste"})
        content = content.findAll("nav")
        ueber = []
        for c in content:
                ueber += c.findAll("header")

                for u in ueber:
                    linetxt = u.text.encode('utf-8')
                    wordlist = linetxt.split()
                    #print(wordlist)
                    for word in wordlist:
                        word = word.decode()
                        word = word.strip('"')
                        #print(word)
                        if word not in d:
                            d[word] = 1
                        if word in d:
                            d[word] = d[word] + 1
    sorted_d = sorted(d.items(), key=itemgetter(1), reverse=True)
    print('Most common Words:')
    for i in range (3):
        print(sorted_d[i][0]+':'+str(sorted_d[i][1]))

    fobj.close()  



# main program
if __name__ == '__main__':
    main()

