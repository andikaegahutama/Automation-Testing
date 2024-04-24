import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def apply_wait(self):
        self.driver.set_page_load_timeout(3)

    def menu(self):
        self.driver.get("https://reports.erhanesia.id/login")
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def email(self):
        fill_email = self.driver.find_element(By.ID, "email")
        fill_email.send_keys("{Email}")
        self.driver.implicitly_wait(10)

    def password(self):
        fill_password = self.driver.find_element(By.ID, "password")
        fill_password.send_keys("{Password}")

    def login_button(self):
        submit = self.driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/div[1]/div/div[2]/form/div[4]/button")
        submit.click()
        time.sleep(50000000)
