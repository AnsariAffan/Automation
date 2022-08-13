from selenium.webdriver.common.by import By

from src.Config.config import TestData
from src.pages.Utilities import Utilities


class HomePage(Utilities):

# All Homepage selector path
    logo = (By.XPATH,"//div[@class='ast-main-header-wrap main-header-bar-wrap ']//span[1]")
    all_nav_items = (By.XPATH,"//div[@id='ast-desktop-header']/div[1]")
    homePage = (By.XPATH, "//li[@id='menu-item-25307']/a[text()='Home']")
    about = (By.XPATH,"//li[@id='menu-item-25308']/a[.='About']")
    allCourses = (By.XPATH, "//li[@id='menu-item-25309']/a[.='All Courses']")
    placement = (By.XPATH,"//li[@id='menu-item-25520']/a[.='Placements']")
    contact = (By.XPATH,"//li[@id='menu-item-25310']/a[.='Contact']")

# homePage fucntions
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.baseURL)

#Logo
    def click_on_logo(self):
        return self.click(self.logo)


    def get_logo_text(self):
        return self.getElementText(self.logo)

#Home Page
    def click_on_home_page(self):
       return self.click(self.homePage)

    def get_homepage_text(self):
        return self.getElementText(self.homePage)

#About Page
    def click_on_about_page(self):
        return  self.click(self.about)

    def get_aboutpage_text(self):
        return self.getElementText(self.about)


#All courses Page
    def click_on_allcourses(self):
        return self.click(self.allCourses)

    def get_allcoursespage_text(self):
        return self.getElementText(self.allCourses)

#All placments Page
    def click_on_placements(self):
        return self.click(self.placement)

    def get_placements_text(self):
        return self.getElementText(self.placement)

#All contact Page
    def click_on_contact(self):
        return self.click(self.contact)

    def get_contact_text(self):
        return self.getElementText(self.contact)

