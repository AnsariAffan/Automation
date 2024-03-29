from selenium.webdriver.support import expected_conditions as EC

import selenium
from selenium.webdriver.support.wait import WebDriverWait


class Utilities:

    '''================================================UTILITIS FUNCTIONS============================================'''

    def __init__(self,driver):
        self.driver = driver

    def click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def take_findelements(self,by_loators):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_loators))

    def getElementText(self,by_locator):
        elementText = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return elementText.text

    def sendKey(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_Keys(text)

    def getTabeName(self):
        return self.driver.title

    def isDisplay(self,by_locator):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()


    def closebrowser(self):
       self.driver.close()