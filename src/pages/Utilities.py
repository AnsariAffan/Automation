from selenium.webdriver.support import expected_conditions as EC

import selenium
from selenium.webdriver.support.wait import WebDriverWait


class Utilities:

    def __init__(self,driver):
        self.driver = driver

    def click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def getElementText(self,by_locator):
      elementText = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
      return elementText.text

    def sendKey(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_Keys(text)