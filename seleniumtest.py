from selenium import webdriver


browser = webdriver.Firefox()

browser.get('http://www.boerse.de/historische-kurse/wertpapier/TH0268010Z11_jahr,2017#jahr')
i = 1
elem = []


while i <= 51:
    try:
        elem.append(browser.find_element_by_css_selector('table.table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5)').text)

    except Exception as e:
        pass
