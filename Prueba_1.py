import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def show_start_popup():
    popup = tk.Tk()
    popup.title("Inicio del Test: Prueba 1")
    label = tk.Label(popup, text="¡El test 1 está por comenzar!")
    label.pack(padx=10, pady=10)
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10)
    popup.mainloop()

def show_result_popup(result):
    popup = tk.Tk()
    popup.title("Resultado del Test")
    label = tk.Label(popup, text=result)
    label.pack(padx=10, pady=10)
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10)
    popup.mainloop()

driver = webdriver.Chrome()

driver.get("http://localhost:4200/login")

show_start_popup()

register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
register_link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

compliance_result = ""

try:
    consent_checkbox = driver.find_element(By.ID, "consentimiento")
    compliance_result += "Checkbox de consentimiento presente.\n"
except Exception as e:
    compliance_result += "Checkbox de consentimiento no encontrado.\n"

try:
    privacy_policy_link = driver.find_element(By.XPATH, "//a[@href='/privacy-policy']")
    compliance_result += "Link a la política de privacidad presente."
except Exception as e:
    compliance_result += "Link a la política de privacidad no encontrado."

show_result_popup(compliance_result)

driver.quit()
