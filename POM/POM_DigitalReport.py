from selenium.webdriver.common.by import By

Kanal_Digital = [By.XPATH, '(//a[span[starts-with(text(),"Digital Reports")]])[1]']
btn_DownloadFullReport = [By.XPATH, "(//button[.='Download Full Report'])[1]"]
btn_Download = [By.XPATH, "(//button[@type='submit'])[2]"]

fill_FirstName = [By.XPATH, "(//input[@placeholder='First Name'])[2]"]
fill_LastName = [By.XPATH, "(//input[@placeholder='Last Name'])[2]"]
fill_Email = [By.XPATH, "(//input[@placeholder='Email'])[2]"]
fill_Phone = [By.XPATH, "(//input[@placeholder='Phone Number'])[2]"]
fill_Company = [By.XPATH, "(//input[@placeholder='Company Name'])[2]"]
fill_JobTitle = [By.XPATH, "(//input[@placeholder='Job Title'])[2]"]

WaIcon = [By.XPATH, '(//img[@alt="Share to Whatsapp"])[2]']
shareIcon = [By.XPATH, "(//button[@class ='bg-transparent'])[2]"]

sumber_link = [By.XPATH, "(//li[@class='text-primary'])[1]"]

