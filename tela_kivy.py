# importar APP, builder (gui)
# criar aplicativo
# criar funcao build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela_kivy.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    #executa ao iniciar
    def on_start(self):
        self.root.ids["dolar"].text = f"Dólar R$ {self.pegar_cotacao('USD')} "
        self.root.ids["euro"].text = f"Euro R$ {self.pegar_cotacao('EUR')} "
        self.root.ids["btc"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')} "
        self.root.ids["ether"].text = f"Etherium R$ {self.pegar_cotacao('ETH')} "
        # ver json
        self.pegar_cotacao("USD")
        
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        # retorna como json
        #print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
        
        
        
        
    

MeuAplicativo().run()