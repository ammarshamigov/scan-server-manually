from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
ip = str(input(" Enter IP : "))
word = str(input(" Enter word : "))
url = 'http://www.bing.com/search?q=ip%3A'+ip+'+'+word
openurl = urllib.request.urlopen(url) 
read = openurl.read()
soup = BeautifulSoup(read,"html.parser")
for i in soup.findAll("li",{"class":"b_algo"}):
        print(" [ + ] Found ->\033[93m "+i.a.get("href"))

def test2(ip):
    word = str(input(" Enter word : "))
    url = 'http://www.bing.com/search?q=ip%3A'+ip+'+'+word
    openurl = urllib.request.urlopen(url) 
    read = openurl.read()
    soup = BeautifulSoup(read,"html.parser")
    for i in soup.findAll("li",{"class":"b_algo"}):
        print(" [ + ] Found ->\033[93m "+i.a.get("href"))

while True:
    check = str(input("you want contunie [ y <> n ] :"))
    if check == "y":
        test2(ip)
    else:
        break
    
