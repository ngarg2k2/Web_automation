from selenium import webdriver
import time

web = webdriver.Chrome()

# link for google form
web.get('https://docs.google.com/forms/d/e/1FAIpQLScPT85DJ9FyhD_-mWmpy1UfvijkPudWoj1iho3jjJ1wk3y7Pw/viewform')

time.sleep(2)

# inputs of google form
Name = "Nipun"
name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(Name)

Number = "102003674"
number = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
number.send_keys(Number)

Code="dscode"
code = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
code.send_keys(Code)

Submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
Submit.click()

# confirmation message
get_confirmation_div_text = web.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[3]')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Your response has been recorded."):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")
