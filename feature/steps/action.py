from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
import time 
from pages.locators import action_Locator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'open action page')
def step_impl(context):
    pageLocator = getattr(action_Locator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

@when (u'I drag to my target')
def dragToBox(context):
    dragLocator = getattr(action_Locator, "dragBox")
    dropHereLocator = getattr(action_Locator, "dropHere")
    box = context.browser.find_element(dragLocator.l_type, dragLocator.selector)
    drop_here = context.browser.find_element(dropHereLocator.l_type, dropHereLocator.selector)
    ActionChains(context.browser)\
        .drag_and_drop(box,drop_here)\
        .perform()
    time.sleep(5)

@when (u'I double click')
def doubleClick(context):
    double_click_Locator = getattr(action_Locator, "double_click_box")
    double_click = context.browser.find_element(double_click_Locator.l_type, double_click_Locator.selector)
    ActionChains(context.browser)\
        .double_click(double_click)\
        .perform()
    time.sleep(5)

@when (u'I hold the button')
def doubleClick(context):
    hold_Locator = getattr(action_Locator, "hold_box")
    holding_click = context.browser.find_element(hold_Locator.l_type, hold_Locator.selector)
    ActionChains(context.browser)\
        .click_and_hold(holding_click)\
        .perform()
    time.sleep(5)