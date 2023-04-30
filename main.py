import selenium
from selenium import webdriver

input("Enter your URL: ")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://syndication.exdynsrv.com/splash.php?cat=&idzone=4970886&type=8&p=https%3A%2F%2Ftoonily.com%2Fwebtoon%2Fwriter-sungs-life%2F&sub=&block=1&el=&tags=&cookieconsent=true&scr_info=aW5saW5lfHBvcE1hZ2ljfDE%3D")
# access HTML source code with page_source method
sourceCode = driver.page_source

def getallscripts(sourceCode,sWord,eWord):
   
    startScript = [
        index for index in range(len(sourceCode))
        if sourceCode.startswith(sWord, index)
    ]
    endScript = [
        index for index in range(len(sourceCode))
        if sourceCode.startswith(eWord, index)
    ]

    allScripts=""
    for i in range(len(startScript)):
        allScripts+=(sourceCode[startScript[i]:endScript[i]+8])+'\n'

    return allScripts


alljs=getallscripts(sourceCode,'<script','/script>')
allphp=getallscripts(sourceCode,'<php?','?>')
import pickle
with open('alljs.txt', 'wb') as f:
    pickle.dump(alljs,f)
with open('allphp.txt', 'wb') as f:
    pickle.dump(allphp,f)


import words_list

print("_"*64)
print("-"*64)

alertflag=False
for x in words_list.phplist:
    if (allphp.find(x)) != -1:
        print("Your website's PHP code poses DANGER")
        print("THREAT KEYWORD: ",x)
        alertflag=True

if alertflag==False:
    print("Your website PHP code is safe")

print("_"*64)

alertflag=False    
for x in words_list.scriptlist:
    if (alljs.find(x)) != -1:
        print("Your website's JS code poses DANGER !!")
        print("THREAT KEYWORD: ",x)
        alertflag=True

if alertflag==False:
    print("Your website JS code is safe")

print("_"*64)
print("-"*64)

input()