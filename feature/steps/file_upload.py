from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
import time 
from pages.locators import file_uploadLocator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'open file upload page')
def step_impl(context):
    pageLocator = getattr(file_uploadLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'I choose my {file}')
def step_impl(context,file):
    upload_Locator = getattr(file_uploadLocator, "upload_button")
    test=context.browser.find_element(upload_Locator.l_type, upload_Locator.selector)
    test.send_keys(file)
    time.sleep(4)

@when(u'I click on submit button - file upload')
def step_impl(context):
    submit_Locator = getattr(file_uploadLocator, "submit_button")
    context.browser.find_element(submit_Locator.l_type, submit_Locator.selector).click()
    time.sleep(5)

@then(u'the messenge appeared')
def step_impl(context):
    alert = context.browser.switch_to.alert
    s = alert.text
    print(s)
    alert.accept()

   


    

