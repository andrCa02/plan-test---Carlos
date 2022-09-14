from mailbox import Babyl
from re import X
from selenium.webdriver.common.by import By

"""Locator objects for finding Selenium WebElements"""
class Locator:

    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

"""Login page element locators"""
class LoginPageLocators:
    userName = Locator(By.ID, "text")
    password = Locator(By.ID, "password")
    

class formPageLocators:
    name = Locator(By.NAME,"first_name")
    lastname = Locator(By.NAME,"last_name")
    email = Locator(By.NAME,"email")
    comment = Locator(By.NAME,"message")

class objectPageLocator: 
    firstImage = Locator(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div/div[1]/img")
    backbutton = Locator(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/a[1]")
    Our_Products = Locator(By.XPATH,"/html/body/div[1]/div/div/nav/div/ul/li[2]/a")
    Contact_Us = Locator(By.XPATH,"/html/body/div[1]/div/div/nav/div/ul/li[3]/a")
    box1 = Locator(By.XPATH,"/html/body/div[1]/div/div/div[2]")
    box2 = Locator(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div")
    box3 = Locator(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[3]/div")
    box4 = Locator(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[4]/div")


class buttonClickLocator:
    
    closeButton1 = Locator(By.XPATH,"/html/body/div[1]/div[4]/div/div/div[3]/button")
    closeButton2 = Locator(By.XPATH,"/html/body/div[1]/div[5]/div/div/div[3]/button")
    closeButton3 = Locator(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[1]/button")
    button1 = Locator(By.ID,"button1")
    button2 = Locator(By.ID,"button2")
    button3 = Locator(By.ID,'button3')

class toDoListLocator:
    addInput = Locator (By.XPATH,"/html/body/div/input")
    deleteButton = Locator(By.XPATH,"/html/body/div/ul/li[3]/span")
    check_button = Locator(By.XPATH,'/html/body/div/ul/li[1]')

class text_appearLocator:
    box1 = Locator (By.ID,"manual-testing-accordion")
    box2 = Locator(By.ID,"cucumber-accordion")
    box3 = Locator(By.ID,"automation-accordion")
    box4 = Locator(By.ID,"click-accordion")

class dropdown_menuLocator:
    dropdown1 = Locator(By.ID,"dropdowm-menu-1")
    dropdown2 = Locator(By.ID,"dropdowm-menu-2") 
    dropdown3 = Locator(By.ID,"dropdowm-menu-3")
    checkbox1 = Locator(By.XPATH,"/html/body/div/div[3]/div/div/label[1]/input")
    checkbox2 = Locator(By.XPATH,"/html/body/div/div[3]/div/div/label[2]/input")
    checkbox3 = Locator(By.XPATH,"/html/body/div/div[3]/div/div/label[3]/input")
    checkbox4 = Locator(By.XPATH,"/html/body/div/div[3]/div/div/label[4]/input")
    
class ajaxLocator:
    page = Locator(By.ID,"ajax-loader")
    button = Locator(By.ID,"button1")

class scrollingLocator:
    page = Locator(By.ID,"scrolling-around")
    scrollingZone = Locator(By.ID,"zone4")
    MouseZone = Locator(By.ID,"zone2")

class popupLocator:
    page = Locator(By.ID,"popup-alerts")
    javascriptButton = Locator(By.ID,"button1")
    modalPopup = Locator(By.ID,"button2")
    ajaxLoader = Locator(By.ID,"button3")
    clickME = Locator(By.ID,"button1")
    javascriptBox = Locator(By.ID,"button4")
    closeModal = Locator(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[3]/button")

class hiddenLocator:
    page = Locator(By.ID,"hidden-elements")
    Not_displayed_message = Locator(By.XPATH,"/html/body/div[1]/div[4]/div/div/div[1]/h4")
    notdisplayed = Locator(By.ID,"not-displayed")
    clickMe1 = Locator(By.XPATH,"/html/body/div/div[2]/div/div/div[1]/div/div/span/p")
    closeButton1 = Locator(By.XPATH,"/html/body/div[1]/div[4]/div/div/div[3]/button")

    visibility_hidden = Locator(By.ID,"visibility-hidden")
    visibility_hidden_message = Locator(By.XPATH,"/html/body/div[1]/div[5]/div/div/div[1]/h4")
    clickMe2 = Locator(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div/div/span")
    closeButton2 = Locator(By.XPATH,"/html/body/div[1]/div[6]")

    zero_opacity = Locator(By.ID,"zero-opacity")
    zero_opacity_message = Locator(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[1]/h4")
    clickMe3 = Locator(By.ID,"button3")
    closeButton2 = Locator(By.XPATH,"/html/body/div[1]/div[6]")

class autocompleteLocator: 
    page = Locator(By.ID,"autocomplete-textfield")
    input_autocomplete = Locator(By.ID,"myInput")
    tester = Locator(By.XPATH,"/html/body/div[1]/div/div/section/div/div[2]/form/div/input")

class file_uploadLocator:
    page = Locator(By.ID,"file-upload")
    upload_button = Locator(By.ID,"myFile")
    submit_button = Locator(By.ID,"submit-button")

class date_pickerLocator:
    page = Locator(By.ID,"datepicker")
    calendar = Locator(By.XPATH,"/html/body/div/div[2]/div/div/span")
    day_past = Locator(By.XPATH,"/html/body/div[2]/div[1]/table/tbody/tr[3]/td[3]")
    day_future = Locator(By.XPATH,"/html/body/div[2]/div[1]/table/tbody/tr[3]/td[5]")
    month = Locator(By.XPATH,"/html/body/div[2]/div[1]/table/thead/tr[1]/th[2]")
    year = Locator(By.XPATH,"/html/body/div[2]/div[2]/table/thead/tr/th[2]")

class action_Locator:
    page = Locator(By.ID,"actions")
    dragBox = Locator(By.XPATH,"/html/body/div/div[2]/div/div[1]")
    dropHere = Locator(By.XPATH,"/html/body/div/div[2]/div/div[2]")
    double_click_box = Locator(By.ID,"double-click")
    hold_box = Locator(By.ID,"click-box")
