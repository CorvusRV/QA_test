import pytest
from sbis_page import SbisPage


def test_two(browser):
    main_page = SbisPage(browser)
    main_page.go_to_site()
    main_page.enter_contacts()
    my_region = main_page.get_region()
    assert my_region == 'Ярославская обл.'
    my_partners = main_page.get_partners()
    assert my_partners
    main_page.change_region()
    new_region = main_page.get_region()
    new_partners = main_page.get_partners()
    assert new_region == 'Камчатский край'
    assert main_page.verification_url(new_region)
    assert main_page.verification_title(new_region)
    assert my_partners != new_partners
