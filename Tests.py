from selenium import webdriver

import time

import pytest

from YandexPages import SearchHelper

# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
#     yield driver
#     driver.quit()

driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
login="neuroappuser@yandex.ru"
password="vytctujlyz30ktn"
letter_from="neuroappuser@yandex.ru"
letter_to="neuroappuser@yandex.ru"
theme="Тестовое задание. Погорелов"

def test_yandex(driver,login,password,letter_from,letter_to,theme):
    yandex_main_page = SearchHelper(driver)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_mail_href()
    yandex_main_page.click_login_account_button()
    yandex_main_page.enter_login_name(login)
    yandex_main_page.click_login_next_button()
    yandex_main_page.enter_password_name(password)
    yandex_main_page.click_password_next_button()
    yandex_main_page.click_search_email_filter_button()
    yandex_main_page.click_search_email_filter_from_button()
    yandex_main_page.enter_search_email_filter_from_data(letter_from)

    time.sleep(5)
    
    n_letters=yandex_main_page.get_amount_of_letters_from()
    print(n_letters)
    time.sleep(5)
    
    yandex_main_page.click_write_an_email_button()
    yandex_main_page.write_recipient_email(letter_to)
    yandex_main_page.write_theme_of_the_email(theme)
    yandex_main_page.write_a_body_of_the_letter("Найдено писем: "+str(n_letters))
    yandex_main_page.click_send_the_letter_button()
    
    
    
    
test_yandex(driver,login,password,letter_from,letter_to,theme)
time.sleep(5)
driver.quit()