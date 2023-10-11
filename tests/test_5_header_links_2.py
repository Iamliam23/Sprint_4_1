from pages.main_page_0 import MainPageQaScooter



class TestHeaderLinks():

    def test_click_header_links_waitfor_correct_url_2(self, get_driver_and_page):
        reg_two = MainPageQaScooter(get_driver_and_page)
        reg_two.click_yandex_link()
        assert get_driver_and_page.current_url == 'https://dzen.ru/?yredirect=true'


