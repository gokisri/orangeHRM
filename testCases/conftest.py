import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome/firefox)")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})
    config._metadata['Project Name'] = 'Capstone Project 1'
    config._metadata['Module Name'] = 'Employees'
    config._metadata['Tester'] = 'Gokilavijay'

# Hook for modifying/deleting environment info in the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
