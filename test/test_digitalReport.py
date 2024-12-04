
from test.test_home import test_cancel
from helper.action import *
from POM.POM_DigitalReport import *
def test_digitalReport(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_Digital)
    element_click(openDriver, btn_DownloadFullReport)

def test_blank_form(openDriver):
    test_digitalReport(openDriver)
    element_click(openDriver, btn_Download)

def test_input_firstName(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_click(openDriver, btn_Download)
    #openDriver.find_element(By.XPATH, "(//img[@alt='Share to Whatsapp'])[2]").click()

def test_input_LastName(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_input(openDriver, fill_LastName, "Mulya Ningsih")
    element_click(openDriver, btn_Download)

def test_input_Email(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_input(openDriver, fill_LastName, "Mulya Ningsih")
    element_input(openDriver, fill_Email, "kika@gmail.com")
    element_click(openDriver, btn_Download)

def test_input_Phone(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_input(openDriver, fill_LastName, "Mulya Ningsih")
    element_input(openDriver, fill_Email, "kika@gmail.com")
    element_input(openDriver, fill_Phone, "0887867687878")
    element_click(openDriver, btn_Download)

def test_input_CompanyName(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_input(openDriver, fill_LastName, "Mulya Ningsih")
    element_input(openDriver, fill_Email, "kika@gmail.com")
    element_input(openDriver, fill_Phone, "0887867687878")
    element_input(openDriver, fill_Company, "Jaya jaya")
    element_click(openDriver, btn_Download)

def test_input_JobTitle(openDriver):
    test_digitalReport(openDriver)
    element_input(openDriver, fill_FirstName, "Rizkika")
    element_input(openDriver, fill_LastName, "Mulya Ningsih")
    element_input(openDriver, fill_Email, "kika@gmail.com")
    element_input(openDriver, fill_Phone, "0887867687878")
    element_input(openDriver, fill_Company, "Jaya jaya")
    element_input(openDriver, fill_JobTitle, "Qa")
    element_click(openDriver, btn_Download)

def test_share_Wa (openDriver):
    test_digitalReport(openDriver)
    element_click(openDriver, WaIcon)

def test_share (openDriver):
    test_digitalReport(openDriver)
    element_click(openDriver, shareIcon)

def test_sumber(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_Digital)
    element_click(openDriver, sumber_link)