import time

import names
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

random_num = "".join(random.choices(numbers, k=11))
phone = "62" + random_num

random_part = "".join(random.choices(letters, k=7))
email = random_part + "@gmail.com"


class CreateCustomer:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def apply_wait(self):
        self.driver.set_page_load_timeout(3)

    def login_menu(self):
        self.driver.get("https://omgspi-uat.vitastore.id/#/login")
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def fill_username(self):
        username = self.driver.find_element(By.ID, "email")
        username.send_keys("{Email}")

    def fill_password(self):
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("{Password}")

    def submit_login(self):
        login = self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form/button")
        login.click()

    def customer_menu(self):
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.fullscreen_window()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/ul/li[4]").click()

    def create_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/div/button[1]").click()

    def create_firstname(self):
        self.driver.find_element(By.ID, "firstName").send_keys(names.get_first_name(gender="Male"))

    def create_lastname(self):
        self.driver.find_element(By.ID, "lastName").send_keys(names.get_last_name())

    def create_phone(self):
        self.driver.find_element(By.ID, "phone").send_keys(phone)

    def create_email(self):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def create_submit(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/form/div[2]/div[2]/button").click()
        time.sleep(5)
