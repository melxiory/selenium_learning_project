import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = webdriver.Chrome()
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    #else:
    #    raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def link(request):
    language = request.config.getoption("language")
    if language:
        print("\nstart language for test..")
        link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    elif language == "":
        print("\nstart default for test..")
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    else:
        raise pytest.UsageError("--language should be re,en,fr or other, Default=ru")
    yield link
