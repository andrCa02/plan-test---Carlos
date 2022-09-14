from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from pages.locators import text_appearLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@when(u'open text appear page')
def step_impl(context):
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[6]/a").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'click on text boxes')
def step_impl(context):
    time.sleep(12)
    locator_1 = getattr(text_appearLocator, "box1")
    locator_2 = getattr(text_appearLocator, "box2")
    locator_3 = getattr(text_appearLocator, "box3")
    locator_4 = getattr(text_appearLocator, "box4")
    box1 = context.browser.find_element(locator_1.l_type, locator_1.selector).click()
    box2 = context.browser.find_element(locator_2.l_type, locator_2.selector).click()
    box3 = context.browser.find_element(locator_3.l_type, locator_3.selector).click()
    box4 = context.browser.find_element(locator_4.l_type, locator_4.selector).click()
    
    #context.browser.find_element(By.XPATH,"//*[@id='form_buttons']/input[2]").click()
   
    
    #WebDriverWait(context.browser, 6).until(EC.element_to_be_clickable(box4)).click()
    time.sleep(10)