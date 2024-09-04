from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pandas as pd
#from selenium.webdriver.support.ui import WebDriverWait

#set variables
driver=webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('https://www.youtube.com/watch?v=4k4Ues5uAOw')   

driver.maximize_window()
sleep(2)

#scroll once to get comments
driver.execute_script("window.scrollBy(0,400)","")
sleep(3)
sort=driver.find_element(By.XPATH,"""//*[@id="label-icon"]/span/div""")
sort.click()
sleep(2)
newest=driver.find_element(By.XPATH,"""/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/div[2]/span/yt-sort-filter-sub-menu-renderer/yt-dropdown-menu/tp-yt-paper-menu-button/tp-yt-iron-dropdown/div/div/tp-yt-paper-listbox/a[2]/tp-yt-paper-item/tp-yt-paper-item-body/div[1]/div""")
newest.click()
sleep(2)

#loop, get comments
for i in range(15):
    driver.execute_script("window.scrollBy(0,700)","")
    sleep(2)
sleep(2)
comments=[]
usernames=[]
init_times=[]
times=[]

comment=driver.find_elements(By.XPATH,"""//*[@id="content-text"]/span""")
for i in comment:
    comments.append(i.text)
#print(comments)

username=driver.find_elements(By.XPATH,"""//*[@id="author-text"]/span""")
#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="author-text"]/span""")))
for j in username:
    usernames.append(j.text)
#print(usernames)

init_time=driver.find_elements(By.XPATH,"""//*[@id="published-time-text"]/a""")
for k in init_time:
    init_times.append(k.text)
#print(init_times)


for i in init_times:
    if(i[-10:-4]=="months"):
        inte=int(i[:-11]) #get number of months
        time=datetime.now()-relativedelta(months = inte)
        times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
    elif(i[-8:-4]=="days"):
        inte=int(i[:-9]) #get number of days
        time=datetime.now()-relativedelta(days = inte)
        times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
    elif(i[-9:-4]=="weeks"):
        inte=int(i[:-10]) #get number of hours
        time=datetime.now()-relativedelta(weeks = inte)
        times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
    elif(i[-9:-4]=="hours"):
        inte=int(i[:-10]) #get number of hours
        time=datetime.now()-relativedelta(hours = inte)
        times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
    else:
        if (i[-9:-4]=="month"):
            inte=int(i[:-10])
            time=datetime.now()-relativedelta(months= inte)
            times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
        elif (i[-7:-4]=="day"):
            inte=int(i[:-8])
            time=datetime.now()-relativedelta(days = inte)
            times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
        elif(i[-8:-4]=="week"):
            inte=int(i[:-9])
            time=datetime.now()-relativedelta(weeks = inte)
            times.append(time.strftime('%m-%d-%Y %H:%M:%S'))
        elif(i[-8:-4]=="hour"):
            inte=int(i[:-9])
            time=datetime.now()-relativedelta(hours = inte)
            times.append(time.strftime('%m-%d-%Y %H:%M:%S'))        
        else:
            print(f"heeree ~{i}~")

print(times)



print(len(comments))
print(len(usernames))
print(len(init_times))
print(len(times))

for i in range(len(times),len(usernames)):
    times.append(datetime.now().strftime('%m-%d-%Y %H:%M:%S'))


df=pd.DataFrame({"comment":comments,"username":usernames,"timestamp":times})
print(df)
#df.to_csv("you_tube_comment_1.csv",index=False)
df.to_excel('youtube_comments.xlsx')
# assert "No results found." not in driver.page_source
driver.close()
