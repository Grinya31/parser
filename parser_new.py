import requests
from bs4 import BeautifulSoup
from time import sleep
import json
import csv


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

category={}
category_tov={}
spis=[]
link='https://shop.kerama-marazzi.ru/'
responce=requests.get(link,headers=headers)
soup=BeautifulSoup(responce.text,'lxml')
spisok_cat=soup.find('ul',class_="child collapse").find_all('li')
all_collections=soup.find('ul', class_="accordion-menu").find_all('li',class_="has-child")
count=0

for col in all_collections:
    if count==0:

        name_col=col.find('a').text.strip()
        url='https://shop.kerama-marazzi.ru'+col.find('a').get('href')
        spisok_cat=col.find('ul',class_="child collapse").find_all('li')
        for tov in spisok_cat:
            name_tov=tov.find('a').text.strip()
            url='https://shop.kerama-marazzi.ru'+tov.find('a').get('href')
            responce=requests.get(url,headers=headers)
            soup_tov=BeautifulSoup(responce.text,'lxml')
            vse_tovar=soup_tov.find_all('div',class_="col-xl-3 col-md-4 col-sm-6 mt-3")
            for i in vse_tovar:
                name_url=i.find_all('a')
                name=name_url[1].text

                url='https://shop.kerama-marazzi.ru'+name_url[1].get('href')
                price=i.find('div',class_="price-wrap").find('div',class_="price").find_all('div', class_="current")
                if len(price)>1:
                    price=price[1].text
                else:
                    price=price[0].text
                b=[name,url,price]
                spis.append(b)
                category[name_tov]=spis
            spis=[]
                
              
        category_tov[name_col]=category
        count+=1       
       ##with open(f'{name_col}.csv','a', encoding='utf-8') as file:
            ##writer=csv.writer(file)
            ##writer.writerow(
                ##(
                       # #"Имя",
                        #"Адрес",
                        #"Цена"

               # #)
            #)    

            
                
        #with open(f'{name_col}.csv','a', encoding='utf-8') as file:
            #writer=csv.writer(file)
            #writer.writerows(spis)
                       

                
        #category_tov={}
        
with open(f'category_{name_col}.json','a',encoding='utf-8') as file:
    json.dump(category_tov, file, indent=4, ensure_ascii=False)
       

#print(spisok_cat)
#with open("category.json",'w',encoding='utf-8') as file:
   #json.dump(category, file, indent=4, ensure_ascii=False)
#count=0
#for category_name, category_href in category.items():
    #if count=0
   # #cat_tovar={}

    #req=requests.get(category_href,headers=headers)
    #soup=BeautifulSoup(req.text,'lxml')
    
    
    #for col in all_collections:
        #name=col.text.strip()
        #url='https://shop.kerama-marazzi.ru'+col.find('a').get('href')
        #cat_tovar[name]=url
        


           
        #with open(f'category_all_{count}.json','w',encoding='utf-8') as file:
            #json.dump(cat_tovar, file, indent=4, ensure_ascii=False)
    #count+=1
 
        #pagination=soup.find('div', class_="pagination-section")
    #if pagination is not None:
        #all_page=int(pagination.find('li',class_='next').find_previous_sibling('li').text)
        #for page in range(1,all_page+1):

    #else:
        #for collection in all_collections:
            #name=collection.text.strip()
            #url='https://shop.kerama-marazzi.rucollection.get'+collection.find('a').get('href')
  

 
   
  #straniza=vsego_straniz.find_previous_siblings('li')

    
#def get_card_url(my_dict):
    #for count in range(1,col+1):
        #url=f'f{count}'
        #response=requests.get(url,headers=headers)
        #soup=BeautifulSoup(response.text,'lxml')
       # #cat_name=soup.find_all('div',class_="col-md-4 col-sm-6 text-center")
        #for i in cat_name:
            #name ="https://shop.kerama-marazzi.ru"+i.find('a').get('href')
            #y#ield name

#def array():
    #for card_url in get_card_url():
        #response=requests.get(card_url,headers=headers)
        #sleep(1)
        #soup=BeautifulSoup(response.text,'lxml')
        #tovars=soup.find_all('div',class_="col-xl-3 col-md-4 col-sm-6 mt-3")
        #for i in tovars:
           # #name=i.find('a', class_='title').text
            #link="https://shop.kerama-marazzi.ru"+i.find('a',class_='title').get('href')
            #img_link="https://shop.kerama-marazzi.ru"+i.find('a').get('href')
            #b=i.find('div',class_="price-wrap").find_all('div',class_="current")
            #if len(b)==0:
                #price="Товар выведен из ассортимента"
            #elif len(b)==1:
                #price=b[0].text 
            #else:
                #price=b[1].text

            #yield name,link,img_link,price
           
    


        

data={'https://shop.kerama-marazzi.ru/catalog/plitka-dlja-vannoj/':['https://shop.kerama-marazzi.ru/catalog/plitka-dlja-vannoj/?ysclid=lzlzwxkzxb703718618&PAGEN_1=',21],
      'https://shop.kerama-marazzi.ru/catalog/plitka-dlja-kuhni/': ['https://shop.kerama-marazzi.ru/catalog/plitka-dlja-kuhni/?PAGEN_1=', 19],
      'https://shop.kerama-marazzi.ru/catalog/keramicheskij-granit-kerama-marazzi/':['https://shop.kerama-marazzi.ru/catalog/keramicheskij-granit-kerama-marazzi/?PAGEN_1=',8],
      'https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi/':['https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi/?PAGEN_1=',2],
      'https://shop.kerama-marazzi.ru/catalog/keramicheskaya-plitka-kerama-marazzi-oboi/':['https://shop.kerama-marazzi.ru/catalog/keramicheskaya-plitka-kerama-marazzi-oboi/?PAGEN_1=',2]}


