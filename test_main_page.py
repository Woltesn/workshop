from .pages.main_page import MainPage
from .pages.clinic_booking import ClicnicBooking
from  .pages.accomadation_reject_approve import AccommodationRejectAccept
from .pages.accommodation_booking import AccommodationBooking

def test_guest_can_go_to_login_page(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.from_main_page_to_booking_list()          # выполняем метод страницы - переходим на страницу логина


def test_book_driver(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/countries/vu/locations/357/facilities/139/form/"
    page = MainPage(browser, link)
    page.open()
    page.fill_in_all_fields_driver()

def test_book_accommodation(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/countries/vu/locations/357/accommodations/434/form/"
    page = MainPage(browser, link)
    page.open()
    page.fill_in_all_fields_accommodation()

def test_book_clinic(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/countries/it/locations/88/facilities/65/form/"
    page = ClicnicBooking(browser, link)
    page.open()
    page.fill_in_all_fields_clinic()

def test_book_accommodation(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/countries/vu/locations/357/accommodations/434/form/"
    page = AccommodationBooking(browser, link)
    page.open()
    page.fill_in_all_fields_accommodation()

def test_accept_reject_accomodation(browser):
    link = "https://dev.humanitarianbooking.wfp.org/en/secure/office/locations/434/"
    page = AccommodationRejectAccept(browser, link)
    page.open()
    page.accommodation_accept()


