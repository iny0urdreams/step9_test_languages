import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LANGUAGES = ['ru', 'eng', 'es', 'fr']


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language:ru or eng")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        if language in LANGUAGES:
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            print(f"\nstart chrome browser({language}) for test..")
            browser = webdriver.Chrome(options=options)
        else:
            raise pytest.UsageError('--language should be eng or ru or es or fr')
    elif browser_name == "firefox":
        if language in LANGUAGES:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            print(f"\nstart firefox browser({language}) for test..")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError('--language should be eng or ru or es or fr')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
