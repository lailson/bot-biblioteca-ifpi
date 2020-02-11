from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver = webdriver.Firefox()
driver.get("http://sardes.ifpi.edu.br/pergamum/mobile/idiomas.php")
assert "Languages" in driver.title

pt = driver.find_element_by_link_text("Português")
pt.click()

driver.get("http://sardes.ifpi.edu.br/pergamum/mobile/login.php?flag=renovacao.php")

usuario = driver.find_element_by_name("login")
usuario.send_keys("2081976")
senha = driver.find_element_by_name("password")
senha.send_keys("2081976")
logar = driver.find_element_by_name("button")
logar.click()

livros = driver.find_elements_by_class_name("li")


for livro in livros:
    
    livro.click()
    driver.find_element_by_name("Voltar").click()

