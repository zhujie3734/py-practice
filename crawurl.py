

def craw3(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'LxmL')
    for pic_href in soup.find_all('div', class_='news_type_video"):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            dir =os.path.abspath('.')
            filename = os.path.basename(imgurl)
            imgpath = os.path.join(dir, filename)
            print(' Fe FR %s' % imgurl)
            download_jpg(imgurl, imgpath)