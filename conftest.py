import pytest
from selenium import webdriver
from utils.config import Config

@pytest.fixture(scope="function")
def driver():
    if Config.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox()

    elif Config.BROWSER == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")

    yield driver
    driver.quit()
