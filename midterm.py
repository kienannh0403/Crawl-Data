import bs4
import pandas
import requests
import keyboard
from random import choice
import requests
import time
from collections import OrderedDict
from selenium import webdriver
import os
import tkinter as tk

# def selenium_checkbox():
# 	PATH = "C:/Users/LTKA/Desktop/midterm/chromedriver.exe"
# 	driver = webdriver.Chrome(PATH)
# 	driver.implicitly_wait(100)
# 	driver.get("https://youtube.com")
# 	# status = driver.find_element_by_class("recaptcha-checkbox-border").is_select()
# 	# driver.find_element_by_class("appsMaterialWizButtonPaperbuttonContent exportButtonContent").click()
# 	driver.find_element_by_id("search-icon-legacy").click()
# 	driver.implicitly_wait(100)


def get_page_content(url):

	header = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/9.0.570.1 Safari/534.11"}
	page = requests.get(url,headers=header)
	return bs4.BeautifulSoup(page.text,"html.parser")
def create_url(key):
    url_parent = 'https://vi.glosbe.com/vi/en/'
    temp =[]
    if '-' not in key:
        temp = key.split(' ')
    else:
        temp = key.split('-')
    url = url_parent
    url += temp[0]
    for j in range (1,len(temp)):
        url += '%20' + temp[j]
    return url
def trans(key):
	
    url = create_url(key)
    soup = get_page_content(url)
    result = soup.findAll('strong')

    for i in result:
        i.string.replace_with('_' + i.text + '_')

    tv = [tv.text for tv in soup.findAll('div',class_='translate-entry-translation-example-text')]
    if len(tv) == 0:
        tv = [tv.text for tv in set(soup.findAll('div',class_='translate-entry-empty-text ng-star-inserted'))]
    if len(tv) == 0:
        tv = [tv.text for tv in set(soup.findAll('div',class_='translate-entry-translation-query'))]
    if len(tv) == 0:
        tv = [tv.text for tv in set(soup.findAll('div',class_='translate-entry-summary-query'))]
    tv = list( OrderedDict.fromkeys(tv) )
    
    return tv if len(tv) > 0 else 'garp13'

def pause_key():
	if keyboard.is_pressed('s'):  # if key 'q' is pressed 
		print('Bạn đang tạm dừng chương trình')
		input("Nhấn Enter để tiếp tục")
	else:
		pass
def split_words(a):
	b = a.split('_')
	return b[1]

def crawl_dict_to_text():
	f = open('Viet11k.txt',encoding="utf-8")
	st = f.read().split('\n')
	print('Nhấn S để pause')
	x = 1
	for i in st[0:3]:
		pause_key()	
		while trans(i) == 'garp13':
			input("Đang bị tạm dừng, bạn cần vào trang web xác minh sau đó nhấn enter")
		transi = trans(i)
		temp1 = str()
		temp2 = str()
		mean = str()
		mean2 = str()
		means = [10]
		example = str()
		example1 = str()
		num = 1
		countspace = 1
		for j in transi:
			temp1 += (j + '\n')

			if num == 1:
				mean += (j)
			if num == 2:
				mean2 += (j)
			num += 1	
		temp1 = temp1[:-1]

		example = temp1.split(mean)
		print(x)
		if str(mean).count(' ') > 2:
			example1 += mean

		if str(mean2).count('_') > 1:
			sent = str(mean2)
			means.append((split_words(sent)))
		else:
			means.append(str(mean))
		os.chdir('C:/Users/LTKA/Desktop/midterm/Dict')
		with open(i+'.txt','a',encoding="utf-8") as f:
			f.truncate(0)
			f.write("Từ Tiếng Anh tương ứng: " + str(means[1]) +'\n')
			f.write("Từ đồng nghĩa và câu: "+'\n'+example1 +str(example[1]) +  '\n')
			x += 1
	print('done')

crawl_dict_to_text()



