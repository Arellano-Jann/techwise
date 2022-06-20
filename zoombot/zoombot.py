import time
import config
from selenium import webdriver # https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By


# Configures the time set up for hours and minutes
# local_time = time.localtime()
# while local_time[4] != config.minute:
#     time.sleep(1) # sleeps for 1 second until specified minute
#     local_time = time.localtime()
# while local_time[3] != config.hour:
#     time.sleep(60*60) # sleeps for 1 hour until specified hour
#     local_time = time.localtime()
    

# Opens Firefox and the meeting link at a specified time
# print(time.localtime())
# print(local_time)
opts = FirefoxOptions() # headless option
opts.add_argument("--headless") # we run headless because it wont run in wsl without this because of that lack of display. you can inspect this more by going to the geckodriver.log 
driver = webdriver.Firefox(options=opts)
# while True:
#     if config.days.count(local_time[6]) > 0: ## tf does this do again?
#         break
#     else:
#         time.sleep(60*60*24) # sleeps for 1 day
driver.get(config.meeting_link)
print("Launched meeting link:", config.meeting_link)
time.sleep(5)

# Logs In to the techwise page
if "TechWise: Go Beyond Yourself" in driver.page_source:
    print("Logging into TechWise...")
    login = driver.find_element(By.ID, "login-email")
    login.send_keys(config.user_id)
    print("Entered email")
    password = driver.find_element(By.ID, "login-password")
    password.send_keys(config.password)
    print("Entered password")
    for x in range(2):  # Entering after login # why 2? idk
        login.send_keys(Keys.RETURN)
    print("Waiting for join page to load...")
    time.sleep(20) # waits for login

# Joins From Browser
# ctrl r and tab 9 times
# # # driver.get(driver.current_url) # binds driver to the current url
# # # time.sleep(5) # sleeps to give time to binding
# # # driver.refresh() # refreshes page
# # # print("Refreshing page")
# # # for x in range(9): # bugs here
# # #     driver.send_keys(Keys.TAB) # navigates to join from browser
# # # driver.click()

# x path method
# browser_join = driver.find_element_by_xpath("//*[ text() = 'Join from Your Browser']")# finds the join from your browser button

# # how does this work
# # browser_join = driver.find_element_by_class_name("pUmU_FLW")
# # for x in range(4):  # Entering after login
# #     login.send_keys(Keys.TAB)
# # browser_join.send_keys(Keys.RETURN)

# # # # Link Text Method to join from browser
browser_join = driver.find_element(By.LINK_TEXT, "Join from Your Browser")
browser_join.send_keys(Keys.RETURN)
print('Joined from browser and loading in...')
time.sleep(10)


# Checks if name is valid
name_box = driver.find_element(By.ID, "inputname")
if name_box.get_attribute('value') == '':
    name_box.send_keys(config.nameTag)
    print('Name inputted as:', config.nameTag)
else:
    print("Name in box is:", name_box.get_attribute('value'))

# Clicks Join on the name screen
join_button = driver.find_element(By.ID, "joinBtn")
join_button.click()
print("Clicked the join button on the name screen")



# # Joins audio
# # audio_button = driver.find_element(By.CLASS_NAME, "footer-button-base__button ax-outline join-audio-container__btn")
# # audio_button = driver.locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "foot-bar"})
# audio_button = driver.find_element(By.CLASS_NAME, "footer-button-base__img-layer")
# audio_button.send_keys(Keys.RETURN)
# print("Joined audio")



# check here if meeting not started or waiting room
# this is not searching for text "the meeting has not started" because it's in the source for the video chat
count = 0
while not driver.find_element(By.ID, "multi-view-video").is_displayed() and count < 100: # checks for video display
    print("Sleeping for 5. Waiting for meeting to start...")
    time.sleep(5)
    count += 1


# Exits meeting
current_time = time.monotonic()
print("Current time is:", current_time)
print("Sleeping for:", config.time_in_meeting)
time.sleep(config.time_in_meeting)
while not ( (current_time+config.time_in_meeting) < (time.monotonic()-10) ): # checks if current time (right side) is more than the scheduled time in meeting
    print("Current time is:", time.monotonic(), "and sleeping for 20 sec...")
    time.sleep(20) # waits until top is finished
print("Current time is:", time.monotonic(), "and exiting meeting now...")
driver.quit() # quits all web browsers
print("Successfully exited the meeting. The Zoom user will ghost for 3 minutes.")




# # # Function calling
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