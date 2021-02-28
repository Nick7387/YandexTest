import pytest
from selenium import webdriver

# Инициализируем webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    yield driver
    driver.quit()