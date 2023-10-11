from pages.registration_page import Registration



class TestCheckHeaderLinks():

    def test_click_header_links_waitfor_correct_url_1(self, get_driver_and_page, go_to_registration_page):
        reg_one = Registration(get_driver_and_page)
        reg_one.click_scooter_link()
        assert get_driver_and_page.current_url == 'https://qa-scooter.praktikum-services.ru/'


