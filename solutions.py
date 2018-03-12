# from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common import exceptions as ex
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
import time
from smtplib import SMTP_SSL
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import formatdate

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

# TRASH START HERE

try:
    WebDriverWait(driver, DELAY).until(ec.presence_of_element_located((
        By.XPATH,
        '//*[contains(text(), "%s")]' % 'Подать жалобу')))
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[contains(text(), "%s")]' % SUB_SET)
    print("OLOLO")

except ex.TimeoutException:
    print("TIME OUT")
except ex.NoSuchElementException:
    print("NO FIND")
finally:
    print("continue workaround")

# workaround
try:
    driver.get('https://www.cbr.ru/Reception/Message/Register?messageType=Gratitude')
    WebDriverWait(driver, DELAY).until(ec.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    lst = driver.find_elements(By.TAG_NAME, 'textarea')
    for elem in lst:
        if elem.get_attribute('id') == 'MessageBody':
            elem.send_keys("thanks for watching")
            break

    lst = driver.find_elements(By.TAG_NAME, 'input')
    for elem in lst:
        if elem.get_attribute('type') == 'checkbox':
            elem.click()
            break
    driver.get_screenshot_as_file('one.png')
except ex.TimeoutException:
    print('ERROR')
    driver.quit()
    exit(1)
except ex.NoSuchElementException:
    print('NoSuchElementException')
    driver.quit()
    exit(1)

file = "one.png"
basename = os.path.basename(file)
address = "onpython@yandex.ru"

# Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(file, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)

# Compose message
msg = MIMEMultipart()
msg['From'] = address
msg['To'] = address
msg.attach(part)

# Send mail
smtp = SMTP_SSL()
smtp.connect('smtp.yandex.ru')
smtp.login(address, 'qwertyasdfzxcv')
smtp.sendmail(address, address, msg.as_string())
smtp.quit()

input()
driver.quit()
