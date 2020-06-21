from selenium import webdriver
import time

path = "/Users/melisaborekcioglu/Downloads/chromedriver"
browser = webdriver.Chrome(path)

browser.get("https://www.zomato.com/tr/istanbul/%C3%BCsk%C3%BCdar-restoranlar%C4%B1")
#browser.get("https://www.zomato.com/tr/istanbul/filizler-köftecisi-1-salacak-istanbul")
print("melisa")

data = {}
restourants = []
restourant = {}
resturls = []


def browserstart():
    try:
        rests = browser.find_elements_by_class_name('fontsize0')
        for restulr in rests:
            print(restulr.get_attribute('href'))
            resturls.append(restulr.get_attribute('href'))
    except:
        print('restoran linkleri alınamadı')


def getDetails():
    try:
        for url in resturls:
            browser.get(url)
            getName()
            #getCategory()
            #getCommend()
            #openingTime()
    except:
        print('link kalmadı veya hatalı')
        browser.get("https://www.zomato.com/tr/istanbul/%C3%BCsk%C3%BCdar-restoranlar%C4%B1")

def getName():
    names = browser.find_elements_by_tag_name('h1')
    for name in names:
        print(name.text)

# zomato sol menüdeki restoran tipleri çekilemedi!! geçici olarak manuel dolduruldu, düzeltileccek
def getCategory():
    categoryType = ['Lüks','Cafe','Lokanta','Yemek','Meyhane','Pastane','Tatlıcı','YeveKalk','Fırın','Ocakbaşı']
    for type in categoryType:
        try:
            category = browser.find_element_by_link_text(type)
            if (category.text == type):
                print(category.text)
                break
        except:
            if(type == 'Ocakbaşı'):
                break


def getCategori():
    categories = browser.find_elements_by_css_selector('cursor-pointer')
    for categori in categories:
        print(categori.text)
        browser.execute_script(categori)
'''
def getMode():
    mode = browser.find_elements_by_xpath('//*[@id="orig-search-list"]/div[3]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[1]/a[1]')
    for mod in mode:
        print(mod.text)
'''

def getComment():
    comment = browser.find_element_by_class_name("gcPmsM")
    print(comment.text)

def getPoint():
    point = browser.find_element_by_class_name('bObnWx')
    print(point)


def allRestoranType():
    allTypes = browser.find_elements_by_class_name('couisin')
    for type in allTypes:
        print(type)

def openingTime():
    time = browser.find_element_by_class_name('cxBEnh')
    print(time.text)

getMode()
#getCategori()
#browserstart()
#getDetails()
#getCategory()
#allRestoranType()



