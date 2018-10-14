import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(paginas, profundidade):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    for i in range(profundidade):
        novas_paginas = set()
        #valores repetidos
        for pagina in paginas:
            http = urllib3.PoolManager()
            try:
                dados_pagina = http.request('GET', pagina)
            except:
                print("Erro ao abrir a página" + pagina)
                continue
                
            sopa = BeautifulSoup(dados_pagina.data, "lxml")
            links = sopa.find_all('a')
            contador = 1
            for link in links:
                if ('href' in link.attrs):
                    url = urljoin(pagina, str(link.get('href')))
                    if url.find("''") != -1:
                        continue
                    
                    url = url.split('#')[0]
                    
                    if url[0:4] == 'http':
                        novas_paginas.add(url)
                                    
                    contador = contador + 1
            paginas = novas_paginas
            print(novas_paginas)
        print(contador)

lista_paginas = ['https://pt.wikipedia.org/wiki/Avengers:_Infinity_War']
crawl(lista_paginas, 2)
