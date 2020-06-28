import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

info = list()

with open("details.txt") as file:
    lines = file.readlines()
    for line in lines:
        info.append(line.strip(" \n"))

details = {
    "firstName" : info[0],
    "lastName" : info[1],
    "email" : info[2],
    "phone" : info[3],
    "college" : info[4],
    "resume" : info[5],
    "linkedin" : info[6],
    "github" : info[7],
    "facebook" : info[8],
    "gradMonth" : info[9],
    "gradYear" : info[10],
    "location" : info[11]
}

def greenhouse(driver):
    # basic info
    driver.find_element_by_id('first_name').send_keys(details['firstName'])
    driver.find_element_by_id('last_name').send_keys(details['lastName'])
    driver.find_element_by_id('email').send_keys(details['email'])
    driver.find_element_by_id('phone').send_keys(details['phone'])

    # Resume
    # driver.find_element_by_css_selector("[data-source='attach']").click()
    # time.sleep(5)

    # Location
    try:
        driver.find_element_by_id('job_application_location').send_keys(details['location'])
    except NoSuchElementException:
        pass

    # LinkedIn
    try:
        # Upper case "I"
        driver.find_element_by_xpath("//label[contains(.,'LinkedIn')]").send_keys(details['linkedin'])
    except NoSuchElementException:
        try:
            #Lower case "i"
            driver.find_element_by_xpath("//label[contains(.,'Linkedin URL')]").send_keys(details['linkedin'])
        except NoSuchElementException:
            pass

    # Graduation Year
    try:
        driver.find_element_by_xpath("//select/option[text()='2022']").click()
    except NoSuchElementException:
        pass

    # University
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Oberlin')]").click()
    except NoSuchElementException:
        pass

    # Github
    try:
        driver.find_element_by_xpath("//label[contains(.,'Github')]").send_keys(details['github'])
    except NoSuchElementException:
        pass

    # Degree
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    # Major
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    except NoSuchElementException:
        pass

    # Gender
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Male')]").click()
    except NoSuchElementException:
        pass

    # Race
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'No')]").click()
        time.sleep(0.5)
    except NoSuchElementException:
        pass

    # Specific Race
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Asian')]").click()
    except NoSuchElementException:
        pass

    # Veteran Status
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'I am not a protected veteran')]").click()
    except NoSuchElementException:
        pass

    # Disability Status
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'No, I don't have a disability')]").click()
    except NoSuchElementException:
        pass

def lever(driver):

    #You need to click "Apply" depending on the link used
    #driver.find_element_by_class_name('template-btn-submit').click()

    # basic info
    firstName = details['firstName']
    lastName = details['lastName']
    fullName = firstName + ' ' + lastName  # f string didn't work here, but that's the ideal thing to do
    driver.find_element_by_name('name').send_keys(fullName)
    driver.find_element_by_name('email').send_keys(details['email'])
    driver.find_element_by_name('phone').send_keys(details['phone'])
    driver.find_element_by_name('org').send_keys(details['college'])

    # LinkedIn
    driver.find_element_by_name('urls[LinkedIn]').send_keys(details['linkedin'])

    #Github
    try: # try both versions
        driver.find_element_by_name('urls[Github]').send_keys(details['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name('urls[GitHub]').send_keys(details['github'])
        except NoSuchElementException:
            pass


    # add College
    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(details['college']) # find university in dropdown
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # add how you found out about the company
    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath("//select/option[text()='Glassdoor']").click()
    except NoSuchElementException:
        pass

    # Resume
    driver.find_element_by_name('resume').send_keys(os.getcwd()+"/Akshat_Phumbhra_Resume.pdf")
    time.sleep(1)

def general(driver):
    driver.find_element_by_id('first_name').send_keys(details['firstName'])
    driver.find_element_by_id('last_name').send_keys(details['lastName'])
    driver.find_element_by_id('email').send_keys(details['email'])
    driver.find_element_by_id('phone').send_keys(details['phone'])

if __name__ == '__main__':
    urls = list()

    with open("urls.txt") as file:
        lines = file.readlines()
        for url in lines:
            urls.append(url.strip(" \n"))
        total = len(urls)

    # Add installation location of chromedriver
    # driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver.exe')
    driver = webdriver.Firefox()
    google = "https://www.google.com/"
    driver.get(google)

    for i, url in enumerate(urls):
        tab = f'tab{i}'
        driver.execute_script(f"window.open('about:blank', '{tab}');")
        driver.switch_to.window(tab)
        if 'greenhouse' in url:
            driver.get(url)

            try:
                greenhouse(driver)
                print(f'Success for {url}')

            except Exception:
                continue

        elif 'lever' in url:
            driver.get(url)

            try:
                lever(driver)
                print(f'Success for {url}')

            except Exception:
                continue

        else:
            driver.get(url)
            try:
                general(driver)
                print(f'Success for {url}')

            except Exception:
                continue

        time.sleep(0.5)
