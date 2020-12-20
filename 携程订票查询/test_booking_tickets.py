import time

from functions import css, xpath, return_driver
from search_tickets import search_tickets

search_tickets('上海', '杭州', 1)
driver = return_driver()
time.sleep(2)
xpath('//div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a').click()
time.sleep(2)
css("input[class='input-name']").send_keys('张晓')
