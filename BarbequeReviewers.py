import csv 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d1132694-\
Reviews-Barbeque_Nation-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d4312086-\
Reviews-Barbeque_Nation-New_Delhi_National_Capital_Territory_of_Delhi.html"
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


url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d785303-\
Reviews-The_Great_Kabab_Factory-New_Delhi_National_Capital_Territory_of_Delhi.html"
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


url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d5788719-\
Reviews-Pirates_of_Grill-New_Delhi_National_Capital_Territory_of_Delhi.html"
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


url = "https://www.tripadvisor.com/Restaurant_Review-g304551-d4097502-\
Reviews-Barbeque_Nation-New_Delhi_National_Capital_Territory_of_Delhi.html"
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
