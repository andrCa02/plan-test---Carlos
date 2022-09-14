from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from pages.locators import dropdown_menuLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

@when(u'open dropown menu page')
def step_impl(context):
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"dropdown-checkboxes-radiobuttons").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

#scenario 1
@when(u'click on dropdown menu/linguages')
def step_impl(context):
    linguages =[]
    dropdown1Locator = getattr(dropdown_menuLocator, "dropdown1")
    drop1 = context.browser.find_element(dropdown1Locator.l_type, dropdown1Locator.selector)
    select_object = Select(drop1)
    linguages = ["java","c#","python","sql"]
    

    for x in linguages:
        select_object.select_by_value(x)
        time.sleep(2)
    
@when(u'click on second dropdown menu')
def step_impl(context):
    dropdown2Locator = getattr(dropdown_menuLocator, "dropdown2")
    drop2 = context.browser.find_element(dropdown2Locator.l_type, dropdown2Locator.selector)
    select_object = Select(drop2)
    IDe = ["eclipse","maven","testng","junit"]
    for y in IDe:
        select_object.select_by_value(y)
        time.sleep(2)

@when(u'click on the third dropdown menu')
def step_impl(context):
    dropdown3Locator = getattr(dropdown_menuLocator, "dropdown3")
    drop3 = context.browser.find_element(dropdown3Locator.l_type, dropdown3Locator.selector)
    select_object = Select(drop3)
    web = ["html","css","javascript","jquery"]
    for k in web:
        select_object.select_by_value(k)
        time.sleep(2)

@when(u'I click on the checkbox options')
def step_impl(context):
    #checkbox 1
    check1Locator = getattr(dropdown_menuLocator, "checkbox1")
    context.browser.find_element(check1Locator.l_type, check1Locator.selector).click()
    #checkbox2
    check2Locator = getattr(dropdown_menuLocator, "checkbox2")
    context.browser.find_element(check2Locator.l_type, check2Locator.selector).click()
    #checkbox3
    check3Locator = getattr(dropdown_menuLocator, "checkbox3")
    context.browser.find_element(check3Locator.l_type, check3Locator.selector).click()
    #checkbox4
    check4Locator = getattr(dropdown_menuLocator, "checkbox4")
    context.browser.find_element(check4Locator.l_type, check4Locator.selector).click()
    time.sleep(5)

@when(u'I click on each radio options')
def step_impl(context):
    IDe = [1,2,3,4,5]
    for y in IDe:
        context.browser.find_element(By.XPATH,f"//*[@id='radio-buttons']/input[{y}]").click()
        time.sleep(2)