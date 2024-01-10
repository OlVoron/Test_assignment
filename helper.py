from selenium.webdriver.common.by import By
import random
import requests
import time
import credentials as cr

# URL - home page
main_url = "https://www.target.com/"


def delay():  # Set random delay
    time.sleep(random.randint(1, 3))


def check_api_code(driver):  # Check API response code (200 correct)
    print("Target Url has", requests.get("https://www.target.com/").status_code, "as status Code")
    code = requests.get("https://www.target.com/").status_code
    if code == 200:
        print("API response code is OK")
    else:
        print("API response code is not 200", "Current code is:", code)


def verify_title_home_page(driver):  # Verify title of home page
    try:
        assert driver.title == "Target : Expect More. Pay Less."
        print("The driver title is correct: ", driver.title)
    except AssertionError:
        print("Title is different. Current Title is:", driver.title)


def verify_sign_in_target(driver):  # Verify sign in button
    try:
        driver.find_element(By.XPATH, "//span[contains(.,'Sign in')]").click()
        delay()
        driver.find_element(By.XPATH, "(//span[contains(.,'Sign in')])[2]").click()
        delay()
        driver.find_element(By.ID, "login")
        delay()
        print("Sign in button and window are verify")
    except AssertionError:
        print("Something wrong with button sign in")


def verify_user_login(driver):   # put credentials and Enter
    try:
        driver.find_element(By.ID, "username").click()
        driver.find_element(By.ID, "username").send_keys(cr.ue)
        delay()
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys(cr.up)
        delay()
        driver.find_element(By.ID, "login").click()
        delay()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Olga")
        print("Users account is correct!")      # assert displayed name
    except AssertionError:
        print("Users account is wrong")


