from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import xlrd
import openpyxl
import os
import string
from selenium import webdriver

#dir = r'C:\Users\Tien'
#os.chdir(dir)

########### input excel ##########
input_workbook = xlrd.open_workbook("aktie.xlsx")

input_worksheet = input_workbook.sheet_by_index(0)



############### output excel ####################
rawdata_workbook = openpyxl.load_workbook('rawdata.xlsx')

rawdata_worksheet = rawdata_workbook.get_sheet_by_name('Sheet1')


################### global variables ####################
################### index - 2 ###########################
i = 1805
alphabet = list(string.ascii_uppercase)

browser = webdriver.Firefox()


while i <= 1805:
	try:

		i = i + 1 
		
		my_url = input_worksheet.cell(i,0).value

		finanzen_stockname = my_url.replace("http://www.finanzen.net/aktien/","")


		print('http://www.finanzen.net/bilanz_guv/' + finanzen_stockname.replace("-Aktie",""))

		guv_url = 'http://www.finanzen.net/bilanz_guv/' + finanzen_stockname.replace("-Aktie","")


		###########################################   MAIN SITE  http://www.finanzen.net/aktien/BASF-Aktie #############################################

		#url reader function
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		page_soup = soup(page_html, "html.parser")

		#grab isin
		try:
			isin = page_soup.findAll("span",{"class":"instrument-id"})

			isin = isin[0].text

			if isin[0:4] == "ISIN":
				isin = isin[6:17]
			else:
				isin = isin[20:32]

			isin_index = 'A' + str(i-47)
			rawdata_worksheet[isin_index] = isin

		except Exception as e:
			print('no ISIN')


		#grab name

		try:
			stock_index = 'B' + str(i-47)
			rawdata_worksheet[stock_index] = finanzen_stockname.replace("-Aktie","")

		except Exception as e:
			print('no stockname')

		#grab newest stock price

		try:
			stock = page_soup.findAll("div",{"class":"col-xs-5"})

			eur_price = stock[0].contents[0]

			eur_price_index = 'C' + str(i-47)
			rawdata_worksheet[eur_price_index] = eur_price

		except Exception as e:
			print('no stockdata')



		###########################################   BILANZ GUV   #############################################


		uClient = uReq(guv_url)
		page_html = uClient.read()
		uClient.close()

		page_soup = soup(page_html, "html.parser")
		guv = page_soup.findAll("td",{"class":"font-bold"})


		##############################################  check currency  ########################################
		try:
			currency = page_soup.findAll("h2",{"class":"box-headline"})
			currency = currency[0].text.split('(in ')
			currency = currency[1]
			currency = currency.replace(')','')
			currency_index = 'AW' + str(i-47)
			rawdata_worksheet[currency_index] = currency
		except Exception as e:
			print ('no currency')


		###################################### Boerse.de      ##############################################

		#########################################      grab price Feb 2009 ####################################

		try:
			browser.get('http://www.boerse.de/historische-kurse/wertpapier/'+ isin + '_jahr,2009#jahr')
			price2009 = browser.find_element_by_css_selector('table.table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(5)').text
			price2009index = 'AA' + str(i-47)
			rawdata_worksheet[price2009index] = price2009
		except Exception as e:
			print('no Feb 2009 data')

		

		#########################################      grab price Jan 2017 ######################################
		try:
			browser.get('http://www.boerse.de/historische-kurse/wertpapier/'+ isin + '_jahr,2017#jahr')
			price2017 = browser.find_element_by_css_selector('table.table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5)').text
			price2017index = 'AX' + str(i-47)
			rawdata_worksheet[price2017index] = price2017
		except Exception as e:
			print('no Jan 2017 data')

		rawdata_workbook.save('rawdata.xlsx')


	except Exception as e:
		print('error')