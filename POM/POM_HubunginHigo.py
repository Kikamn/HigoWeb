from selenium.webdriver.common.by import By

Kanal_HubungiKami = [By.XPATH, '(//a[span[starts-with(text(),"Hubungi HIGO")]])[1]']

Fill_FullName = [By.NAME, "fullName"]
Fill_Email = [By.NAME, "email"]
Fil_Company = [By.NAME, "companyName"]
Fill_Phone = [By.NAME, "phoneNumber"]
dropDown = [By.XPATH, "//select[@name='service']"]
layanan_btn = [By.XPATH, "//*[@value='Higospot']"]
Fill_Pesan = [By.NAME, "message"]

btn_submit = [By.XPATH, "//button[@type='submit']"]

