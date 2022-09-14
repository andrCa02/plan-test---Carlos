from datasource.message import MESSAGES
from multiprocessing.connection import wait
from xml.etree.ElementTree import Comment
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from nose.tools import assert_equals

class BasePage(object):
    def __init__(self, browser, base_url):

        self.browser = browser

        self.base_url = base_url

        self._timeout = 40

        self.implicit_wait = 40
    
    def replace_space(data):
         return data.replace(' ', '_')


    def datapool_read(self, source, data, key):
        """Get a list of arguments named as 'data' on the 'source' and search the 'key' on that list."""
        data_args = source.get(self.replace_space(data))
        dt_key = self.replace_space(key)
        #key.replace(' ', '_')
        if data_args is not None:
        #Search the 'key' on that list
            if data_args[0].get(dt_key)is not None:
                return data_args[0].get(dt_key)
            else:
                message = "No matching results for parameter data = "+ data +" on the key = " + key +" was found in DataPool."
                raise Exception(message)
        else:
            message = "No matching results for parameter data = "+ data +" on the key = " + key +" was found in DataPool."
            raise Exception(message)

    #------------------------------------------------------------------------------------------------------------------------------#

    # SOME_MESSAGE_SHOULD_APPEAR is a method designed to check if some error/message appeared during the test, in this case if a   #

    # error/message was not thrown the the test failed                                                                             #

    #                                                                                                                              #

    # It is necessary to pass the locator of which input will be analyzed by parameter and which error/message should appear.      #

    #------------------------------------------------------------------------------------------------------------------------------#
    def some_message_should_appear(context, page, message_key, messageInput):

        base_page = BasePage

        # Getting the attribute (location of element) from class, passing the current input as parameter

        current_input = getattr(page, BasePage.replace_space(messageInput))

        element_isDisplayed = BasePage.element_displayed(base_page, context, current_input)

        # If no message appears on the current input then the exception is thrown

        if not element_isDisplayed:

            raise Exception("The element was not found or the message not appeared on the " + messageInput + " field")

        else:

            current_message = BasePage.get_element(base_page, context, current_input).text

            expected_message = base_page.datapool_read(base_page, MESSAGES, "message", message_key)

            BasePage.compare_message(expected_message, current_message)

    
    #----------------------------------------------------------------------------------------------------------------------#

    # ELEMENT_DISPLAYED is a method designed to verify if some element is displayed (visible)                              #                                                                                                                                                                                

    #                                                                                                                      #

    # It is necessary to pass the locator of which element will be analyzed by parameter                                   #                                                                                                                                                                                

    #----------------------------------------------------------------------------------------------------------------------#

    def element_displayed(self, context, locator):

        try:

            WebDriverWait(context.browser, 60).until(EC.visibility_of_element_located((locator.l_type, locator.selector)))

        except TimeoutException:

            message = "The element or the selector "+ locator.selector +" is not visible, can't be found or it doesn't exist on the screen."

            raise Exception(message)

        return True

    #----------------------------------------------------------------------------------------------------------------------#

    # GET_ELEMENT is a method designed to find and get the current element                                                 #                                                                                                                                                                                

    #                                                                                                                      #

    # It is necessary to pass the locator of which element will be analyzed by parameter                                   #

    #----------------------------------------------------------------------------------------------------------------------#

    def get_element(self, context, locator):

        if not self.locate_element(self, context, locator):

            raise NoSuchElementException("Could not find {locator.selector}")

        return context.browser.find_element(locator.l_type, locator.selector)
    
    #----------------------------------------------------------------------------------------------------------------------#

    # COMPARE_MESSAGE is a method designed to verify if expected message is the same as result message       #                                                                                                                                                                                

    #                                                                                                                      #

    # It is necessary to pass both messages by parameter                                                                   #                                                                                                                                                                                

    #----------------------------------------------------------------------------------------------------------------------#

    def compare_message(expected_message, current_message):

        try:

            assert_equals(expected_message, current_message)

        except AssertionError:

            message = "The expected message/title was different than the current message/title.\n\nExpected message/title: " + expected_message + "\nCurrent message/title: " + current_message

            raise Exception(message)

    #----------------------------------------------------------------------------------------------------------------------#

    # LOCATE_ELEMENT is a method designed to locate an element on page                                                        #                                                                                                                                                                                

    #                                                                                                                      #

    # It is necessary to pass the locator of which element will be analyzed by parameter                                   #

    #----------------------------------------------------------------------------------------------------------------------#

    def locate_element(self, context, locator):

        try:

            return WebDriverWait(context.browser, 140).until(EC.presence_of_element_located((locator.l_type, locator.selector)))

        except TimeoutException:

             message = "The element or the selector "+ locator.selector +" can't be found or it doesn't exist on the screen."

             raise Exception(message)
