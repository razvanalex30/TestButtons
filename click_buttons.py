from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from driver_creation import SeleniumLibraryExt

class ClickButtons:

    def __init__(self):
        self.dict = None
    
    def retrieve_buttons(self):
        """
        Method used to retrieve all the buttons in the page
        :return:
        """
        self.driver = SeleniumLibraryExt.create_driver()
        label_dict = dict()
        xpaths = list()
        form_1 = self.driver.find_elements_by_xpath("//button[contains(@class,'btn btn-primary')]")
        for elem in form_1:
            name = elem.text
            xpath = f"//button[text()='{name}']"
            xpaths.append(xpath)
            label_dict[name] = xpath
        self.dict = label_dict

    def click_selected_button(self, choice):
        self.driver = SeleniumLibraryExt.create_driver()
        source = self.driver.find_element_by_xpath(f"//button[text()='{choice}']")
        action = ActionChains(self.driver)
        if choice == "Double Click Me":
            action.double_click(source).perform()
        elif choice == "Right Click Me":
            action.context_click(source).perform()
        elif choice == "Click Me":
            action.click(source).perform()