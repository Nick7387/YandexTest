from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Базовая short страница Yandex

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
# Базовая страница сервиса Yandex.Почта

class MailBase:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://mail.yandex.ru/"
        
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
                      
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
# Страница регистрации нового пользователя в Yandex.Почта.

class MailRegistration:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://passport.yandex.ru/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
                      
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
# Страница авторизации пользователя в Yandex.Почта.
   
class MailAuthorisation:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://passport.yandex.ru/auth?from=mail&require_hint=1&origin=hostroot_homer_reg_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
                      
    def go_to_site(self):
        return self.driver.get(self.base_url)