import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import *

wb = load_workbook('Data Base.xlsx')
sheet = wb['Criptos']

driver = webdriver.Chrome(r'C:\Users\Geovani Debastiani\.wdm\drivers\chromedriver\win32\95.0.4638.69\chromedriver.exe')

websites = ['https://coinmarketcap.com/pt-br/currencies/shiba-inu/',
            'https://coinmarketcap.com/pt-br/currencies/tether/',
            'https://coinmarketcap.com/pt-br/currencies/bittorrent/',
            'https://coinmarketcap.com/pt-br/currencies/gala/',
            'https://coinmarketcap.com/pt-br/currencies/xrp/',
            'https://coinmarketcap.com/pt-br/currencies/binance-coin/']

cell = 5

for website in websites:
    driver.get(website)
    time.sleep(2)

    last_purchases_24hr = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/span').text
    current_value = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
    growth = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/span').text

    new_current_value = current_value[2:].replace('.', ',')

    sheet[f'D{cell}'] = str(new_current_value)
    sheet[f'G{cell}'] = growth
    sheet[f'J{cell}'] = last_purchases_24hr

    wb.save(f'Data Base - {datetime.date.today()}.xlsx')

    cell += 1