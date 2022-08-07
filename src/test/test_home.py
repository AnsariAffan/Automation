from selenium import webdriver

from src.pages.Homepage import HomePage
from src.test.test_Base import Test_Base
from selenium.webdriver.chrome.service import Service

class Test_Home(Test_Base):
    abc = Service("./src/test/chromedriver.exe")
    driver = webdriver.Chrome(service=abc)

    def test_click_On_Aboutpage(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_about_page()
        assert "pass","Fails"

    def test_click_On_allcourses(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_allcourses()
        assert "pass", "Fails"





