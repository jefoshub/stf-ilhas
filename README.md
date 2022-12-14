# stf-ilhas
Módulo 1 Raspagem de Dados


----------------------------------------------------------------
UFRRJ - MESTRADO INTERDISCIPLINAR EM HUMANIDADES DIGITAIS
Jeferson dos Santos Antunes Huaracha

Orientadores: Prof. Dr. Leandro Guimarães Marques Alvim 
              Prof. Dr. Rodrigo de Souza Tavares

Última verificação do funcionamento: Outubro/22
----------------------------------------------------------------

Nota: Mudanças estruturais na página do STF poderão demandar alterações futuras neste código.

ATENÇÃO: Baixe a versão adequada do chromedriver.exe de acordo com a versão do browser instalado no S.O. e 
Substitua-o no diretório raiz

Com a Integração Selenium + Chrome, esta aplicação em Python navega automaticamente pelas páginas do motor de busca jurisprudência do STF, baixando os dados de cada acórdão. 

Esse módulo foi projetado para suprir a falta de campos de interesse no arquivo csv exportado da própria página.

As raspagens de dados de acórdãos das classes processuais ADIs e HCs são efetuadas de forma separada. 
Durante a execução do programa é requisitada a informação de qual classe deverá se processada.

Eventualmente  a raspagem de dados é interrompida por falta de resposta do site. Nesses casos é requisitado que o usuário clique manualmente na página do próximo acórdão a ser examinado, no navegador (Chrome) que é utilizado através do Selenium. 

Os dados extraídos através deste módulo deverão ser mesclados aos dados de arquivos CSV baixados diretamente do site jurisprudência do STF. 

Utilize os seguintes links para baixá-los:

ADIs: https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&processo_classe_processual_unificada_classe_sigla=ADI&julgamento_data=01012011-31122022&page=1&pageSize=250&queryString=adi&sort=date&sortBy=desc

HCs: 
https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&processo_classe_processual_unificada_classe_sigla=HC&julgamento_data=01012011-31122022&orgao_julgador=Tribunal%20Pleno&page=1&pageSize=10&queryString=hc&sort=_score&sortBy=desc

