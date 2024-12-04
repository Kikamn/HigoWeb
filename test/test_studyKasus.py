from selenium.webdriver.common.by import By
from POM.POM_StudyKasus import *
from helper.action import *
from test.test_home import test_cancel

def test_studyKasus(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_StudyKasus)

def test_HigoSpot(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_StudyKasus)
    element_click(openDriver, HigoSpot)
    validate_is_display(openDriver, KintaroSushiImg)

def test_WiFiAdvertising(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_StudyKasus)
    element_click(openDriver, WiFiAdvertising)
    validate_is_display(openDriver, HomeCreditImg)

def test_All(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_StudyKasus)
    element_click(openDriver, All)
    validate_is_display(openDriver, KintaroSushiImg)

def test_detail_product(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_StudyKasus)
    element_click(openDriver, WiFiAdvertising)
    element_click(openDriver, HomeCreditImg)
