import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


details = {
    "firstName" = ""
    "lastName" = ""
    "email" = ""
    "phone" = ""
    "college" = ""
    "resume" = ""
    "linkedin" = ""
    "github" = ""
    "facebook" = ""
    "gradMonth" = ""
    "gradYear" = ""
    "location" = ""
}

def greenhouse(driver):
    # basic info
    driver.find_element_by_id('first_name').send_keys(details['firstName'])
    driver.find_element_by_id('last_name').send_keys(details['lastName'])
    driver.find_element_by_id('email').send_keys(details['email'])
    driver.find_element_by_id('phone').send_keys(details['phone'])

    # Resume
    driver.find_element_by_css_selector("[data-source='attach']").click()
    time.sleep(5)

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
            driver.find_element_by_xpath("//label[contains(.,'Linkedin')]").send_keys(details['linkedin'])
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
        driver.find_element_by_xpath("//select/option[contains(.,'I am not')]").click()
    except NoSuchElementException:
        pass

    # Disability Status
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'No, I ')]").click()
    except NoSuchElementException:
        pass


if __name__ == '__main__':
    urls = list()
    success = 0
    fails = 0

    with open("urls.txt") as file:
        lines = file.readlines()
        for url in lines:
            urls.append(url.strip())
        total = len(urls)

    # Add installation location of chromedriver
    driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver.exe')

    for url in urls:

        if 'greenhouse' in url:
            driver.get(url)

            try:
                greenhouse(driver)
                print(f'Success for {url}')
                success += 1

            except Exception:
                fails += 1
                continue

        elif 'lever' in url:
            driver.get(url)

            try:
                lever(driver)
                print(f'Success for {url}')
                success += 1

            except Exception:
                fails += 1
                continue

        time.sleep(1)

    driver.close()
