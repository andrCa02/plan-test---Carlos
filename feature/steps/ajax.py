from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
import time 
from pages.locators import ajaxLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'open ajax page')
def step_impl(context):
    pageLocator = getattr(ajaxLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'wait and click on the button')
def step_impl(context):
    check1Locator = getattr(ajaxLocator, "button")
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((check1Locator.l_type, check1Locator.selector))).click()