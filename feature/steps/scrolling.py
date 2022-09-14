from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time 
from pages.locators import scrollingLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'open scrolling around page')
def step_impl(context):
    pageLocator = getattr(scrollingLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'scrolling the page')
def step_impl(context):
    ZoneLocator = getattr(scrollingLocator, "scrollingZone")
    iframe = context.browser.find_element(ZoneLocator.l_type, ZoneLocator.selector)
    ActionChains(context.browser)\
        .click(iframe)\
        .perform()
    time.sleep(5)

@when(u'put mouse on the zone')
def step_impl(context):
    MouseLocator = getattr(scrollingLocator, "MouseZone")
    test = context.browser.find_element(MouseLocator.l_type, MouseLocator.selector)
    ActionChains(context.browser)\
        .click(test)\
        .perform()
    time.sleep(5)