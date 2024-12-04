from selenium.webdriver.common.by import By

from test.test_home import test_cancel

def test_layananHigo(openDriver):
    test_cancel(openDriver)
    openDriver.find_element(By.XPATH, "/html/body/header/div/div/nav/ul/li[2]/label[2]/div/svg[1]").click()