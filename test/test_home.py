
from helper.action import *
from POM.POM_Home import *
from helper.config import *


def test_baca_selengkapnya(openDriver):
    element_click(openDriver, bacaSelengkap_Btn)
    validasi_url(openDriver, url_anualReport)

def test_cancel(openDriver):
    element_click(openDriver, close_Btn)

def test_panah_kiri_kanan(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, panahKiri)
    element_click(openDriver, panahKanan)

def test_dropdown_pertanyaanHigo(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, dropDown_Btn)
    validate_is_display(openDriver, detail_Dropdown)
    element_click(openDriver, dropDown_Btn)

def test_footer_linkedinHigo(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, LinkedinIcon)
    validasi_url(openDriver, linkedinHigo)

def test_footer_FBHigo(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, FBIcon)
    validasi_url(openDriver, FbHigo)

def test_footer_IGHigo(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, IGIcon)
    validasi_url(openDriver, IGHigo)

def test_footer_XHigo(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, XIcon)
    validasi_url(openDriver, XHigo)

def test_footer_WiFiAdvertising(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, WiFiAdvertising_Footer)
    validasi_url(openDriver, WiFiAdvertising_Link)


def test_footer_HIGOSpot(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, HigoSpot_Footer)
    validasi_url(openDriver, HIGOSpot_Link)


def test_footer_IntegratedDigitalAgency(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, IntegratedDigital_footer)
    validasi_url(openDriver, Integrated_Link)


def test_footer_AboutUs(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, AboutUs_Footer)
    validasi_url(openDriver, AboutUs_Link)


def test_footer_Karir(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Karir_footer)
    validasi_url(openDriver, linkedinHigo)

def test_footer_Blog(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Blog_footer)
    validasi_url(openDriver, url_blogHigo)

def test_footer_TermsAndConditions(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Term_footer)
    validasi_url(openDriver, Term_Link)

def test_footer_PrivacyAndPolicy(openDriver):
    test_cancel(openDriver)
    element_click(openDriver, Privacy_footer)
    validasi_url(openDriver, Privacy_Link)
