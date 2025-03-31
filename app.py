#repita passos manuais usando codigo
#1 - entrar no site - https://clone-olx-devaprender.netlify.app/
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


driver = webdriver.Chrome()
driver.get('https://clone-olx-devaprender.netlify.app/')

sleep(5)

#2 - anotar o nome do 1º produto;
produtos = driver.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")


#3 - anotar o preço do 1º produto;

precos = driver.find_elements(By.XPATH,"//span[@class='text-2xl font-bold text-gray-900']")


#4 - repetir para todos os produtos da pasta (fazer laço de repetição); 

for produto, preco in zip(produtos,precos):
    with open('precos.csv','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{preco.text}{os.linesep}')
input('')




#4 - repetir para todos os produtos da pasta;
#5 - guardar informações em arquivo de texto (CSV);