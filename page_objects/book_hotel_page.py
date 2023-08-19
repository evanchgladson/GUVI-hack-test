from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BookHotelPage:
    def __init__(self, driver):
        self.driver = driver

    def book_hotel(self, first_name, last_name, address, cc_num, cc_type, exp_month, exp_year, cvv):
        self.driver.find_element(By.NAME, "first_name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last_name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "cc_num").send_keys(cc_num)

        card = Select(self.driver.find_element(By.NAME, "cc_type"))
        card.select_by_visible_text(cc_type)

        exp_mon = Select(self.driver.find_element(By.NAME, "cc_exp_month"))
        exp_mon.select_by_visible_text(exp_month)

        expiry_year = Select(self.driver.find_element(By.NAME, "cc_exp_year"))
        expiry_year.select_by_visible_text(exp_year)

        self.driver.find_element(By.NAME, "cc_cvv").send_keys(cvv)

        self.driver.find_element(By.NAME, "book_now").click()
