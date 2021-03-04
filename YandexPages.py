from BaseApp import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_MAIL_LOGIN_HREF = (By.CLASS_NAME, "b-inline")
    
class YandexRegMailLocators:
    LOCATOR_YANDEX_MAIL_CREATE_ACCOUNT_BUTTON = (By.CLASS_NAME, "HeadBanner-ButtonsWrapper>a:nth-child(1)")
    LOCATOR_YANDEX_MAIL_LOGIN_ACCOUNT_BUTTON = (By.CLASS_NAME, "HeadBanner-ButtonsWrapper>a:nth-child(2)")
    LOCATOR_YANDEX_MAIL_LOGIN_NAME_FIELD = (By.ID, "passp-field-login")
    LOCATOR_YANDEX_MAIL_LOGIN_NEXT_BUTTON = (By.CSS_SELECTOR, ".Button2_view_action")
    LOCATOR_YANDEX_MAIL_PASSWORD_FIELD = (By.ID, "passp-field-passwd")
    LOCATOR_YANDEX_MAIL_PASSWORD_NEXT_BUTTON = (By.CSS_SELECTOR, ".Button2_view_action")
    
class YandexMailLocators:
    LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FIELD = (By.CSS_SELECTOR, "[class='textinput__control']")
    LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_START_BUTTON = (By.CSS_SELECTOR, ".search-input__form-button")
    LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_BUTTON = (By.CSS_SELECTOR, "[class='control button2 button2_view_default button2_tone_mail-suggest-themed button2_size_n button2_theme_normal search-input__advanced-button']")
    LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_FROM_BUTTON = (By.CLASS_NAME, "mail-AdvancedSearch>button:nth-child(4)")
    LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_FROM_FIELD = (By.CSS_SELECTOR, ".mail-AdvancedSearch-ContactSelector .textinput .textinput__control")
    
    
    LOCATOR_YANDEX_MAIL_GET_AMOUNT_OF_LETTERS = (By.CLASS_NAME, "mail-MessagesSearchInfo-Title")
    LOCATOR_YANDEX_MAIL_WRITE_AN_EMAIL_BUTTON = (By.CLASS_NAME, "mail-ComposeButton-Text")
    LOCATOR_YANDEX_MAIL_WRITE_RECIPIENT_EMAIL = (By.CSS_SELECTOR, ".ComposeYabblesField .composeYabbles")
    LOCATOR_YANDEX_MAIL_WRITE_THEME_OF_THE_EMAIL = (By.CSS_SELECTOR, ".composeTextField")
    LOCATOR_YANDEX_MAIL_WRITE_A_BODY_OF_THE_LETTER = (By.CSS_SELECTOR, ".composeReact-MBodyPanels .cke_wysiwyg_div")
    LOCATOR_YANDEX_MAIL_SEND_THE_LETTER_BUTTON = (By.CSS_SELECTOR, ".theme-colorful .ComposeSendButton .button2.button2.button2")
    

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
    
    def click_on_mail_href(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_MAIL_LOGIN_HREF,time=2).click()

#----------------------------------------
 
    def click_create_account_button(self):
        return self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_CREATE_ACCOUNT_BUTTON,time=2).click()
    
    def click_login_account_button(self):
        return self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_LOGIN_ACCOUNT_BUTTON,time=2).click()
    
    
    def enter_login_name(self, word):
        login_name_field = self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_LOGIN_NAME_FIELD)
        login_name_field.click()
        login_name_field.send_keys(word)
        return login_name_field
    
    def click_login_next_button(self):
        return self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_LOGIN_NEXT_BUTTON,time=2).click()
    
    def enter_password_name(self, word):
        password_field = self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(word)
        return password_field
    
    def click_password_next_button(self):
        return self.find_element(YandexRegMailLocators.LOCATOR_YANDEX_MAIL_PASSWORD_NEXT_BUTTON,time=2).click()

#----------------------------------------

    def enter_search_email_data(self, word):
        email_data = self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FIELD)
        email_data.click()
        email_data.send_keys(word)
        return email_data
    
    def click_search_email_start_button(self):
        return self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FIELD,time=2).click()
    
    def click_search_email_filter_button(self):
        self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FIELD).click()
        return self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_BUTTON,time=2).click()
    
    def click_search_email_filter_from_button(self):
        return self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_FROM_BUTTON,time=2).click()
    
    def enter_search_email_filter_from_data(self, word):
        self.email_filter_from = self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEARCH_EMAIL_FILTER_FROM_FIELD)
        self.email_filter_from.click()
        #self.email_filter_from.send_keys(word)
        for i in word:
            self.email_filter_from.send_keys(i)
            time.sleep(0.5)
        self.email_filter_from.send_keys(Keys.ENTER)
        return self.email_filter_from
    
    def enter_search_email_filter_from_confirm(self):
        return self.email_filter_from.submit()
    
    def get_amount_of_letters_from(self):
        str=self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_GET_AMOUNT_OF_LETTERS,time=2).text
        if str=="одно письмо":
           self.nletter=1
        else:
            self.nletters= [int(s) for s in str.split() if s.isdigit()]
        return self.nletters[0]

    def click_write_an_email_button(self):
        return self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_WRITE_AN_EMAIL_BUTTON,time=2).click()
    
    def write_recipient_email(self, word):
        recipient_data = self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_WRITE_RECIPIENT_EMAIL)
        recipient_data.click()
        recipient_data.send_keys(word)
        return recipient_data
    
    def write_theme_of_the_email(self, word):
        theme_data = self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_WRITE_THEME_OF_THE_EMAIL)
        theme_data.click()
        theme_data.send_keys(word)
        return theme_data
    
    def write_a_body_of_the_letter(self, word):
        theme_data = self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_WRITE_A_BODY_OF_THE_LETTER)
        theme_data.click()
        theme_data.send_keys(word)
        return theme_data

    def click_send_the_letter_button(self):
        return self.find_element(YandexMailLocators.LOCATOR_YANDEX_MAIL_SEND_THE_LETTER_BUTTON,time=2).click()
    