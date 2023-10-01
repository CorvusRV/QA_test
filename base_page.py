from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def element_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def enter_to(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        try:
            return element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
