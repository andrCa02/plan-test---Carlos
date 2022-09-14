from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
import time 
from pages.locators import tableLocator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when(u'open table page')
def step_impl(context):
    pageLocator = getattr(tableLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

@when(u'get {text} from {field}')
def step_impl(context,text,field):
    text_Locator = getattr(tableLocator, "text_table")
    BasePage.some_message_should_appear(context,tableLocator,text,field)