import datetime

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import *

wb = load_workbook('Data Base.xlsx')
sheet = wb['Criptos']

driver = webdriver.Chrome(r'chromedriver.exe')

websites = ['https://coinmarketcap.com/pt-br/currencies/shiba-inu/',
            'https://coinmarketcap.com/pt-br/currencies/tether/',
            'https://coinmarketcap.com/pt-br/currencies/bittorrent/',
            'https://coinmarketcap.com/pt-br/currencies/gala/',
            'https://coinmarketcap.com/pt-br/currencies/xrp/',
            'https://coinmarketcap.com/pt-br/currencies/binance-coin/']

cell = 9

comma = ''
pont = ''

for website in websites:
    driver.get(website)

    crypto = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/h2/small').text
    last_purchases_24hr = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/span').text
    current_value = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
    growth = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/span').text
    profit_loss_growth = driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div[1]/table/tbody/tr[2]/td/span').text

    if profit_loss_growth[2] == '-':
        growth = '-' + growth

    new_current_value = current_value[2:]

    if '.' in new_current_value[-3:]:
        pont = new_current_value[-3:]
        pont = pont.replace('.', ',')
    else:
        pont = new_current_value[-3:]

    if ',' in new_current_value[:-3]:
        comma = new_current_value[:-3]
        comma = comma.replace(',', '.')
    else:
        comma = new_current_value[:-3]

    if int(new_current_value[0]) == 0:
        current_value = new_current_value.replace('.', ',')
    else:
        current_value = comma + pont

    sheet[f'A{cell}'] = crypto
    sheet[f'D{cell}'] = current_value
    sheet[f'G{cell}'] = growth
    sheet[f'J{cell}'] = last_purchases_24hr

    wb.save(f'Data Base - {datetime.date.today()}.xlsx')

    cell += 1