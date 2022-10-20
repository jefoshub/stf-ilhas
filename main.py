##############################################
##      MÓDULO 1 - RASPAGEM DE DADOS        ##
##############################################

# UFRRJ - MESTRADO INTERDISCIPLINAR EM HUMANIDADES DIGITAIS
# Jeferson dos Santos Antunes Huaracha

# orientadores: Prof. Dr. Leandro Guimarães Marques Alvim / Prof. Dr. Rodrigo de Souza Tavares

# Última verificação do funcionamento: Outubro/22
# Mudanças estruturais na página do STF poderão demandar alterações futuras neste código.

# ATENÇÃO: Baixe a versão adequada do chromedriver.exe de acordo com a versão do browser instalado no S.O. e
# Substitua-o no diretório raiz

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Escolhendo classe de acórdãos a serem processados (ADIs ou HCs)
choice = '0'
while choice == '0':
    print("Escolha a classe de acórdãos a ser processada")
    print("1 - Ações Diretas de Inconstitucionalidade ")
    print("2 – Habeas Corpus")
    print("3 - Sair")

    choice = input("Digite o número e pressione ENTER : ")

    if choice == "1":
        print("Processando ADIs")

    elif choice == "2":
        print("Processando HCs")

    elif choice == "3":
        print("Finalizando")
        exit()

    else:
        print("opção Inválida")

# criando o dataframe
dataset = pd.DataFrame(columns=['HC', 'UF', 'RELATOR', 'DATA-JULGAMENTO','PARTES', 'EMENTA','DECISÃO','URL'])

chrome_options = Options()

#Pleno#url = 'https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&processo_classe_processual_unificada_classe_sigla=HC&julgamento_data=01011995-&orgao_julgador=Tribunal%20Pleno&page=1&pageSize=250&queryString=hc&sort=date&sortBy=desc'
#ADIs 2016-17
if choice == '1':
    url = 'https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&processo_classe_processual_unificada_classe_sigla=ADI&julgamento_data=01012011-31122022&page=1&pageSize=250&queryString=adi&sort=date&sortBy=desc'

elif choice =='2':
    url = 'https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&processo_classe_processual_unificada_classe_sigla=HC&julgamento_data=01012011-31122022&orgao_julgador=Tribunal%20Pleno&page=1&pageSize=10&queryString=hc&sort=_score&sortBy=desc'

print("Entre no link e verifique o nº total de registros:")
print('')
print(url)
total = input("Informe o número total de registros a serem acessados: ")
total = int(total)


browser = Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
browser.get(url)


time.sleep(6)
main = browser.find_element_by_tag_name('body')
main = main.find_element_by_tag_name('app-root')
main = main.find_element_by_tag_name('app-home')
main = main.find_element_by_tag_name('main')

main_id = main.find_element_by_id('scrollId')
main_class = main_id.find_elements_by_id('result-index-0')
hc_link = main_class[0].find_element_by_tag_name('a')
hc_link.click()

for c in range(0,total):
    print('Ação: ',c)
    try:
        # buscando conteudo
        if c % 100 == 0:
            time.sleep(10)
        time.sleep(6)
        cont_div = browser.find_element_by_id('scrollId')
        cont_div = cont_div.find_element_by_tag_name('mat-tab-group')
        cont_div = cont_div.find_element_by_tag_name('mat-tab-body')
        cont = cont_div.find_elements_by_tag_name('div')
        conteudo = (cont[0].text).split('\n')


        hc_uf  = conteudo[0].split('/')
        hc = hc_uf[0]
        uf = hc_uf[1]
        relator = conteudo[2]
        data_julgamento = conteudo[3]
        #data_publicacao = conteudo[4]
        #publicacao = conteudo[conteudo.index('Publicação')+1] +' '+ conteudo[conteudo.index('Publicação')+2]
        partes = ' | '.join(conteudo[conteudo.index('Partes')+1:conteudo.index('Ementa')])
        ementa = conteudo[conteudo.index('Ementa') + 1]
        decisao = conteudo[conteudo.index('Decisão') + 1]
        url = browser.current_url

        data = []
        data.append(hc)
        print(hc)
        data.append(uf[1:3])
        print(uf[1:3])
        data.append(relator[17:])
        data.append(data_julgamento[12:])
        #data.append(data_publicacao)
        #data.append(publicacao)
        data.append(partes)
        data.append(ementa)
        data.append(decisao)
        data.append(url)

        # colocando os dados no df
        dataset.loc[len(dataset)] = data

        if choice == '1':
            dataset.to_csv('scraped-ADIs.csv')

        else:
            dataset.to_csv('scraped-HCs.csv')

        # proxima pagina
        pagination = browser.find_element_by_tag_name('paginator')
        pagination_ul = pagination.find_element_by_tag_name('ul')
        pagination_ul_link = pagination_ul.find_elements_by_class_name('pagination-icon')
        next = pagination_ul_link[2]
        next.click()
        time.sleep(1)

    except Exception as e:
        print(e,c)
        input(f'Parou na pag.{c}, acórdõ {hc} clique em voltar no browser, selecione a página, volte para esta janela e pressione ENTER')

browser.quit()

print('Concluído!')
print('Dataset (csv) Salvo no diretório raíz deste módulo.')

# Código desenvolvido para os fins da pesquisa
# Ilhas, Arquipélagos ou Continentes? Uma Análise Sobre a Geografia do Supremo Tribunal Federal

# Com a Integração Selenium + Chrome, esta aplicação em Python navega automaticamente pelas páginas do
# motor de busca jurisprudência do STF, baixando os dados de cada acórdão.

# Este módulo foi projetado para suprir a falta de campos de interesse no arquivo csv exportado da própria página.

# Agradecimento ao Gabriel Marcial de Paiva (UERJ) pelo trinamento e auxílio na produção deste módulo.

