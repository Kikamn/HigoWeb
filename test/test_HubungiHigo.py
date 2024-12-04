from test.test_home import test_cancel
from helper.action import *
from POM.POM_HubunginHigo import *

def test_blank_form(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_click(openDriver, btn_submit)

def test_fill_FullName(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")

def test_fill_Email(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")
    element_input(openDriver, Fill_Email, "kika@gmail.com")

def test_fill_PhoneNumber(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")
    element_input(openDriver, Fill_Email, "kika@gmail.com")
    #element_input(openDriver, test_fill_PhoneNumber, "+6285451522151")

def test_fill_Company(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")
    element_input(openDriver, Fill_Email, "kika@gmail.com")
    #element_input(openDriver, test_fill_PhoneNumber, "+6254365657")
    element_input(openDriver, Fil_Company, "jaya jaya")

def test_fill_Layanan(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")
    element_input(openDriver, Fill_Email, "kika@gmail.com")
    #element_input(openDriver, test_fill_PhoneNumber, "021214541454")
    element_input(openDriver, Fil_Company, "jaya jaya")
    element_click(openDriver, dropDown)
    element_click(openDriver, layanan_btn)

def test_fill_Pesan(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Kanal_HubungiKami)
    element_input(openDriver, Fill_FullName, "Rizkika")
    element_input(openDriver, Fill_Email, "kika@gmail.com")
    #element_input(openDriver, test_fill_PhoneNumber, "021214541454")
    element_input(openDriver, Fil_Company, "jaya jaya")
    element_click(openDriver, dropDown)
    element_click(openDriver, layanan_btn)
    element_input(openDriver, Fill_Pesan, "Coba coba")
