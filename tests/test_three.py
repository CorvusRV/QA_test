import pytest
from sbis_page import SbisPage


def test_three(browser):
    main_page = SbisPage(browser)
    main_page.go_to_site()
    main_page.enter_download_sbis()
    main_page.enter_sbis_plugin()
    file_size = main_page.download_file()
    assert file_size in main_page.get_web_installer()
    main_page.remove_file()
