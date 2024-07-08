import requests
from bs4 import BeautifulSoup


for count in range(1,3):
    url=f'https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi/?PAGEN_1={count}'

    response=requests.get(url)


    soup = BeautifulSoup(response.text, 'lxml')

    name = soup.find_all('div',class_="col-md-4 col-sm-6 text-center")

    for i in name:
        name_catalog=i.find('img',class_="catalog-image equal").get('title').lower().replace(' ','_')
        url_a=f'https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi'+'-'+ name_catalog +'/'
        response=requests.get(url_a)
        soup=BeautifulSoup(response.text,'lxml')
        name_tov=soup.find_all('div',class_="col-xl-3 col-md-4 col-sm-6 mt-3")
    
        for i in name_tov:
            name=i.find('a',class_='title').text
            price=i.find('div',class_="price-wrap").text
            link=i.find('a',class_="title").get('href')
            print(name,price,link)

        
           

    
        


