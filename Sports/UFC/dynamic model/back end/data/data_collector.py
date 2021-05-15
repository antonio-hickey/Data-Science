#------------------------------------------
# Importing Python Modules
#------------------------------------------
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from collections import Iterable
import csv
import time
import datetime as dt
import pandas as pd

#------------------------------------------
# Browser Path
#------------------------------------------
PATH = "/home/sratus/Desktop/API/chromedriver"
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(ChromeDriverManager().install())

#------------------------------------------
# Data targeting
#------------------------------------------

# Timestamp
tStamp = dt.datetime.now().strftime('%m-%d-%Y')

# Completed Events
driver.get('http://www.ufcstats.com/statistics/events/completed')

# Click last event
last_event = driver.find_element_by_css_selector("tr.b-statistics__table-row:nth-child(3) > td:nth-child(1) > i:nth-child(1) > a:nth-child(1)")
last_event.click()

# Wait for 3 seconds
time.sleep(3)

# Figuring out about the table
table = driver.find_elements_by_xpath("/html/body/section/div/div/table/tbody/tr")

# For each fight in the range of fights
for nth in range(1,(len(table)+1)):
    # Defining Target Data 
    
    # Fighter 1
    f1 = driver.find_element_by_css_selector("tr.b-fight-details__table-row:nth-child({}) > td:nth-child(2) > p:nth-child(1) > a:nth-child(1)".format(nth))
    f1.click()
    f1_name = driver.find_element_by_css_selector("body > section > div > h2 > span.b-content__title-highlight").text
    f1_xp = driver.find_element_by_css_selector("body > section > div > h2 > span.b-content__title-record").text[8:]
    if " (" in f1_xp: # In case of NC which would otherwise break the script
        f1_xp = f1_xp.replace(' (1 NC)', '')
    f1_height = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(1)").text[8:]
    f1_weight = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(2)").text[8:12]
    f1_reach = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(3)").text[7:9]
    f1_stance = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(4)").text[8:]
    f1_age = (int(dt.date.today().year) - int(driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(5)").text[-4:]))
    f1_SLpM = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(1)").text[6:]
    f1_strAcc = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(2)").text[11:]
    f1_SApM = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(3)").text[6:]
    f1_strDef = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(4)").text[10:]
    f1_tdAvg = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(2)").text[9:]
    f1_tdAcc = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(3)").text[9:]
    f1_tdDef = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(4)").text[9:]
    f1_subAvg = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(5)").text[11:]

    if nth == 1:
        fight_1_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 2:
        fight_2_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 3:
        fight_3_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 4:
        fight_4_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 5:
        fight_5_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 6:
        fight_6_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 7:
        fight_7_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 8:
        fight_8_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 9:
        fight_9_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 10:
        fight_10_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 11:
        fight_11_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 12:
        fight_12_f1 = [tStampf1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 13:
        fight_13_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 14:
        fight_14_f1 = [tStamp,f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]
    if nth == 15:
        fight_15_f1 = [f1_name,f1_xp,f1_height,f1_weight,f1_reach,f1_stance,f1_age,f1_SLpM,f1_strAcc,f1_SApM,f1_strDef,f1_tdAvg,f1_tdAcc,f1_tdDef,f1_subAvg,1]

    # Go Back to fighters page
    driver.back()

    # Fighter 2
    f2 = driver.find_element_by_css_selector("body > section > div > div > table > tbody > tr:nth-child({}) > td:nth-child(2) > p:nth-child(2) > a".format(nth))
    f2.click() 
    f2_name = driver.find_element_by_css_selector("body > section > div > h2 > span.b-content__title-highlight").text
    f2_xp = driver.find_element_by_css_selector("body > section > div > h2 > span.b-content__title-record").text[8:]
    if " (" in f2_xp: # In case of NC which would otherwise break the script
        f2_xp = f2_xp.replace(' (1 NC)', '')
    f2_height = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(1)").text[8:]
    f2_weight = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(2)").text[8:12]
    f2_reach = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(3)").text[7:9]
    f2_stance = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(4)").text[8:]
    f2_age = (int(dt.date.today().year) - int(driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_small-width.js-guide > ul > li:nth-child(5)").text[-4:]))
    f2_SLpM = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(1)").text[6:]
    f2_strAcc = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(2)").text[11:]
    f2_SApM = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(3)").text[6:]
    f2_strDef = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-left > ul > li:nth-child(4)").text[10:]
    f2_tdAvg = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(2)").text[9:]
    f2_tdAcc = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(3)").text[9:]
    f2_tdDef = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(4)").text[9:]
    f2_subAvg = driver.find_element_by_css_selector("body > section > div > div > div.b-list__info-box.b-list__info-box_style_middle-width.js-guide.clearfix > div.b-list__info-box-left.clearfix > div.b-list__info-box-right.b-list__info-box_style-margin-right > ul > li:nth-child(5)").text[11:]

    # Storing data
    if nth == 1:
        fight_1_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 2:
        fight_2_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 3:
        fight_3_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 4:
        fight_4_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 5:
        fight_5_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 6:
        fight_6_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 7:
        fight_7_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 8:
        fight_8_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 9:
        fight_9_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 10:
        fight_10_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 11:
        fight_11_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 12:
        fight_12_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 13:
        fight_13_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 14:
        fight_14_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    if nth == 15:
        fight_15_f2 = [f2_name,f2_xp,f2_height,f2_weight,f2_reach,f2_stance,f2_age,f2_SLpM,f2_strAcc,f2_SApM,f2_strDef,f2_tdAvg,f2_tdAcc,f2_tdDef,f2_subAvg,0]
    
    # Go Back to fighter's page
    driver.back()

#------------------------------------------
# Output data to csv
#------------------------------------------

# Flatten list to 1 dimensional
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

# Output filename
filename = "historical.csv"

# Data structuring
columns = ["f1 name", "f1 xp","f1 height", "f1 weight", "f1 reach", "f1 stance", "f1 age", "f1 sig str lpm", "f1 sig str acc", "f1 sig str abs","f1 sig str def", "f1 td avg", "f1 td acc", "f1 td def", "f1 sub avg","Result",
           "f2 name", "f2 xp","f2 height", "f2 weight", "f2 reach", "f2 stance", "f2 age", "f2 sig str lpm", "f2 sig str acc", "f2 sig str abs","f2 sig str def", "f2 td avg", "f2 td acc", "f2 td def", "f2 sub avg","Result"]
# Number of fights
n_fights = len(table)
if n_fights == 9:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9]
if n_fights == 10:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10]
if n_fights == 11:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    fight_11 = list(flatten(fight_11_f1 + fight_11_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10,fight_11]
if n_fights == 12:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    fight_11 = list(flatten(fight_11_f1 + fight_11_f2))
    fight_12 = list(flatten(fight_12_f1 + fight_12_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10,fight_11,fight_12]
if n_fights == 13:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    fight_11 = list(flatten(fight_11_f1 + fight_11_f2))
    fight_12 = list(flatten(fight_12_f1 + fight_12_f2))
    fight_13 = list(flatten(fight_13_f1 + fight_13_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10,fight_11,fight_12,fight_13]
if n_fights == 14:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    fight_11 = list(flatten(fight_11_f1 + fight_11_f2))
    fight_12 = list(flatten(fight_12_f1 + fight_12_f2))
    fight_13 = list(flatten(fight_13_f1 + fight_13_f2))
    fight_14 = list(flatten(fight_14_f1 + fight_14_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10,fight_11,fight_12,fight_13,fight_14]
if n_fights == 15:
    fight_1 = list(flatten(fight_1_f1 + fight_1_f2))
    fight_2 = list(flatten(fight_2_f1 + fight_2_f2))
    fight_3 = list(flatten(fight_3_f1 + fight_3_f2))
    fight_4 = list(flatten(fight_4_f1 + fight_4_f2))
    fight_5 = list(flatten(fight_5_f1 + fight_5_f2))
    fight_6 = list(flatten(fight_6_f1 + fight_6_f2))
    fight_7 = list(flatten(fight_7_f1 + fight_7_f2))
    fight_8 = list(flatten(fight_8_f1 + fight_8_f2))
    fight_9 = list(flatten(fight_9_f1 + fight_9_f2))
    fight_10 = list(flatten(fight_10_f1 + fight_10_f2))
    fight_11 = list(flatten(fight_11_f1 + fight_11_f2))
    fight_12 = list(flatten(fight_12_f1 + fight_12_f2))
    fight_13 = list(flatten(fight_13_f1 + fight_13_f2))
    fight_14 = list(flatten(fight_14_f1 + fight_14_f2))
    fight_15 = list(flatten(fight_15_f1 + fight_15_f2))
    rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6,fight_7,fight_8,fight_9,fight_10,fight_11,fight_12,fight_13,fight_14,fight_15]

# Rendering csv dataset
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in rows: # for each row write row
        print(row)
        csvwriter.writerow(row)
