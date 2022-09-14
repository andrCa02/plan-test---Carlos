from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from context.config import Settings
from pages.locators import buttonClickLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC



@when(u'I click button_click button')
def step_impl(context):
    time.sleep(5)
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"button-clicks").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'I click on WebElement Click button')
def step_impl(context):
    time.sleep(2)
    locator_1 = getattr(buttonClickLocator, "button1")
    context.browser.find_element(locator_1.l_type, locator_1.selector).click()

@when(u'Open and close a modal WebElement')
def step_impl(context):
    time.sleep(2)
    close = getattr(buttonClickLocator, "closeButton1")
    context.browser.find_element(close.l_type, close.selector).click()
    #context.browser.find_element(By.CLASS_NAME,"'modal-title' and text()='Congratulations!'")
    #WebDriverWait(context.browser, 2).until(EC.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[3]/button")).click()
    

#botao 2

@when(u'I click on JavaScript Click button')
def step_impl(context):
    time.sleep(2)
    locator_2 = getattr(buttonClickLocator, "button2")
    context.browser.find_element(locator_2.l_type, locator_2.selector).click()
    #context.browser.find_element(By.CLASS_NAME,"'modal-title' and text()='It’s that Easy!!  Well I think it is.....'")
    #WebDriverWait(context.browser, 2).until(EC.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[3]/button")).click()

@when(u'Open and close a modal JavaScript')
def step_impl(context):
    time.sleep(2)
    close2 = getattr(buttonClickLocator, "closeButton2")
    context.browser.find_element(close2.l_type, close2.selector).click()

#botao 3
@when(u'I click on Action Move & Click button')
def step_impl(context):
    time.sleep(2)
    locator_3 = getattr(buttonClickLocator, "button3")
    context.browser.find_element(locator_3.l_type, locator_3.selector).click()


@when(u'Open and close a modal Action Move')
def step_impl(context):
    time.sleep(2)
    #close3 = getattr(buttonClickLocator, "closeButton3")
    #context.browser.find_element(close3.l_type, close3.selector).click()
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[3]/button")).click()
    time.sleep(2)
@Then ('close browser')
def step_impl(context):
    time.sleep(2)
    context.browser.quit()