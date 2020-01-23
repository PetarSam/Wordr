import bs4 as bs
import urllib.request

words = {}
innerLinks = []
outerLinks = []

def main(link):
    sauce = urllib.request.urlopen(link)
    soup = bs.BeautifulSoup(sauce,'lxml')
    for link in soup.find_all('a'):
        print("links\n")
        print(link.get('href')) 

    ### Needs to add background images
    for source in soup.find_all('img'):
        print("images\n")
        print(source.get('src')) 
    body = soup.find('body').text.strip().split()
    for word in body:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    wordsSorted = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
    print(wordsSorted.items())

main('https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea71&positionTypes=5b8e46b3853f039706b6ea72&positionTypes=5b8e46b3853f039706b6ea70&roles=backenddeveloper&roles=frontenddeveloper&roles=fullstackdeveloper&roles=androiddeveloper&roles=iosdeveloper&location=Copenhagen,%20Denmark&countryCode=DK')