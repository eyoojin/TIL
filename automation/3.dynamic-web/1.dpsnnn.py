from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date, timedelta
import time
import csv

# 클릭하는 것이 너무 비효율적이라 클릭하지 않고 데이터 수집하는 것으로 변경

driver = webdriver.Chrome()

URL = 'https://dpsnnn-s.imweb.me/reserve_ss'
driver.get(URL)

# booking_list = driver.find_elements(By.CSS_SELECTOR, 'div.booking_list:not(.closed)')

# bookable_list = {}
title_list = {}
target_date = []

start_date = date(2025, 4, 15)
for j in range(6):
    current_date = start_date + timedelta(days=j)
    date_str = current_date.strftime('%Y-%-m-%d')
    target_date.append(date_str)

# print(target_date)

for k in target_date:
    selector  = f"td[data-date={k}] div.booking_list:not(.closed)"
    booking_list = driver.find_elements(By.CSS_SELECTOR, selector)
    time.sleep(1)

    # for i in range(len(booking_list)):

    #     print(booking_list[i].text)
    #     if booking_list[i].text == '-':
    #         continue
    #     else:
    #         booking_list[i].click()
        
    #     time.sleep(1)
    #     title = driver.find_element(By.CSS_SELECTOR, 'div.title').get_attribute('innerHTML')
    #     booking_date = driver.find_element(By.CSS_SELECTOR, 'div.text-brand').text

    #     title_list.append(title)
    #     bookable_list[booking_date] = title_list

    #     driver.back()

    for i in range(len(booking_list)):
        selector = f"td[data-date='{k}'] div.booking_list:not(.closed)"
        booking_list_temp = driver.find_elements(By.CSS_SELECTOR, selector)
        element = booking_list_temp[i]
        text = element.find_element(By.CSS_SELECTOR, 'span.text').text
        
        if text == '-':
            continue
        else:
            title = text[:2].strip()
            booking_time = text[4:].strip()
    
        if title not in title_list:
            title_list[title] = []
        title_list[title].append(f'{k} / '+ booking_time)

print(title_list)