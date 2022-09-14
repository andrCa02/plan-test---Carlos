from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from context.config import Settings
from pages.locators import formPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

@given('current page is homepage')
def scenario(context):
    WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='udemy-promo-thumbnail']/p[1]/a")))
   
@when('I click contact button')
def scenario(context):
    time.sleep(5)
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"contact-us").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break
    #context.browser.find_element(By.XPATH,"//div[@class='caption' and text()='Contact Us Form']").click()
    #WebDriverSleep(context.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='section-title' and text()='CONTACT US']"))).click() #dever de casa
    
@when('I fill fields with correct data')
def scenario(context):
    locator_name = getattr(formPageLocators, "name")
    input_name = context.browser.find_element(locator_name.l_type, locator_name.selector)
    input_name.send_keys("carlos")
    
    locator_lastName = getattr(formPageLocators,"lastname")
    input_lastname = context.browser.find_element(locator_lastName.l_type, locator_lastName.selector)
    input_lastname.send_keys("nascimento")

    locator_email = getattr(formPageLocators,"email")
    input_email = context.browser.find_element(locator_email.l_type, locator_email.selector)
    input_email.send_keys("carlos@gmail.com")

    locator_comment = getattr(formPageLocators,"comment")
    input_comment = context.browser.find_element(locator_comment.l_type, locator_comment.selector)
    input_comment.send_keys("any message")
    

@When('I click on submit button')
def step_impl(context):
    context.browser.find_element(By.XPATH,"//*[@id='form_buttons']/input[2]").click()

@then('A sucess message should appear on page')
def step_impl(context):
    l= context.browser.find_element(By.XPATH,"//*[@id='contact_reply']/h1")
    s= l.text
    if(s =='Thank You for your Message!'):
        print('funciona '+s)
    else:
        print('não funcionou')


@then('A failure messagem should appear')
def step_impl(context):
    f= context.browser.find_element(By.XPATH,"/html/body")
    teste = f.text
    if(teste == "Error: all fields are required" or "Error: Invalid email address"):
        print('fuciona'+ teste)
    else:
        print("nao funciona")


   