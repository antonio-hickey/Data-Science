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

# Get UFC Schedule
driver.get('https://www.espn.com/mma/schedule/_/league/ufc')

# Select next fight link
next_fight = driver.find_element_by_css_selector("div.Schedule__EventLeague:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)")
next_fight.click()

# Wait 3 seconds after link clicked
time.sleep(3)

# Get number of fights
n_mainCard = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[3]/div/div[1]/div[2]/section/div/div/div")

# Fight 1
f1_name = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__header.pointer > div.MMAFightCard__Gamestrip.br-5.mh4.relative.MMAFightCard__Gamestrip--open > div > div > div.MMACompetitor.relative.flex.flex-uniform.pr6.flex-row-reverse.MMACompetitor--desktop > div > div.MMACompetitor__Detail.flex.flex-column.justify-center > h2 > span").text 
f1_height = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(1) > div:nth-child(1) > div > div").text
f1_weight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(2) > div:nth-child(1) > div > div").text
f1_reach = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(3) > div:nth-child(1) > div > div").text
f1_stance = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(4) > div:nth-child(1) > div > div").text
f1_sig_str_lpm = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(5) > div:nth-child(1) > div > div").text
f1_sig_str_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(6) > div:nth-child(1) > div > div").text
f1_td_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(7) > div:nth-child(1) > div > div").text
f1_td_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(8) > div:nth-child(1) > div > div").text
f1_sub_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(9) > div:nth-child(1) > div > div").text
f2_name = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__header.pointer > div.MMAFightCard__Gamestrip.br-5.mh4.relative.MMAFightCard__Gamestrip--open > div > div > div.MMACompetitor.relative.flex.flex-uniform.pl6.MMACompetitor--desktop > div > div.MMACompetitor__Detail.flex.flex-column.justify-center > h2 > span").text
f2_height = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(1) > div.MMAMatchup__Basis.tar > div > div").text
f2_weight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(2) > div.MMAMatchup__Basis.tar > div > div").text
f2_reach = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(3) > div.MMAMatchup__Basis.tar > div > div").text
f2_stance = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(4) > div.MMAMatchup__Basis.tar > div > div").text
f2_sig_str_lpm = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(5) > div.MMAMatchup__Basis.tar > div > div").text
f2_sig_str_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(6) > div.MMAMatchup__Basis.tar > div > div").text
f2_td_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(7) > div.MMAMatchup__Basis.tar > div > div").text
f2_td_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(8) > div.MMAMatchup__Basis.tar > div > div").text
f2_sub_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(9) > div.MMAMatchup__Basis.tar > div > div").text

# Log Data
fight_1 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]


# Close Div after data collected
click_fight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child(1) > div.AccordionPanel__header.pointer")
click_fight.click()


# For loop for each fight
for j in range(2,len(n_mainCard)+1):
    # Show div 
    click_fight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__header.pointer".format(j))
    click_fight.click()
    # Targeting data for nth fight
    f1_name = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__header.pointer > div.MMAFightCard__Gamestrip.br-5.mh4.relative.MMAFightCard__Gamestrip--open > div > div > div.MMACompetitor.relative.flex.flex-uniform.pr6.flex-row-reverse.MMACompetitor--desktop > div > div.MMACompetitor__Detail.flex.flex-column.justify-center > h2 > span".format(j)).text 
    f1_height = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(1) > div:nth-child(1) > div > div".format(j)).text
    f1_weight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(2) > div:nth-child(1) > div > div".format(j)).text
    f1_reach = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(3) > div:nth-child(1) > div > div".format(j)).text
    f1_stance = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(4) > div:nth-child(1) > div > div".format(j)).text
    f1_sig_str_lpm = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(5) > div:nth-child(1) > div > div".format(j)).text
    f1_sig_str_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(6) > div:nth-child(1) > div > div".format(j)).text
    f1_td_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(7) > div:nth-child(1) > div > div".format(j)).text
    f1_td_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(8) > div:nth-child(1) > div > div".format(j)).text
    f1_sub_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(9) > div:nth-child(1) > div > div".format(j)).text
    f2_name = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__header.pointer > div.MMAFightCard__Gamestrip.br-5.mh4.relative.MMAFightCard__Gamestrip--open > div > div > div.MMACompetitor.relative.flex.flex-uniform.pl6.MMACompetitor--desktop > div > div.MMACompetitor__Detail.flex.flex-column.justify-center > h2 > span".format(j)).text
    f2_height = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(1) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_weight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(1) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_reach = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(3) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_stance = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(4) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_sig_str_lpm = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(5) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_sig_str_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(6) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_td_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(7) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_td_acc = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(8) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    f2_sub_avg = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__body > div > div > div > div.ResponsiveWrapper > div > div.flex.pb4 > div.MMAFightCenter__Matchup > div > ul > li:nth-child(9) > div.MMAMatchup__Basis.tar > div > div".format(j)).text
    
    # Log data
    if j == 2:
        fight_2 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]
    if j == 3:
        fight_3 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]
    if j == 4:
        fight_4 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]
    if j == 5:
        fight_5 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]
    if j == 6:
        fight_6 = [f1_name,f1_height,f1_weight,f1_reach,f1_stance,f1_sig_str_lpm,f1_sig_str_acc,f1_sub_avg, f2_name,f2_height,f2_weight,f2_reach,f2_stance,f2_sig_str_lpm,f2_sig_str_acc,f2_sub_avg]

    # Collapse div when done so the bot doesnt have to scroll
    click_fight = driver.find_element_by_css_selector("#fittPageContainer > div:nth-child(4) > div > div.PageLayout__Main > div:nth-child(2) > section > div > div > div:nth-child({}) > div.AccordionPanel__header.pointer".format(j))
    click_fight.click()

#------------------------------------------
# Output data to csv
#------------------------------------------

# Output filename
filename = "next_fight.csv"

# Data structuring
columns = ["f1 name", "f1 height", "f1 weight", "f1 reach", "f1 stance", "f1 sig str lpm", "f1 sig str acc", "f1 sub avg","f2 name", "f2 height", "f2 weight", "f2 reach", "f2 stance", "f2 sig str lpm", "f2 sig str acc", "f2 sub avg"]
rows = [fight_1,fight_2,fight_3,fight_4,fight_5,fight_6]

# Rendering csv dataset
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(columns)
    for row in rows:                # for each row write row
        print(row)
        csvwriter.writerow(row)



