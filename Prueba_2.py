import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def show_start_popup():
    popup = tk.Tk()
    popup.title("Inicio del Test: Prueba 2")
    label = tk.Label(popup, text="¡El test 2 está por comenzar!")
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

privacy_policy_link = driver.find_element(By.XPATH, "//a[@href='/privacy-policy']")

privacy_policy_link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2")))

sections = ["WHAT INFORMATION DO WE COLLECT?", "HOW DO WE PROCESS YOUR INFORMATION?",
            "WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR PERSONAL INFORMATION?",
            "WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?",
            "DO WE USE COOKIES AND OTHER TRACKING TECHNOLOGIES?", "HOW LONG DO WE KEEP YOUR INFORMATION?",
            "HOW DO WE KEEP YOUR INFORMATION SAFE?", "DO WE COLLECT INFORMATION FROM MINORS?",
            "WHAT ARE YOUR PRIVACY RIGHTS?", "CONTROLS FOR DO-NOT-TRACK FEATURES",
            "DO UNITED STATES RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?",
            "DO OTHER REGIONS HAVE SPECIFIC PRIVACY RIGHTS?", "DO WE MAKE UPDATES TO THIS NOTICE?",
            "HOW CAN YOU CONTACT US ABOUT THIS NOTICE?", "HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?"]

compliance_result = ""

for section in sections:
    try:
        section_element = driver.find_element(By.XPATH, f"//h2[contains(text(),'{section}')]")
        compliance_result += f"Sección '{section}' presente en la página de la Política de Privacidad."
    except Exception as e:
        compliance_result += f"No se encontró la sección '{section}' en la página de la Política de Privacidad."
    finally:
        compliance_result += "\n"

show_result_popup(compliance_result)

driver.quit()
