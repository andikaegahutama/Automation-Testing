import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

partnerandom = ["react-select-5-option-0", "react-select-5-option-1", "react-select-5-option-2", "react-select-5-option-3", "react-select-5-option-4", "react-select-5-option-5", "react-select-5-option-6", "react-select-5-option-7", "react-select-5-option-8", "react-select-5-option-9"]
partnerrandomid = random.choice(partnerandom)

customergeneralrandom = ["react-select-2-option-0", "react-select-2-option-1", "react-select-2-option-2", "react-select-2-option-3", "react-select-2-option-4", "react-select-2-option-5", "react-select-2-option-6", "react-select-2-option-7", "react-select-2-option-8", "react-select-2-option-9"]
customergeneralrandomid = random.choice(customergeneralrandom)

payment = ["react-select-6-option-0", "react-select-6-option-1"]
paymentid = random.choice(payment)

customerrecepient = ["react-select-7-option-0", "react-select-7-option-1", "react-select-7-option-2", "react-select-7-option-3", "react-select-7-option-4", "react-select-7-option-5", "react-select-7-option-6", "react-select-7-option-7", "react-select-7-option-8", "react-select-7-option-9"]
customerrecepientid = random.choice(customerrecepient)

ordertype = ["react-select-8-option-0", "react-select-8-option-1"]
ordertypeid = random.choice(ordertype)

shippingcost = ["10000", "20000", "30000", "40000", "50000", "60000", "70000", "80000", "90000", "100000"]
shippingcostid = random.choice(shippingcost)

servicecost = ["10000", "20000", "30000", "40000", "50000", "60000", "70000", "80000", "90000", "100000"]
servicecostid = random.choice(servicecost)

servicefee = ["1000", "2000", "3000", "4000", "5000", "6000", "7000", "8000", "9000", "10000"]
servicefeeid = random.choice(servicefee)


class CreateTransaction:
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

    def transaction_menu(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/ul/li[2]/div").click()

    def create_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/div/button[1]").click()

    def customer_general(self):
        self.driver.find_element(By.ID, "react-select-2-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, customergeneralrandomid).click()

    def pickup_general(self):
        # self.driver.find_element(By.ID, "general_info_pick_of_location").send_keys("Purbalingga")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/div/form/div[1]/div[2]/div[2]/fieldset/input").send_keys("Purbalingga")

    def addorder_general(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/div/form/div[2]/button").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def set_general(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/button").click()

    def typeservice_general(self):
        self.driver.find_element(By.ID, "react-select-4-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "react-select-4-option-1").click()

    def submit_general(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/button").click()

    def partner_pesanan(self):
        self.driver.find_element(By.ID, "react-select-5-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, partnerrandomid).click()

    def pickup_pesanan(self):
        self.driver.find_element(By.ID, "pick_of_location").send_keys("Purbalingga")

    def distance_pesanan(self):
        self.driver.find_element(By.ID, "total_distance").clear()
        self.driver.find_element(By.ID, "total_distance").send_keys("10")

    def shippingcost_pesanan(self):
        self.driver.find_element(By.ID, "shipping_cost").send_keys(shippingcostid)

    def servicecost_pesanan(self):
        self.driver.find_element(By.ID, "service_cost").send_keys(servicecostid)

    def servicefee_pesanan(self):
        self.driver.find_element(By.ID, "service_fee").send_keys(servicefeeid)

    def payment_pesanan(self):
        self.driver.find_element(By.ID, "react-select-6-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, paymentid).click()

    def addrecepient_pesanan(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[2]/button").click()

    def customer_recepient(self):
        self.driver.find_element(By.ID, "react-select-7-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, customerrecepientid).click()

    def dropoff_recepient(self):
        self.driver.find_element(By.ID, "recipients.0.drop_of_location").send_keys("Purwokerto")

    def ordertype_recepient(self):
        self.driver.find_element(By.ID, "react-select-8-input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, ordertypeid).click()

    def ordername_recepient(self):
        self.driver.find_element(By.ID, "recipients.0.package_name").send_keys("Sosis")

    def quantity_recepient(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[2]/div[5]/div/div[2]/fieldset/input").send_keys("2")

    def add_recepient(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[3]/div/div[2]/button").click()

    def add_pesanan(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[2]/div[3]/div/div[2]/button").click()

    def submit_order(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[3]/div/div[3]/button").click()
        time.sleep(5)
