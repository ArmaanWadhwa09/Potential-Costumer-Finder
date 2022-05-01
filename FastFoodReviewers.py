import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d14143916-Reviews\
-Spezia_Bistro-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d13414463-Reviews\
-Sandburg_Shakes_Aerocity-New_Delhi_National_Capital_Territory_of_Delhi.html"
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


url = "https://www.tripadvisor.ca/Restaurant_Review-g644043-d1205338-\
Reviews-McDonald_s-Noida_Gautam_Buddha_Nagar_District_Uttar_Pradesh.html"
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


url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d5786476-Reviews\
-Epicuria-New_Delhi_National_Capital_Territory_of_Delhi.html"
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

url = "https://www.tripadvisor.ca/Restaurant_Review-g304551-d17426190-Reviews\
-Housefull-New_Delhi_National_Capital_Territory_of_Delhi.html"
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
