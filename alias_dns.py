from bs4 import BeautifulSoup
import requests
import subprocess
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
    
    def consulta(self):
        for subdominio in self.subdominio:
            resultado = subprocess.getoutput(f'host -t cname {subdominio} | grep "alias"')
            if len(resultado) > 5:
                url = f'https://{((resultado.split("for"))[-1][0:-1]).strip()}/'
                print(f"Resultado: {resultado}\nAlias: {((resultado.split('for'))[-1][0:-1]).strip()}\nGet: {requests.get(url)}\n")
            else:
                pass
  
            






if __name__ == '__main__':
    dns = alias_DNS()
    dns.tratativa()
    dns.consulta()