import bs4 as bs
import urllib.request

words = []
freq = {}

pages = 10
link = 'https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea71&positionTypes=5b8e46b3853f039706b6ea72&positionTypes=5b8e46b3853f039706b6ea70&roles=backenddeveloper&roles=frontenddeveloper&roles=fullstackdeveloper&roles=androiddeveloper&roles=iosdeveloper&location=Copenhagen,%20Denmark&countryCode=DK'
classname = 'card-job-find-list__position'

def skin(elem):
    return str(elem).split('>')[1].split('<')[0].split()

def counter(words):
    wordsSet = sorted(set(words))
    for word in wordsSet:
        freq[word] = words.count(word)
    
def souper(sauce): 
    soup = bs.BeautifulSoup(sauce,'lxml')            
    body = soup.find_all('span',{'class':[classname]})
    for word in body:
        for word in skin(word):
            words.append(word)

def main(link):
    if pages != 0:
        for i in range(pages):
            sauce = urllib.request.urlopen(link+'&page='+str(i+1))
            souper(sauce)
    else:
        sauce = urllib.request.urlopen(link)
        souper(sauce)
    
    counter(words)
    new_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
    print(new_freq)

main(link)
