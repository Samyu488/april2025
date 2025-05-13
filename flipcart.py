
import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/tyy/4io/~cs-xj7gdemumj/pr?sid=tyy,4io&collection-tab-name=Redmi+Note+12+Pro+5G&param=6765363&otracker=clp_banner_1_13.bannerX3.BANNER_mobile-phones-big-saving-days-jan23-56hj-store_FMM4NVEBNJK7&fm=neo%2Fmerchandising&iid=M_75a6c7e3-723f-4a0b-89f7-0f66d112fff6_13.FMM4NVEBNJK7&ppt=hp&ppn=homepage&ssid=2bmt249nlc0000001678801426964")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('div',class_='KzDlHZ')
print(names)
for i in names[0:10]:
    d=i.get_text()
    print(d)
    names=[]
    names.append(d)
    print(names)
prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
print(prices)
for i in prices[0:10]:
    d=i.get_text()
    print(d)
    prices=[]
    prices.append(d)
    print(prices)
ratings=soup.find_all('div',class_='XQDdHH')
print(ratings)
for i in ratings[0:10]:
    d=i.get_text()
    print(d)
    ratings=[]
    ratings.append(d)
    print(ratings)
images=soup.find_all('img',class_='DByuf4')
print(images)
for i in images[0:10]:
    d= i['src']
    print(d)
    images=[]
    images.append(d)
    print(images)
    df=pandas.DataFrame()
    #print(df)
    df['Names']=names
    df['prices']=prices
    df['ratings']=ratings
    df['images']=images
    print(df)
    df.to_csv('Mobilesaprilbatch.cvs')



    




















































































