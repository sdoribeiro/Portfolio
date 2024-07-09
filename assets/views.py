import yfinance as vf
import decimal
# import pandas as pd
import IPython.display as display
from django.shortcuts import render

from .models import Trade, PortfolioComp, Asset

# Create your views here.
def index(request):

    class LocalAsset:
        def __init__(self, ticker, perc):
            self.ticker = ticker
            # using yfinance to get ticker data
            stock_obj = vf.Ticker(ticker)
            self.name = stock_obj.info['shortName']
            self.price = stock_obj.info['currentPrice']
            self.operations = []
            self.Mprice = 0
            self.QtdAsset = 0
            self.percRef = perc
            self.vlrInvestido = 0

        def add_opp(self, operation):
            self.operations.append(operation)
            # only calc average price in buy operation

            if operation.operator.factor == 1.0000: # buy
                # Calc average pri ce
                if self.Mprice == 0:
                    self.Mprice = round(operation.price + (operation.tax/operation.quantity),2)
                    self.QtdAsset = operation.quantity
                    self.vlrInvestido = self.vlrInvestido + (operation.price * operation.quantity)
                else:  #sell
                    self.Mprice = round(((self.Mprice * self.QtdAsset) + (operation.price * operation.quantity + operation.tax))/ (self.QtdAsset + operation.quantity),2)
                    self.QtdAsset = self.QtdAsset + operation.quantity
                    
            else:
                self.QtdAsset = self.QtdAsset - operation.quantity
                self.vlrInvestido = self.vlrInvestido - (operation.price * operation.quantity)

        def __str__(self):
                return f"LocalAsset class: Ticker {self.ticker} | Name {self.name} | Price: {self.price} | Perc: {self.percRef} | Mprice: {self.Mprice} | QtdAsset: {self.QtdAsset} | VlrInvestido: {self.vlrInvestido}"
        

    class LocalPortifolio:
        def __init__(self,name):
            self.name = name
            self.composicao = {}
            self.vlrTotal = 0

        def add_asset(self, asset):
            self.composicao[asset.ticker+"%REF"] = asset.percRef
            self.composicao[asset.ticker] = (asset.price * asset.QtdAsset)
            self.vlrTotal = self.vlrTotal + (asset.price * asset.QtdAsset)
    
        # Calc percentual do ativo em relacao ao patrimonio total
        def calc_perc(self):
            aux = {}
            for x in self.composicao.keys():
                
                # selecionar somente as chaves de referencia do asset padrao.
                if x[len(x)-2:len(x)] == "SA":
                    ticker = x[0:len(x)-3]
                    y = ticker+"%Calc"
                    aux[y]=decimal.Decimal(round((self.composicao[x]/self.vlrTotal)*100,2))
                    # Rec > 0 buy Rec <0 wait
                    aux[ticker+"Rec"] = self.composicao[ticker+".SA%REF"] - aux[y]
            for x in aux.keys():
                self.composicao[x]=round(aux[x],2)

        def show_data(self):
            aux = []
            for x in self.composicao.keys():
                if x[len(x)-2:len(x)] == "SA":
                    ticker = x[0:len(x)-3]
                    valor = self.composicao[x]
                    PercRef = self.composicao[x+"%REF"]
                    PercRec = self.composicao[ticker+"Rec"]
                    print (ticker + "|" + str(valor) + "|" + str(PercRef) + "|" + str(PercRec))
                    a = ticker + "|" + str(valor) + "|" + str(PercRef) + "|" + str(PercRec)
                    aux.append(a)
            return aux      
               
        def __str__(self):
            return f"Class Portifolio: {self.name} | {self.vlrTotal} | {self.composicao} "
        
    portfolio = PortfolioComp.objects.all()

    minhacarteira = LocalPortifolio("ribeiro")

    for item in portfolio:

        localAsset = LocalAsset(item.asset.ticker, item.percentage)
    
        trades = Trade.objects.filter(ticker = item.asset)
        for trade in trades:
            localAsset.add_opp(trade)
        minhacarteira.add_asset(localAsset)
    
    minhacarteira.calc_perc()

    return render(request, "assets/index.html", {
        "assets": minhacarteira.show_data(),
        "trades": Trade.objects.all()
    })