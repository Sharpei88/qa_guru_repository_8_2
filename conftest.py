import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open("https://www.google.com/")
    browser.driver.set_window_size(1920, 800)
    yield
    browser.quit()