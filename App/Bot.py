from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurar o WebDriver
driver = webdriver.Chrome(executable_path='CAMINHO_PARA_SEU_CHROMEDRIVER')

# Abrir o YouTube e fazer login
driver.get("https://www.youtube.com")
time.sleep(3)  # Esperar a página carregar

# Fazer login
login_button = driver.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/a')
login_button.click()
time.sleep(2)

# Inserir email
email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys("SEU_EMAIL")
email_field.send_keys(Keys.RETURN)
time.sleep(2)

# Inserir senha
password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys("SUA_SENHA")
password_field.send_keys(Keys.RETURN)
time.sleep(5)  # Esperar o login completar

# Navegar para a página de inscrições
driver.get("https://www.youtube.com/feed/channels")
time.sleep(5)

# Loop para desinscrever-se de todos os canais
unsubscribe_buttons = driver.find_elements(By.XPATH, '//*[@aria-label="Unsubscribe"]')
for button in unsubscribe_buttons:
    button.click()
    time.sleep(1)  # Esperar um pouco entre as ações

# Fechar o navegador
driver.quit()