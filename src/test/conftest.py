import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='class')
def init_driver():
    web_driver = webdriver.Chrome(service=Service("C:/Users/ANSARI/Downloads/driver/chromedriver.exe"))