from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from pages.locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

@given('current page is loginPage')
def step_impl(context):
    WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='udemy-promo-thumbnail']/p[1]/a")))

@when('I click login button')
def scenario(context):
    time.sleep(5)
    original_window = context.browser.current_window_handle
    context.browser.find_element(By.ID,"login-portal").click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break

@when('I fill fields with any data')
def step_impl(context):
    locator_user = getattr(LoginPageLocators, "userName")
    input_user = context.driver.find_element(locator_user.l_type, locator_user.selector)
    input_user.send_keys("carlos")

    locator_pass = getattr(LoginPageLocators, "password")
    input_passwrd = context.driver.find_element(locator_pass.l_type, locator_pass.selector)
    input_passwrd.send_keys("senha123")

@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.ID,"login-button").click()


@then('A failture message should appear on page')
def step_impl(context):
    alert = context.driver.switch_to.alert
    s = alert.text
    print(s)
    alert.dismiss()