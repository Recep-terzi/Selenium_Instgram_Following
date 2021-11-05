from selenium import webdriver
import loginInfo
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get("https://instgram.com")

time.sleep(1)

username = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

giris_yap = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")

giris_yap.click()

time.sleep(4)

giris_yap2 = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")

giris_yap2.click()

giris_yap3 = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
giris_yap3.click()


time.sleep(2)
profil = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]")
profil.click()
time.sleep(2)
takip = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div")
takip.click()
time.sleep(2)
takip = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]")
takip.click()
time.sleep(5)


jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(1)
followersList = []

followers =browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="utf-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
browser.close()
    


