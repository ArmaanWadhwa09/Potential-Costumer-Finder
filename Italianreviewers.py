import csv #This package lets us save data to a csv file
from selenium import webdriver #The Selenium package we'll need
import time #This package lets us pause execution for a bit
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d8703583-\
Reviews-Mosaic-New_Delhi_National_Capital_Territory_of_Delhi.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
content = driver.page_source
products=[]
soup = BeautifulSoup(content, features="lxml")
a = soup.find_all("div" , class_ = "review-container")
L = []
for item in a:
    title = item.find("div", class_ = "info_text pointer_cursor")
    L.append(title.text)
P = []
for i in range(len(L)):
        if L[i] not in P:
            P.append(L[i])

url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d4462993-\
\Reviews-Edesia_Crowne_Plaza_Today_New_Delhi_Okhla-New_Delhi_\
National_Capital_Territory_of.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
content = driver.page_source
products=[]
soup = BeautifulSoup(content, features="lxml")
a = soup.find_all("div" , class_ = "review-container")
L = []
for item in a:
    title = item.find("div", class_ = "info_text pointer_cursor")
    L.append(title.text)
for i in range(len(L)):
        if L[i] not in P:
            P.append(L[i])


url = "hhttps://www.tripadvisor.com/Restaurant_Review-g304551-d9796435-\
Reviews-Sorrento-New_Delhi_National_Capital_Territory_of_Delhi.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
content = driver.page_source
products=[]
soup = BeautifulSoup(content, features="lxml")
a = soup.find_all("div" , class_ = "review-container")
L = []
for item in a:
    title = item.find("div", class_ = "info_text pointer_cursor")
    L.append(title.text)
for i in range(len(L)):
        if L[i] not in P:
            P.append(L[i])


url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d21325917-Review\
s-Out_Of_The_Box_Courtyard-New_Delhi_National_Capital_Territory_of_Delhi.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
content = driver.page_source
products=[]
soup = BeautifulSoup(content, features="lxml")
a = soup.find_all("div" , class_ = "review-container")
L = []
for item in a:
    title = item.find("div", class_ = "info_text pointer_cursor")
    L.append(title.text)
for i in range(len(L)):
        if L[i] not in P:
            P.append(L[i])

url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d13508233-Reviews\
-FatJar_Cafe_Market-New_Delhi_National_Capital_Territory_of_Delhi.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
content = driver.page_source
products=[]
soup = BeautifulSoup(content, features="lxml")
a = soup.find_all("div" , class_ = "review-container")
L = []
for item in a:
    title = item.find("div", class_ = "info_text pointer_cursor")
    L.append(title.text)
    for i in range(len(L)):
        if L[i] not in P:
            P.append(L[i])

path_to_file = open("/Users/armaanwadhwa/Desktop/Reviewers.csv", "w")
f = csv.writer(path_to_file)
for i in P:
    f.writerow([i])
path_to_file.close()
