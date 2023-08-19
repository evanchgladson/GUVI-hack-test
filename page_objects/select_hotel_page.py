from selenium.webdriver.common.by import By

class SelectHotelPage:
    def __init__(self, driver):
        self.driver = driver

    def select_hotel(self):
        self.driver.find_element(By.ID, "radiobutton_0").click()
        self.driver.find_element(By.NAME, "continue").click()
