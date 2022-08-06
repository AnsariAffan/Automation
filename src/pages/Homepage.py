from selenium.webdriver.common.by import By

from src.Config.config import TestData
from src.pages.Utilities import Utilities


class HomePage(Utilities):

    home = ()
    about = (By.XPATH,"//li[@id='menu-item-25308']/a[.='About']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.baseURL)

    def click_on_about_page(self):
        return  self.click(self.about)

    def get_element_text(self):
        return  self.getElementText(self.about)

