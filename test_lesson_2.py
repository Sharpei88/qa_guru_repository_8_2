from selene import browser, be, have
from selene.support.shared.jquery_style import s

def test_google_search_selene(open_browser):
    s('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))

def test_google_search_no_results(open_browser):
    random_query = 'xhjghjvjkdfxfhcfhxgcfgxhdfx'
    s('[name="q"]').should(be.blank).type(random_query).press_enter()
    s('#center_col').should(have.text("По запросу xhjghjvjkdfxfhcfhxgcfgxhdfx ничего не найдено."))