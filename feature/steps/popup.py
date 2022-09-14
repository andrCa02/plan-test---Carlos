from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time 
from pages.locators import popupLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'open popup page')
def step_impl(context):
    pageLocator = getattr(popupLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

@When(u'click on javascript alert button')
def step_impl(context):
    javascriptLocator = getattr(popupLocator, "javascriptButton")
    context.browser.find_element(javascriptLocator.l_type, javascriptLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.alert_is_present())
    alert = context.browser.switch_to.alert
    alert.dismiss()

@When(u'click on modal button')
def step_impl(context):
    modalLocator = getattr(popupLocator, "modalPopup")
    clasemodalLocator = getattr(popupLocator, "closeModal")
    context.browser.find_element(modalLocator.l_type, modalLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.element_to_be_clickable((clasemodalLocator.l_type, clasemodalLocator.selector))).click()
    time.sleep(5)

@When(u'click on ajax button')
def step_impl(context):
    ajaxLocator = getattr(popupLocator, "ajaxLoader")
    clickmeLocator = getattr(popupLocator, "clickME")
    context.browser.find_element(ajaxLocator.l_type, ajaxLocator.selector).click()
    WebDriverWait(context.browser, 8).until(EC.element_to_be_clickable((clickmeLocator.l_type, clickmeLocator.selector))).click()

@When(u'click on javascript box')
def step_impl(context):
    javascriptboxLocator = getattr(popupLocator, "javascriptBox")
    context.browser.find_element(javascriptboxLocator.l_type, javascriptboxLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.alert_is_present())
    alert = context.browser.switch_to.alert
    alert.accept()
    time.sleep(5)