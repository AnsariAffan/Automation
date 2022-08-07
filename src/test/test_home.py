import pytest
from selenium import webdriver

from src.pages.Homepage import HomePage
from src.pages.Utilities import Utilities
from src.test.test_Base import Test_Base
from selenium.webdriver.chrome.service import Service

class Test_Home(Test_Base):
    abc = Service("./src/test/chromedriver.exe")
    driver = webdriver.Chrome(service=abc)

    @pytest.fixture()
    def setup(self):
        self.homepage = HomePage(self.driver)

    @pytest.mark.test1
    def test_click_On_Aboutpage(self,setup):
        self.homepage.click_on_about_page()
        assert self.homepage.get_element_text(), "pass hogaya"

    @pytest.mark.test2
    def test_click_On_allcourses(self,setup):
        self.homepage.click_on_allcourses()

    @pytest.mark.test3
    def test_close_browser(self,setup):
          self.homepage.closebrowser()





