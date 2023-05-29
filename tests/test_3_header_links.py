from pages.header_links import CheckHeaderLinks



class TestCheckHeaderLinks():

    def test_click_header_links_waitfor_correct_url(self, driver, get_the_page):
        CheckHeaderLinks(driver).click_scooter_link()

    def test_click_header_links_waitfor_correct_url_2(self, driver, get_the_page):
        CheckHeaderLinks(driver).click_yandex_link()