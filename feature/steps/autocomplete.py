from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
import time 
from pages.locators import autocompleteLocator
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'open autocomplete page')
def step_impl(context):
    pageLocator = getattr(autocompleteLocator, "page")
    original_window = context.browser.current_window_handle
    context.browser.find_element(pageLocator.l_type, pageLocator.selector).click()
    WebDriverWait(context.browser, 2).until(EC.number_of_windows_to_be(2))
    for window_handle in context.browser.window_handles:
        if window_handle != original_window:
            context.browser.switch_to.window(window_handle)
            break


@when(u'when i write {word}')
def step_impl(context,word):
    input_Locator = getattr(autocompleteLocator, "input_autocomplete")
    input_word = context.browser.find_element(input_Locator.l_type, input_Locator.selector)
    #input_word.send_keys(word)
    ActionChains(context.browser)\
        .send_keys_to_element(input_word,word)\
        .send_keys(Keys.ARROW_DOWN)\
        .send_keys(Keys.ENTER)\
        .perform()
    time.sleep(5)

@Then (u'I compare {field} with {expectation}')
def compare(context,field,expectation):
    BasePage.some_message_should_appear(context,autocompleteLocator,expectation,field)


