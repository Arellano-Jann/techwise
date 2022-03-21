import time
import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Configures the time set up for hours and minutes
local_time = time.localtime()
while local_time[4] != config.minute:
	time.sleep(1) # sleeps for 1 second until specified minute
while local_time[3] != config.hour:
	time.sleep(60*60) # sleeps for 1 hour until specified hour

# Opens Chrome and the meeting link at a specified time
driver = webdriver.Chrome()
while True:
    if config.days.count(local_time[6]) > 0:
        break
    else:
        time.sleep(60*60*24) # sleeps for 1 day
driver.get("https://google.com")
# driver.get(config.meeting_link)

# Logs In
login = driver.find_element_by_id("login-email")
# for x in range(3):#tabs in login
# 	login.send_keys(Keys.TAB)
for x in range(2):  # DOWN ARROWS
    login.send_keys(Keys.ARROW_DOWN)
    login.send_keys(Keys.ARROW_DOWN)
for x in range(2):  # Entering after login
    login.send_keys(Keys.RETURN)
time.sleep(20)

# Joins From Browser
# browser_join = driver.find_element_by_xpath("//*[ text() = 'Join from Your Browser']")# finds the join from your browser button
browser_join = driver.find_element_by_class_name("pUmU_FLW")
for x in range(4):  # Entering after login
	login.send_keys(Keys.TAB)
browser_join.send_keys(Keys.RETURN)

# Clicks Join
join_button = driver.find_element_by_id("joinBtn")
join_button.click()

# Joins audio
audio_button = driver.find_element_by_id("zm-btn join-audio-by-voip__join-btn zm-btn--primary zm-btn__outline--white zm-btn--lg")
audio_button.click()

# Exits meeting
current_time = time.monotonic()
time.sleep(config.time_in_meeting)
while True:
	if (current_time+config.time_in_meeting) < (time.monotonic()-10):
		driver.quit()
		print("Exited meeting")
		break
	else:
		time.sleep(20)



# def open_browser():
#     driver = webdriver.Chrome()
#     driver.get("https://google.com")
	
#     search = driver.find_element_by_id("login-email")
#     search.send_keys(Keys.ARROW_DOWN)
#     search.send_keys(Keys.ARROW_DOWN)
#     search.send_keys(Keys.RETURN)
#     time.sleep(20)
	
#     return driver
	
# def login(driver, link: str):
#     #3 Tabs
#     search = driver.find_element_by_id()
	

# def join(link: str, ):
#     #