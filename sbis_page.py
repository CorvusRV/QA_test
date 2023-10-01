from selenium.webdriver.common.by import By
from base_page import BasePage
from file_test import File

from transliterate import slugify
import time


class Locators:
    LOCATOR_CONTACTS = (By.XPATH, "//a[text() = 'Контакты']")
    LOCATOR_BANER = (By.XPATH, "//a[@title = 'tensor.ru']")
    LOCATOR_STRENGTH_IN_PEOPLE = (By.XPATH, '//p[contains(text(),"Сила в людях")]')
    LOCATOR_STRENGTH_IN_PEOPLE_DETAILS = (By.XPATH, "//div[p[text() = 'Сила в людях']]//a[text() = 'Подробнее']")
    LOCATOR_REGION = (By.XPATH, "//span[@class = 'sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_PARTNERS = (By.XPATH, "//div[@id = 'city-id-2']")
    LOCATOR_WORKING_PHOTOS = (By.XPATH, '//div[h2[text() = "Работаем"]]//following-sibling::div//img')
    LOCATOR_REGION_SELECTION = (By.XPATH, f"//span[contains(text(),'Камчатский край')]")  # добавить возможность выбора региона
    LOCATOR_SBIS_DOWNLOAD = (By.XPATH, '//a[text() = "Скачать СБИС"]')
    LOCATOR_SBIS_PLUGIN = (By.XPATH, '//div[text() = "СБИС Плагин"]')
    LOCATOR_WEB_INSTALLER = (By.XPATH, '//div[h3[text() = "Веб-установщик "]]//following-sibling::div//a')


class SbisPage(BasePage):
    file = None

    def enter_contacts(self):
        return self.enter_to(Locators.LOCATOR_CONTACTS)

    def enter_baner(self):
        return self.enter_to(Locators.LOCATOR_BANER)

    def enter_download_sbis(self):
        return self.enter_to(Locators.LOCATOR_SBIS_DOWNLOAD)

    def enter_sbis_plugin(self):
        return self.enter_to(Locators.LOCATOR_SBIS_PLUGIN)

    def enter_block_sip(self):
        return self.enter_to(Locators.LOCATOR_STRENGTH_IN_PEOPLE_DETAILS)

    def get_region(self):
        return self.find_element(Locators.LOCATOR_REGION).text

    def get_partners(self):
        return self.find_element(Locators.LOCATOR_PARTNERS).text

    def get_block_sip(self):
        return self.find_element(Locators.LOCATOR_STRENGTH_IN_PEOPLE)

    def change_region(self):
        self.find_element(Locators.LOCATOR_REGION).click()
        self.find_element(Locators.LOCATOR_REGION_SELECTION).click()
        time.sleep(1)

    def verification_url(self, text):
        return slugify(text) in self.get_url()

    def verification_title(self, text):
        return text in self.get_title()

    def get_web_installer(self):
        return self.find_element(Locators.LOCATOR_WEB_INSTALLER).text

    def attribute_comparison(self, attribute):
        elements = self.find_elements(Locators.LOCATOR_WORKING_PHOTOS)
        for i in range(len(elements)-1):
            if self.element_attribute(elements[i], attribute) != self.element_attribute(elements[i+1], attribute):
                return False
        return True

    def download_file(self):
        element = self.find_element(Locators.LOCATOR_WEB_INSTALLER)
        href_file = self.element_attribute(element, "href")
        self.file = File(href_file)
        status = self.file.download()
        if status:
            size = self.file.file_size()
            return str(size)
        else:
            return '0'

    def remove_file(self):
        self.file.remove_file()

