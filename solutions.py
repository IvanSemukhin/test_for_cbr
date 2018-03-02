from selenium import webdriver
from selenium.common import exceptions as ex
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
import os
import time


# cross
EXEC_PATH = ''
if os.name == 'nt':
    EXEC_PATH = 'chromedriver.exe'
elif os.name == 'posix':
    EXEC_PATH = './chromedriver'
else:
    print("Add OS condition for: (" + os.name + ")")
    exit(1)

# const
DELAY = 10
FIELD_NAME = 'q'
TAG_NAME = 'a'
SEARCH_ENGINE = 'https://www.google.ru/'
WHAT_SEARCH = 'Центральный банк РФ'  # в задании была опечатка(“Цетральный банк РФ”)
TRUE_LINK = 'https://www.cbr.ru/'
HREF = "href"
RECEPTION = 'Интернет-приемная'
SUB_SET = 'Написать благодарность'

# init driver
driver = webdriver.Chrome(executable_path=EXEC_PATH)
driver.maximize_window()
driver.implicitly_wait(DELAY)
driver.get(SEARCH_ENGINE)

# search in google
try:
    WebDriverWait(driver, DELAY).until(ec.element_to_be_clickable((By.NAME, FIELD_NAME)))
except ex.TimeoutException:
    print('No find field by name: ', FIELD_NAME)
    driver.quit()
    exit(1)
el = driver.find_element(By.NAME, FIELD_NAME)
el.send_keys(WHAT_SEARCH)
el.send_keys(Keys.RETURN)

links = driver.find_elements(By.TAG_NAME, TAG_NAME)
true_link = None
for elem in links:  # test true link
    if elem.get_attribute(HREF) == TRUE_LINK:
        true_link = elem
        break
if true_link is None:
    print('In first page ' + TRUE_LINK + ' NOT FOUND!')
true_link.click()   # переход на страницу ЦБ

try:
    WebDriverWait(driver, DELAY).until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, RECEPTION)))
    driver.find_element(By.PARTIAL_LINK_TEXT, RECEPTION).click()    # переход в инет-приёмную
except ex.TimeoutException:
    print('No load element: ', RECEPTION)
    driver.quit()
    exit(1)
except ex.NoSuchElementException:
    print('No find field by name: ', RECEPTION)
    driver.quit()
    exit(1)

# треш начинается отсюда
try:
    time.sleep(5)
    # WebDriverWait(driver, DELAY).until(ec.presence_of_element_located((By.XPATH, ".//*[@class='content_cols content_cols_2 no_visited reception_type_container']")))
    # WebDriverWait(driver, DELAY).until(ec.presence_of_element_located((By.XPATH, "//a[text() = 'Подать Жалобу']")))
    # WebDriverWait(driver, DELAY).until(ec.visibility_of_all_elements_located((By.TAG_NAME, 'link')))
    # lst = driver.find_elements_by_xpath(".//*[@class='content_col button']/..")
    # lst = driver.find_elements_by_xpath("//a[text() = 'Написать благодарность']")
    # lst = driver.find_elements_by_xpath(".//*[@id='content']")
    # lst = driver.find_elements_by_xpath("//a[text() = 'Подать жалобу']")
    # lst = driver.find_elements(By.XPATH, ".//*[@href='/Reception/Message/Register?messageType=Gratitude']/..")
    # lst = driver.find_elements(By.TAG_NAME, 'a')
    # lst = driver.find_elements(By.XPATH, ".//*[@class='content']")
    lst = driver.find_elements(By.TAG_NAME, 'frame')
    print("OLOLO", lst)
    for elem in lst:
        print("text:", elem.text)
        if elem.text == 'Написать благодарность':
            input()
except ex.TimeoutException:
    print('ERROR')
    driver.quit()
    exit(1)
input()
driver.quit()

# <h2>Написать благодарность</h2>

# <a href="/Reception/Message/Register?messageType=Gratitude" class="reception_type">
#       <h2>Написать благодарность</h2>
#     </a>
# //*[@id="content"]
# driver.findElement(By.xpath(".//*[text()='Первая ссылка']/.."));
# <span class="r5">5</span><a href="http://google.com">Google</a>
# span[@class ='r5']
# /html/body/div/div[1]/div[3]/div/div[2]/div[1]/div[3]/a
# <div class="content_col button">
#     <a href="/Reception/Message/Register?messageType=Gratitude" class="reception_type">
#       <h2>Написать благодарность</h2>
#     </a>
#   </div>
# content_cols content_cols_2 no_visited reception_type_container
