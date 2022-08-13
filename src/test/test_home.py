import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By


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

#pages functions

    @pytest.mark.logo
    def test_click_On_logo(self, setup):
        self.homepage.click_on_logo()
        assert self.homepage.getTabeName() == "Home - Test Academy | Software Testing Institute in Nagpur", "page not found"
        assert self.homepage.is_logo_display() == True, "not clicked"

    @pytest.mark.home
    def test_click_On_HomePage(self,setup):
         self.homepage.click_on_home_page()
         assert self.homepage.get_homepage_text() =="Home","home page not found"
         assert self.homepage.getTabeName() == "Home - Test Academy | Software Testing Institute in Nagpur", "page not found"
         assert self.homepage.is_homepage_display() == True, "not clicked"

    @pytest.mark.about
    def test_click_On_Aboutpage(self,setup):
         self.homepage.click_on_about_page()
         assert self.homepage.get_aboutpage_text() =="About","About is not available faild"
         assert self.homepage.getTabeName() == "About - Test Academy", "page not found"
         assert self.homepage.is_aboutpage_display() == True,"not clicked"

    @pytest.mark.allcourse
    def test_click_On_allcourses(self,setup):
        self.homepage.click_on_allcourses()
        assert self.homepage.get_allcoursespage_text() =="All Courses", "Allcoursespage is not clicked"
        assert self.homepage.getTabeName() == "All Courses - Test Academy", "page not found"
        assert self.homepage.is_allcoursespage_display() == True, "not clicked"

    @pytest.mark.placements
    def test_click_On_placements(self, setup):
        self.homepage.click_on_placements()
        assert self.homepage.get_placements_text() == "Placements", "placements is not clicked"
        assert self.homepage.getTabeName() == "Placements - Test Academy", "page not found"
        assert self.homepage.is_placementspage_display() == True, "not clicked"

    @pytest.mark.placements
    def test_click_On_Contact(self, setup):
        self.homepage.click_on_contact()
        assert self.homepage.get_contact_text() == "Contact", "placements is not clicked"
        assert self.homepage.getTabeName() == "Contact - Test Academy", "page not found"
        assert self.homepage.is_contact_display() == True, "not clicked"


    def test_close_browser(self):
        self.driver.close()






