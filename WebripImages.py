#load and download images from XKCD
import requests, os, bs4

url = 'http://xkcd.com/1526'    #Starting url
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd

while not url.endswith('#'):
    #Download page.
    print('Downloading pags %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    #find the url of the comic image
    comicSelect = soup.select('#comic img')
    if comicSelect == []:
        print('No comic found')
    else:
        comicUrl = 'http:'+ comicSelect[0].get('src')
        #download image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()                      
    
    #TODO: save image to /xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
    #TODO: get previous button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+ prevLink.get('href')
    
    
print('Done.')