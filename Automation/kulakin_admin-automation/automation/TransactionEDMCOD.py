import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

random_product = ["Nutriflakes", "Vitameal", "Zymuno", "Freshmag", "Gizidat", "Weight Herba"]
random_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random_customer = ["6287654321112", "6285612736171", "6287654314512", "628765167289", "6281218323", "62812183223",
                   "628121832213", "62812181322413", "62812183132213", "6281181322413", "6281181322213", "628118122213",
                   "62811812213", "628118121213", "62811812121", "628118121231", "62811812131", "6281181217131",
                   "628118127131", "6281181227131", "628118227131", "6281182271031", "6281182271231", "6281182271",
                   "62811822711", "62811822713", "6281182273", "628118227391", "62811827391", "6281718190191",
                   "628171819011", "6282181921", "6282187882", "6282129911122", "6282129911", "6282129911211",
                   "62821299111", "628212991211", "62823191211", "627918112911", "627918191911", "628162881264",
                   "628162881864", "628162881726", "6286142318721", "6287615241312", "628652416212", "6281229613471",
                   "6281229613471", "62861527318273", "628516283112", "12312423123", "628761728129", "6281253172112",
                   "6281380405662", "6287654345671", "6287654345678", "628612673812", "6286125831723", "62728162501",
                   "6287654328987", "628981628712", "629876543456", "6286543", "62129831092", "62812871328",
                   "62812931829123", "6285179512101"]
random_revenue = ["AWA", "OFC", "INF", "DWA"]
rndm_prdct = random.choice(random_product)
rndm_nmbr = random.choice(random_numbers)
rndm_prdct2 = random.choice(random_product)
rndm_nmbr2 = random.choice(random_numbers)
rndm_cstmr = random.choice(random_customer)
rndm_rvne = random.choice(random_revenue)


class CreateTransactionEDMCOD:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def apply_wait(self):
        self.driver.set_page_load_timeout(3)

    def menu(self):
        self.driver.get("https://erdigo-admin.zcode.id/#/auth/login")
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def fill_phone(self):
        phone = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/form/div[1]/input")
        phone.send_keys("{Number}")

    def fill_pin(self):
        pin = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/form/div[2]/input")
        pin.send_keys("{Password}")

    def button_login(self):
        login = self.driver.find_element(By.XPATH,
                                         "/html/body/div/div[1]/div/div/div/div/div/div/form/div[3]/div/button")
        login.click()
        time.sleep(5)

    def transaction_menu(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/ul/li[2]/a").click()

    def produk_edm(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/ul/li[2]/ul/li[2]/a").click()

    def create_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div/main/div/div/div[1]/header/div/div[2]/div/div/button[1]").click()

    def paste_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div/main/div/div/div[1]/footer/button[2]").click()

    def textarea_create(self):
        myformat = self.driver.find_element(By.ID, "pasteTemplate")
        myformat.clear()
        # Affiliate: Affiliate: 62872165371
        # Whatapp: {rndm_cstmr}
        myformat.send_keys(f"""Affiliate: 6285179512101

Whatapp:  629876543456

Pesanan: {rndm_nmbr} {rndm_prdct} + {rndm_nmbr2} {rndm_prdct2}
Jenis Pembayaran: COD
notes: notes

Revenue Stream:{rndm_rvne}""")

    time.sleep(1)

    def add_template(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div/main/div/div/div[2]/div[1]/div/div/footer/button[2]").click()
        time.sleep(1)

    def sure_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div/main/div/div/div[3]/div[1]/div/div/div/div[7]/div/div/div[2]/button").click()

    def simpan_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div/main/div/div/div[1]/footer/button[3]").click()
