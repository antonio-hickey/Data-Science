#------------------------------------
# Import Modules                    #
#------------------------------------
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import pathlib
import datetime
import json
import re
import csv
#------------------------------------
# Data Mining                       #
#------------------------------------

urls = [
    "https://www.espn.com/nfl/team/stats/_/name/ari", "https://www.espn.com/nfl/team/stats/_/name/atl", "https://www.espn.com/nfl/team/stats/_/name/bal",
    "https://www.espn.com/nfl/team/stats/_/name/buf", "https://www.espn.com/nfl/team/stats/_/name/car", "https://www.espn.com/nfl/team/stats/_/name/chi",
    "https://www.espn.com/nfl/team/stats/_/name/cin", "https://www.espn.com/nfl/team/stats/_/name/cle", "https://www.espn.com/nfl/team/stats/_/name/dal",
    "https://www.espn.com/nfl/team/stats/_/name/den", "https://www.espn.com/nfl/team/stats/_/name/det", "https://www.espn.com/nfl/team/stats/_/name/gb",
    "https://www.espn.com/nfl/team/stats/_/name/hou", "https://www.espn.com/nfl/team/stats/_/name/ind", "https://www.espn.com/nfl/team/stats/_/name/jax",
    "https://www.espn.com/nfl/team/stats/_/name/kc", "https://www.espn.com/nfl/team/stats/_/name/lv", "https://www.espn.com/nfl/team/stats/_/name/lac",
    "https://www.espn.com/nfl/team/stats/_/name/lar", "https://www.espn.com/nfl/team/stats/_/name/mia", "https://www.espn.com/nfl/team/stats/_/name/min",
    "https://www.espn.com/nfl/team/stats/_/name/ne", "https://www.espn.com/nfl/team/stats/_/name/no", "https://www.espn.com/nfl/team/stats/_/name/nyg",
    "https://www.espn.com/nfl/team/stats/_/name/nyj", "https://www.espn.com/nfl/team/stats/_/name/phi", "https://www.espn.com/nfl/team/stats/_/name/pit",
    "https://www.espn.com/nfl/team/stats/_/name/sf", "https://www.espn.com/nfl/team/stats/_/name/sea", "https://www.espn.com/nfl/team/stats/_/name/tb",
    "https://www.espn.com/nfl/team/stats/_/name/ten", "https://www.espn.com/nfl/team/stats/_/name/wsh"
]

#for url in urls:
#    uClient = uReq(url) # Requesting target url
#    page_soup = soup(uClient.read(), "html.parser") # Reading html data of target site
#    uClient.close() # Close Soup

url = "https://www.espn.com/nfl/team/stats/_/name/atl"
uClient = uReq(url) # Requesting target url
page_soup = soup(uClient.read(), "html.parser") # Reading html data of target site
json_data = page_soup.find_all('script', {'type':'text/javascript'})
test_j = json.loads(json_data)
print(test_j)

uClient.close() # Close Soup


#------------------------------------
# Output Data to csv                #
#------------------------------------
#PATH = pathlib.Path(__file__).parent
#with open(PATH.joinpath('data.csv'), 'a') as f:
#    writer = csv.writer(f)
#    writer.writerow(title)
