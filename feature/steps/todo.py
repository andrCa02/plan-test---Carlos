from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from pages.locators import toDoListLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@when('I click on to do button')
def step_impl(context):
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"to-do-list").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'write something and submit')
def step_impl(context):
    locator_input = getattr(toDoListLocator, "addInput")
    add_input = context.browser.find_element(locator_input.l_type, locator_input.selector)
    add_input.send_keys("do my homework",Keys.ENTER)
    time.sleep(5)

@when(u'check')
def step_impl(context):
    l= context.browser.find_element(By.XPATH,"/html/body/div/ul/li[4]/span")
    s= l.text
    #WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='udemy-promo-thumbnail']/p[1]/a")))
    if(s =='do my homework'):
        print('funciona '+s)
        context.browser.quit()
    else:
        print('não funcionou')

@when(u'I click on delete button')
def step_impl(context):
    locator_delete = getattr(toDoListLocator, "deleteButton")
    delete_button = context.browser.find_element(locator_delete.l_type, locator_delete.selector)
    
    ActionChains(context.browser)\
        .click(delete_button)\
        .perform()
        

    time.sleep(2)

@When ('I finished a task')
def step_impl(context):
    locator_check = getattr(toDoListLocator, "check_button")
    context.browser.find_element(locator_check.l_type, locator_check.selector).click()
    time.sleep(3)
