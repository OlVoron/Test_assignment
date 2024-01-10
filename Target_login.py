import self
from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import helper as h


class Target_Chrome(unittest.TestCase):

    # launch the browser
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_target_sign_in_chrome(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify sign in button
        h.verify_sign_in_target(driver)

        # put credentials and Enter
        h.verify_user_login(driver)

    def tearDown(self):
        self.driver.quit()


class Target_Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_target_firefox(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify sign in button
        h.verify_sign_in_target(driver)

        # put credentials and Enter
        h.verify_user_login(driver)

    def tearDown(self):
        self.driver.quit()


class Target_Edge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_target_edge(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify sign in button
        h.verify_sign_in_target(driver)

        # put credentials and Enter
        h.verify_user_login(driver)

    def tearDown(self):
        self.driver.quit()
