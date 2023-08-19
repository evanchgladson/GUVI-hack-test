import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page_objects.login_page import LoginPage
from page_objects.search_hotel_page import SearchHotelPage
from page_objects.select_hotel_page import SelectHotelPage
from page_objects.book_hotel_page import BookHotelPage


class TestBooking:
    def setup(self):
        serv_obj = Service("C:\\chrome_driver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)

    def test_Booking(self):
        login_page = LoginPage(self.driver)
        login_page.login("evanchgladson", "Password@123")

        search_page = SearchHotelPage(self.driver)
        search_page.search_hotel("New York", 2, 1, "2", "23/08/2023", "24/08/2023", "2", 1)

        select_page = SelectHotelPage(self.driver)
        select_page.select_hotel()

        book_page = BookHotelPage(self.driver)
        book_page.book_hotel("Evanchalin", "C K", "KTC Nagar", "1234567890123456", "VISA", "December", "2024", "345")

    def teardown_method(self):
        self.driver.quit()
