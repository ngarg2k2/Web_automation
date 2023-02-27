import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# function to fill out the form for a single user


def fill_form(name, number, code):
    # create a new instance of the Firefox driver
    driver = webdriver.Chrome()

    # navigate to the web page with the form you want to fill out
    driver.get(
        'https://docs.google.com/forms/d/e/1FAIpQLScPT85DJ9FyhD_-mWmpy1UfvijkPudWoj1iho3jjJ1wk3y7Pw/viewform')

    # find the input fields for the form and enter data into them
    Name = driver.find_element(
        'xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Name.send_keys(name)

    Roll_NO = driver.find_element(
        'xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Roll_NO.send_keys(number)

    Code = driver.find_element(
        'xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Code.send_keys(code)

    # submit the form
    Submit = driver.find_element(
        'xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Submit.click()

    # close the browser window
    driver.quit()


# create a list of users with their information
codes = "multi"
users = [
    {"name": "Nipun1", "number": "102003674", "code": codes},
    {"name": "Nipun2", "number": "102003670", "code": codes},
    {"name": "Nipun3", "number": "102003689", "code": codes},
    {"name": "Nipun4", "number": "102003697", "code": codes}
]

# create a list of threads, one for each user
threads = []
for user in users:
    thread = threading.Thread(target=fill_form, args=(
        user["name"], user["number"], user["code"]))
    threads.append(thread)

# start all threads
for thread in threads:
    thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()
