from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
import time 
from pages.locators import hiddenLocator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'open hidden page')
def step_impl(context):
    pageLocator = getattr(hiddenLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

@When(u'click on Not Displayed button')
def step_impl(context):
    notdisplayedLocator = getattr(hiddenLocator, "notdisplayed")
    clickMe1Locator = getattr(hiddenLocator, "clickMe1")
    
    container = context.browser.find_element(notdisplayedLocator.l_type, notdisplayedLocator.selector)
    context.browser.execute_script("arguments[0].style.display = 'block';", container)
    context.browser.find_element(clickMe1Locator.l_type, clickMe1Locator.selector).click()
    
    time.sleep(5)


@When(u'click on visibility hidden button')
def step_impl(context):
    visibility_Locator = getattr(hiddenLocator, "visibility_hidden")
    clickMe2Locator = getattr(hiddenLocator, "clickMe2")
    closeButton2_Locator = getattr(hiddenLocator, "closeButton2")
    test = context.browser.find_element(visibility_Locator.l_type, visibility_Locator.selector)
    context.browser.execute_script("arguments[0].style.visibility = 'visible';", test)
    time.sleep(5)
    context.browser.find_element(clickMe2Locator.l_type, clickMe2Locator.selector).click()
    time.sleep(5)
    #WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((closeButton2_Locator.l_type, closeButton2_Locator.selector))).click()
    #context.browser.find_element(closeButton2_Locator.l_type, closeButton2_Locator.selector).click()

@When(u'click on zero opacity button')
def step_impl(context):
    zero_Locator = getattr(hiddenLocator, "zero_opacity")
    clickMe3Locator = getattr(hiddenLocator, "clickMe3")
    teste1 = context.browser.find_element(zero_Locator.l_type, zero_Locator.selector)
    context.browser.execute_script("arguments[0].style.opacity = '1'", teste1)
    time.sleep(5)
    #context.browser.find_element(clickMe3Locator.l_type, clickMe3Locator.selector).click()
    ActionChains(context.browser)\
        .double_click(teste1)\
        .perform()
    
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((clickMe3Locator.l_type, clickMe3Locator.selector))).click()
    time.sleep(5)

@Then('the messenge that appeared is {message} on {field}')
def step_impl(context,message,field):
    #closeButton_Locator = getattr(hiddenLocator, "closeButton1")
    BasePage.some_message_should_appear(context,hiddenLocator,message,field)    
    #context.browser.find_element(closeButton_Locator.l_type, closeButton_Locator.selector).click()
    time.sleep(5)