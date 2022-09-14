from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
import time 
from pages.locators import date_pickerLocator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when(u'open date picker page')
def step_impl(context):
    pageLocator = getattr(date_pickerLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'I choose the date in the past')
def step_impl(context):
    calendar_Locator = getattr(date_pickerLocator, "calendar")
    day_Locator = getattr(date_pickerLocator, "day_past")
    month_Locator = getattr(date_pickerLocator, "month")
    year_Locator = getattr(date_pickerLocator, "year")
    context.browser.find_element(calendar_Locator.l_type, calendar_Locator.selector).click()
    context.browser.find_element(month_Locator.l_type, month_Locator.selector).click()
    context.browser.find_element(year_Locator.l_type, year_Locator.selector).click()
    context.browser.find_element(By.XPATH,"/html/body/div[2]/div[3]/table/tbody/tr/td/span[2]").click()
    context.browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr/td/span[9]").click()
    context.browser.find_element(day_Locator.l_type, day_Locator.selector).click()
    time.sleep(3)
    
@when(u'I choose the date in the future')
def step_impl(context):
    calendar_Locator = getattr(date_pickerLocator, "calendar")
    day_Locator = getattr(date_pickerLocator, "day_future")
    month_Locator = getattr(date_pickerLocator, "month")
    year_Locator = getattr(date_pickerLocator, "year")
    context.browser.find_element(calendar_Locator.l_type, calendar_Locator.selector).click()
    context.browser.find_element(month_Locator.l_type, month_Locator.selector).click()
    context.browser.find_element(year_Locator.l_type, year_Locator.selector).click()
    context.browser.find_element(By.XPATH,"//html/body/div[2]/div[3]/table/tbody/tr/td/span[6]").click()
    context.browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr/td/span[7]").click()
    context.browser.find_element(day_Locator.l_type, day_Locator.selecto).click()
    time.sleep(3)

    