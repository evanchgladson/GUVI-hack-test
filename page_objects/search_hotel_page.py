from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver

    def search_hotel(self, location, hotel_index, room_type_index, room_nos_value, date_in, date_out, adult_count,
                     child_index):
        location_select = Select(self.driver.find_element(By.NAME, "location"))
        location_select.select_by_visible_text(location)

        hotel_select = Select(self.driver.find_element(By.ID, "hotels"))
        hotel_select.select_by_index(hotel_index)

        room_type_select = Select(self.driver.find_element(By.ID, "room_type"))
        room_type_select.select_by_index(room_type_index)

        room_nos_select = Select(self.driver.find_element(By.ID, "room_nos"))
        room_nos_select.select_by_value(room_nos_value)

        date_pick_in = self.driver.find_element(By.NAME, "datepick_in")
        date_pick_in.clear()
        date_pick_in.send_keys(date_in)

        date_pick_out = self.driver.find_element(By.NAME, "datepick_out")
        date_pick_out.clear()
        date_pick_out.send_keys(date_out)

        adult_select = Select(self.driver.find_element(By.ID, "adult_room"))
        adult_select.select_by_value(adult_count)

        child_select = Select(self.driver.find_element(By.ID, "child_room"))
        child_select.select_by_index(child_index)

        self.driver.find_element(By.XPATH, "//input[@value='Search']").click()
