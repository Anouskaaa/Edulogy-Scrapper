from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)



edulog_user = input("Masukan Educode Username : ")
edulog_pass = input("Masukan Educode Password : ")
driver.get("https://siswa.edulogy.id")

username_input = driver.find_element(By.NAME, "username")

username_input.send_keys(edulog_user)

password_input = driver.find_element(By.NAME, "password")

password_input.send_keys(edulog_pass)


password_input.send_keys(Keys.ENTER)

driver.implicitly_wait(5)

if "Dashboard" in driver.page_source:
    nama = driver.find_element(By.CLASS_NAME, "name")
    name_text = nama.text.strip()
    span_elements = driver.find_elements(By.CLASS_NAME, "text-center")
    span_texts = [span.text.strip() for span in span_elements]
    print("NAMA : ", name_text)
    print("Sekolah:", span_texts[1])
    print("Tahun Ajaran:", span_texts[2])
    

    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    driver.save_screenshot("screenshot_dashboard.png")
    driver.get("https://siswa.edulogy.id/setting/profile")
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    # driver.save_screenshot(path)  # has scrollbar
    driver.save_screenshot("screenshot_profile.png")
    #driver.find_element(By.TAG_NAME, 'body').screenshot("screenshot.png")  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])
    #driver.save_screenshot("screenshot.png")

else:
    print("User Tidak Ditemukan")

f = open("data_educode.txt", "a")
f.write(f"\nNAMA : {name_text}\nSekolah : {span_texts[1]}\nTahun Ajaran: {span_texts[2]}\nEducode : {edulog_user}\n###########################")
f.close()
print("Saved To Data...")
input("Tekan Enter untuk menutup browser...")
driver.quit()