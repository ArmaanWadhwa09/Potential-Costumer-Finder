import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d10427009-\
Reviews-Pling-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d18922351-\
Reviews-Mesa_Wine_Bistro-New_Delhi_National_Capital_Territory_of_Delhi.html"
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


url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d8002810-\
Reviews-JW_Lounge-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d8548577-Reviews\
-Perch_Wine_Coffee_Bar-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d13356845-Reviews\
-Chidya_Ghar-New_Delhi_National_Capital_Territory_of_Delhi.html"
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
