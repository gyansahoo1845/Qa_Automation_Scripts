import logging

import pytest
from appium import webdriver

driver = None


# Configuration class - Browser stack configuration, Page Screenshot configuration

@pytest.fixture(scope="class")
def setup(request):
    global driver
    userName = "gyansahoo_n6Cjya"
    accessKey = "xDutUy4YZPmWvsk7ugo4"

    desired_caps = {
        "build": "Vessel Mobile Automation",
        "device": "iPhone 12 Mini",
        "os_version": "14",
        "app": "bs://b356b9c42d6802705f92eab56dac507947877354"
    }

    driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
                              desired_caps)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
