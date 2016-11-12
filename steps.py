# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
@step(u'Abro el navegador y entro a facebook')
def abro_el_navegador_y_entro_a_facebook(step):
    world.driver= webdriver.Chrome(os.getcwd()+"/chromedriver")
    #world.driver=webdriver.Firefox()
    world.driver.get("https://www.facebook.com/")


@step(u'Dado que tengo el usuario "([^"]*)" y contrasenia "([^"]*)"')
def dado_que_tengo_el_usuario_group1_y_contrasenia_group2(step, email, contra):

    campoUser= world.driver.find_element_by_name('email')
    campoPass=world.driver.find_element_by_name('pass')
    campoUser.send_keys(email)
    campoPass.send_keys(contra)


@step(u'Presiono el boton Log in')
def presiono_el_boton_log_in(step):
    boton=world.driver.find_element_by_xpath('//*[@id="u_0_n"]')
    boton.click()
    time.sleep(3)
@step(u'Y entro al sistema donde me indica que mi usuario es "([^"]*)"')
def y_entro_al_sistema(step, texto_esperado):
    texto=world.driver.find_element_by_xpath('//*[@id="u_0_2"]/div[1]/div[1]/div/a/span')
    time.sleep(5)
    assert texto.text==texto_esperado, "El texto esperado "+texto_esperado+" no es igual a "+texto.text



@step(u'Le doy click en publicar')
def le_doy_click_en_publicar(step):

    #boton = world.driver.find_element_by_css_selector('span.f_click')
    boton=world.driver.find_element_by_xpath('// *[ @ id = "u_0_2"] / div[1] / div[1] / div / a / span')
    boton.click()
    time.sleep(5)


@step(u'Ingreso la frase "([^"]*)"')
def ingreso_la_frase_group1(step, video):
    textArea = world.driver.find_element_by_class_name('_4h98')
    textArea.send_keys(video+Keys.RETURN)
    time.sleep(5)



@step(u'Y publico el video')
def y_publico_el_video(step):
    elem = world.driver.find_element_by_css_selector(".selected")
    #elem = world.driver.find_element_by_tag_name('button')
    elem.click()
    time.sleep(5)
    world.driver.quit()





