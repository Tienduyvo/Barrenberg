from selenium import webdriver
import time
import openpyxl



aktie_workbook = openpyxl.load_workbook('Aktie.xlsx')

aktie_worksheet = aktie_workbook.get_sheet_by_name('Tabelle1')


browser = webdriver.Firefox()

j = 1
k = 484

while j <= 641:

    browser.get('http://finviz.com/screener.ashx?v=112&f=cap_largeover&o=-marketcap&r=' + str(j))
    j = j + 20

    i = 2
    elem = []
    ticker = []

    while i <= 21:
        try:
            elem.append(browser.find_element_by_css_selector('tr.table-dark-row-cp:nth-child('+ str(i)+') > td:nth-child(3) > a:nth-child(1)'))
        except Exception as e:
            pass
        try:
            elem.append(browser.find_element_by_css_selector('tr.table-light-row-cp:nth-child('+ str(i)+') > td:nth-child(3) > a:nth-child(1)'))
        except Exception as e:
            pass
        try:
            ticker.append(browser.find_element_by_css_selector('tr.table-dark-row-cp:nth-child('+ str(i)+') > td:nth-child(2) > a:nth-child(1)'))
        except Exception as e:
            pass
        try:
            ticker.append(browser.find_element_by_css_selector('tr.table-light-row-cp:nth-child('+ str(i)+') > td:nth-child(2) > a:nth-child(1)'))
        except Exception as e:
            pass
        

        index = 'A' + str(i + k)
        tickerindex = 'B' + str(i + k)
        aktie_worksheet[index] = elem[i-2].text
        aktie_worksheet[tickerindex] = ticker[i-2].text
        i = i + 1

    k = k + 20

    aktie_workbook.save('Aktie.xlsx')




