from urllib.request import urlopen 
from bs4 import BeautifulSoup 
from urllib.error import URLError 
from time import sleep  
while True: 
    try: 
        html = urlopen('http://coinranking.com/') 
        bs = BeautifulSoup(html.read(),'lxml') 
         
        table_rows= bs.find_all('div',{'class':'valuta'}) 
         
        for i in range(0,10,2): 
            print(f"{i}===========================") 
         
            price_string = table_rows[i].get_text().replace('$','').replace(" " ,"").replace("\n","").replace("," ,"") 
            price = float(price_string) 
            print(price) 
            print("******") 
    except URLError as e: 
        print('you should connect ot internt') 
        sleep(1)  