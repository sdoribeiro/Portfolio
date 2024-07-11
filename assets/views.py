import yfinance as vf
import decimal
import pandas as pd

from IPython.display import display
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
            # final use of yfinance
            self.trades = []
            self.Mprice = 0
            self.QtdAsset = 0
            self.percRef = perc
            self.vlrInvestido = 0

        def add_opp(self, operation):
            self.trades.append(operation)
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
            self.vlrTotal = 0
            self.dicionario = {"ticker": [],
                               "valor": [],
                               "percRef": [],
                               "percCor": []
                            }


        def add_asset(self, asset):
            self.vlrTotal = self.vlrTotal + (asset.price * asset.QtdAsset)
            self.dicionario["ticker"].append(asset.ticker)
            self.dicionario["valor"].append(round(asset.price * asset.QtdAsset,2))
            self.dicionario["percRef"].append(round(asset.percRef,2))          

        # Calc percentual do ativo em relacao ao patrimonio total
        def calc_perc(self):

            for x in self.dicionario["valor"]:
                self.dicionario["percCor"].append(round(x/self.vlrTotal*100,2))

        def show_data(self):
            aux = []
            for x in self.dicionario.keys():
                aux.append(self.dicionario[x])
            return aux      
               
        def __str__(self):
            return f"Class Portifolio: {self.name} | {self.vlrTotal} | {self.dicionario} "
        
    portfolio = PortfolioComp.objects.all()

    minhacarteira = LocalPortifolio("ribeiro")

    for item in portfolio:

        localAsset = LocalAsset(item.asset.ticker, item.percentage)
    
        trades = Trade.objects.filter(ticker = item.asset)
        for trade in trades:
            localAsset.add_opp(trade)
        minhacarteira.add_asset(localAsset)
    
    minhacarteira.calc_perc()
    
    df = pd.DataFrame(minhacarteira.dicionario)
    display(df)    

    return render(request, "assets/index.html", {
        "assets": minhacarteira.show_data(),
        "trades": Trade.objects.all()
    })