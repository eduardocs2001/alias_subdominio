from bs4 import BeautifulSoup
import requests

class alias_DNS:

    def __init__(self):
        self.dominio = input("Dominio:")      
        self.html = requests.get(f"https://crt.sh/?q={self.dominio}").content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.subdominio = []

    def tratativa(self):
        texto = self.soup.prettify().replace('<td>','#').replace('</td>','#').replace("\n",'').split('#')
        for linha in texto:
            info = linha.strip()
            if 'useall.com.br' in info:
                info_tratada = info.split(' ')
                self.subdominio.append(info_tratada[0])
            else:
                pass
        self.remove_repetidos()
        for x in self.subdominio:
            print(x)
        
    def remove_repetidos(self):
        l = []
        for i in self.subdominio:
            if i not in l:
                if self.dominio in i and '*' not in i:
                    l.append(i)
                else:
                    pass
        l.sort()
        self. subdominio = l






if __name__ == '__main__':
    dns = alias_DNS()
    dns.tratativa()