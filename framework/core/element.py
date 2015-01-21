from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement


class WebElement(SeleniumWebElement):

    def find_id(self, id):
        return self.find_element(by=By.ID, value=id)

    def find_ids(self, id_):
        return self.find_elements(by=By.ID, value=id_)

    def find_tag(self, name):
        return self.find_element(by=By.TAG_NAME, value=name)

    def find_tags(self, name):
        return self.find_elements(by=By.TAG_NAME, value=name)

    def find_class(self, name):
        return self.find_element(by=By.CLASS_NAME, value=name)

    def find_classes(self, name):
        return self.find_elements(by=By.CLASS_NAME, value=name)

    def find_name(self, name):
        return self.find_element(by=By.NAME, value=name)

    def find_names(self, name):
        return self.find_elements(by=By.NAME, value=name)

    def set_text(self, keys=''):
        data = {
            'elementId': self._id,
            'value': [keys]
        }
        self._execute('replaceKeys', data)
        return self
