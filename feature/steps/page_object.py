from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time 
from selenium import webdriver
from pages.locators import objectPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@when(u'I click page object button')
def step_impl(context):
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"page-object-model").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'test caousel')
def step_impl(context):
    image1Locator = getattr(objectPageLocator, "firstImage")
    back_buttonLocator = getattr(objectPageLocator, "backbutton")
    WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((image1Locator.l_type, image1Locator.selector)))
    context.browser.find_element(back_buttonLocator.l_type, back_buttonLocator.selector).click()
    time.sleep(5)
    
@when(u'check images')
def step_impl(context):
    print("test")

@when(u'I click on buttons and check')
def step_impl(context):
    ProductLocator = getattr(objectPageLocator, "Our_Products")
    contactLocator = getattr(objectPageLocator, "Contact_Us")
    context.browser.find_element(ProductLocator.l_type, ProductLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.url_to_be("http://webdriveruniversity.com/Page-Object-Model/products.html"))
    context.browser.find_element(contactLocator.l_type, contactLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.url_to_be("http://webdriveruniversity.com/Contact-Us/contactus.html"))

@when(u'check if the boxes loaded')
def step_impl(context):
    box1Locator = getattr(objectPageLocator, "box1")
    box2Locator = getattr(objectPageLocator, "box2")
    box3Locator = getattr(objectPageLocator, "box3")
    box4Locator = getattr(objectPageLocator, "box4")
    WebDriverWait(context.browser, 2).until(EC.visibility_of_element_located((box1Locator.l_type, box1Locator.selector)))
    WebDriverWait(context.browser, 2).until(EC.visibility_of_element_located((box2Locator.l_type, box2Locator.selector)))
    WebDriverWait(context.browser, 2).until(EC.visibility_of_element_located((box3Locator.l_type, box3Locator.selector)))
    WebDriverWait(context.browser, 2).until(EC.visibility_of_element_located((box4Locator.l_type, box4Locator.selector)))