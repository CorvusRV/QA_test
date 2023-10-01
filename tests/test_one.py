import pytest
from sbis_page import SbisPage


def test_one(browser):
    main_page = SbisPage(browser)
    main_page.go_to_site()
    main_page.enter_contacts()
    main_page.enter_baner()
    main_page.switch_window()
    assert main_page.get_block_sip()
    main_page.enter_block_sip()
    assert main_page.get_url() == 'https://tensor.ru/about'
    assert main_page.attribute_comparison('height')
    assert main_page.attribute_comparison('width')
