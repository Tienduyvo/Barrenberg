from selenium import webdriver
import time
import openpyxl



aktie_workbook = openpyxl.load_workbook('Aktie.xlsx')

aktie_worksheet = aktie_workbook.get_sheet_by_name('Tabelle1')


browser = webdriver.Firefox()

j = 2
k = 1141

#while j <= 14:
browser.get('http://www.finanzen.net/aktien/aktien_suche.asp?inland=0&inbillanz=0&inbillanzjahr=2016&inbillanzgrkl=2&stsonstigzahl=10000&inbranche=0&inindex=0&infunndagrkl1=2&infunndagrkl2=2&infundamental1=0&infundamentaljahr1=2016&infundamental2=0&infundamentaljahr2=2016&insonstige=1&insonstigegrkl=2')
             
i = 1
elem = []


while i <= 51:
    try:
        elem.append(browser.find_element_by_css_selector('table.table:nth-child(3) > tbody:nth-child(3) > tr:nth-child('+ str(i)+') > td:nth-child(1) > a:nth-child(1)').get_attribute('href'))
    except Exception as e:
        pass

    index = 'A' + str(i + k)
    aktie_worksheet[index] = elem[i-2]
    i = i + 1

#    j = j + 1 
#    k = k + 50


    aktie_workbook.save('Aktie.xlsx')