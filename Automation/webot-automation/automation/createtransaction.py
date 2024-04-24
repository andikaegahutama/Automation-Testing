import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
random_product = ["gizidat", "etawaku", "ssk", "optimaxx", "freshmag", "weight herba", "deepol", "kapsul kutuk", "new briswa"]
random_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
rndm_prdct = random.choice(random_product)
rndm_nmbr = random.choice(random_numbers)


class CreateTransaction:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def apply_wait(self):
        self.driver.set_page_load_timeout(3)

    def login_menu(self):
        self.driver.get("https://webot-dev.vitastore.id/v2/auth/login")
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def fill_username(self):
        username = self.driver.find_element(By.ID, "auth_email")
        username.send_keys("{Email}")

    def fill_password(self):
        password = self.driver.find_element(By.ID, "auth_password")
        password.send_keys("{Password}")

    def submit_login(self):
        login = self.driver.find_element(By.ID, "auth_login")
        login.click()
        self.driver.implicitly_wait(3)

    def transaction_create(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[9]/div[3]/div").click()

    def textarea_create(self):
        myformat = self.driver.find_element(By.ID, "weborderCreateExtractInput")
        myformat.clear()
        myformat.send_keys(f"""Nama: Srihandayani
Whatapp: 085691170813
Kecamatan: secang
Kelurahan: donorejo
Kode Pos: 56595
RT: {rndm_nmbr}
RW: {rndm_nmbr}
Alamat: Jl. Poros KM.11 dsn. Pelangi Dua
    
Pesanan: {rndm_nmbr} {rndm_prdct}
Jenis Pembayaran: COD
Potongan Ongkir: 11.000
Biaya Admin: 0
    
Advertiser: FAKIH
Platform Adv: Tiktok
TIM: Parikesit
Notes: PROMO 20%""")
        self.driver.implicitly_wait(2)

    def ethix_edx(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[6]/div/div/div/div/div[2]/div[2]/label").click()

    def submit_textarea(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[6]/div/div/div/div/div[4]/button[2]").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.implicitly_wait(2)

    def warehouse_type(self):
        self.driver.find_element(By.ID, "react-select-5-input").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "react-select-5-option-1").click()

    def courir_type(self):
        self.driver.find_element(By.ID, "react-select-6-input").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "react-select-6-option-0").click()

    def review_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[3]/div/div[2]/div/button[2]").click()
        self.driver.implicitly_wait(5)

    def publish_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[3]/div/div[2]/div/button[2]").click()
        time.sleep(2)
