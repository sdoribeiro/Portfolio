# import yfinance as yf
import datetime

from .models import Asset

# Automacao da gestao de uma carteira de investimentos com base nos percentuais de alocacao pre estabelecidos
# e ativos selecionados.

class LocalAsset:
    def __init__(self, ticker, perc):
        self.ticker = ticker
        # using yfinance to get ticker data
        stock_obj =ticker # yf.Ticker(ticker)
        self.name = "name" #stock_obj.info['shortName']
        self.price = 50.0 # stock_obj.info['currentPrice']
        self.operations = []
        self.Mprice = 0
        self.QtdAsset = 0
        self.percRef = perc

    def add_opp(self, operation):
        self.operations.append(operation)
        # only calc average price in buy operation
        if operation.ope > 0: # buy
           # Calc average price
           if self.Mprice == 0:
              self.Mprice = round(operation.price + (operation.tax/operation.quantity),2)
              self.QtdAsset = operation.quantity
           else:  #sell
               self.Mprice = round(((self.Mprice * self.QtdAsset) + (operation.price * operation.quantity + operation.tax))/ (self.QtdAsset + operation.quantity),2)
               self.QtdAsset = self.QtdAsset + operation.quantity
        else:
            self.QtdAsset = self.QtdAsset - operation.quantity

    def __str__(self):
        return f"Asset class: Ticker {self.ticker} | Name {self.name} | Price: {self.price} | Perc: {self.percRef} | Mprice: {self.Mprice} | QtdAsset: {self.QtdAsset}"
  
class Reit(LocalAsset):
    pass 

class Operation:
    def __init__(self, asset, date, quantity, price, tax):
        self.asset = asset
        self.date = date
        self.quantity = quantity
        self.price = price
        self.tax = tax
    def __str__(self):
        return f"Operation class: Asset {self.asset} | Date {self.date} | Qtd {self.quantity} | Price {self.price} | {self.tax}"

class Buy(Operation): 
     def __init__(self, asset, date, quantity, price, tax):
        super().__init__(asset, date, quantity, price, tax)
        self.ope = 1.0

     def __str__(self):
        return f"Buy operation: Asset {self.asset} | Date {self.date} | Qtd {self.quantity} | Price {self.price * self.ope}  | {self.tax}"

class Sell(Operation): 
     def __init__(self, asset, date, quantity, price, tax):
        super().__init__(asset, date, quantity, price, tax)
        self.ope = -1.0
     def __str__(self):
        return f"Sell Operation: Asset {self.asset} | Date {self.date} | Qtd {self.quantity} | Price  {self.price * self.ope} | {self.tax}"


BaseAssets = Asset.objects.all()

print(BaseAssets)

SAPR = LocalAsset('SAPR11.SA',40.0)
MRVE = LocalAsset('MRVE3.SA', 10.0)
ITSA = LocalAsset('ITSA4.SA', 30)
ABEV = LocalAsset('ABEV3.SA',10)
HGLG = Reit('HGLG11.SA',10.0)
IRDM = Reit('IRDM11.SA',10.00)
KNRI = Reit('KNRI11.SA', 10.00)
HGRE = Reit('HGRE11.SA',10.00)
# Conjunto de Operacoes SAPR11
sapr1 = Buy('SAPR11.SA', datetime.datetime(2021,12,31),300.0, 24.68, 0.0 )
sapr2 = Buy('SAPR11.SA', datetime.datetime(2022,9,28),300.0, 17.12 , 7.14)
# Conjunto de Operacoes MRVE3
mrve1 = Buy('MRVE3.SA', datetime.datetime(2021,1,14),100.0, 20.93 , 0.0)
mrve2 = Buy('MRVE3.SA', datetime.datetime(2021,10,27),100.0, 10.66 , 0.0)
mrve3 = Sell('MRVE3.SA', datetime.datetime(2022,1,21),100.0, 12.09 , 0.0)
mrve4 = Buy('MRVE3.SA', datetime.datetime(2022,3,15),100.00, 9.96 , 0.0)
mrve5 = Sell('MRVE3.SA', datetime.datetime(2022,3,17),100.0, 10.12 , 0.0)
# Conjunto de Operacoes ITSA4
itsa1 = Buy('ITSA4.SA', datetime.datetime(2022,5,4),500,8.90,6.94)
itsa2 = Buy('ITSA4.SA', datetime.datetime(2022,11,11),50,13.65,0.0)
itsa3 = Buy('ITSA4.SA', datetime.datetime(2023,9,22),7,6.50,0.0)
itsa4 = Buy('ITSA4.SA', datetime.datetime(2023,10,30),27,17.92,0.0)
# Conjunto de Operacoes ABEV3
abev1 = Buy('ABEV3.SA', datetime.datetime(2022,5,18),500,14.52,0.0)
# Conjunto de Operacoes HGLG11
hglg1 = Buy('HGLG11.SA', datetime.datetime(2022,3,10),100,161.25, 4.83)
hglg2 = Buy('HGLG11.SA', datetime.datetime(2022,5,3),18,160.51, 0.00)
hglg3 = Buy('HGLG11.SA', datetime.datetime(2023,6,2),49,155.70, 0.00)
# Conjunto de Operacoes IRDM
irdm1 = Buy('IRDM11.SA', datetime.datetime(2022,4,25),100,107.35, 3.21)
irdm2 = Buy('IRDM11.SA', datetime.datetime(2022,8,12),9,99.42, 0.00)
irdm3 = Buy('IRDM11.SA', datetime.datetime(2022,8,26),21,99.42, 0.00)
# Conjunto de Operacoes KNRI11
knri1 = Buy('KNRI11.SA', datetime.datetime(2022,11,22),20,139.50, 0.82)
knri2 = Buy('KNRI11.SA', datetime.datetime(2024,4,16),4,162.74, 0.00)
knri3 = Buy('KNRI11.SA', datetime.datetime(2024,4,24),29,162.74, 0.00)
# Conjunto de Operacoes HGRE11
hgre1 = Buy('HGRE11.SA', datetime.datetime(2024,4,12),10,128.98, 0.38)

print("### 2 ### Inclusao de Operacoes")

# Adiciona operacoes SAPR
SAPR.add_opp(sapr1)
SAPR.add_opp(sapr2)
# Adiciona operacoes MRVE
MRVE.add_opp(mrve1)
MRVE.add_opp(mrve2)
MRVE.add_opp(mrve3)
MRVE.add_opp(mrve4)
MRVE.add_opp(mrve5)
# Adiciona Operacoes ITSA4
ITSA.add_opp(itsa1)
ITSA.add_opp(itsa2)
ITSA.add_opp(itsa3)
ITSA.add_opp(itsa4)
# Adiciona Operacoes ABEV
ABEV.add_opp(abev1)
# Adiciona Operacoes HGLG
HGLG.add_opp(hglg1)
HGLG.add_opp(hglg2)
HGLG.add_opp(hglg3)
# Adiciona Operacoes IRDM
IRDM.add_opp(irdm1)
IRDM.add_opp(irdm2)
IRDM.add_opp(irdm3)
# Adiciona Operacoes KNRI
KNRI.add_opp(knri1)
KNRI.add_opp(knri2)
KNRI.add_opp(knri3)
# Adiciona Operacoes HGRE
HGRE.add_opp(hgre1)

print("# Exibe situacao ativos")

print(SAPR)
print(MRVE)
print(ITSA)
print(ABEV)
print(HGLG)
print(IRDM)
print(KNRI)
print(HGRE)

### CALCULO DA CARTEIRA REAL ###

class Portifolio:
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
                aux[y]=round((self.composicao[x]/self.vlrTotal)*100,2)
                # Rec > 0 buy Rec <0 wait
                aux[ticker+"Rec"] = self.composicao[ticker+".SA%REF"] - aux[y]
        for x in aux.keys():
            self.composicao[x]=round(aux[x],2)

    def show_data(self):
        for x in self.composicao.keys():
            print (self.composicao[x])

    def __str__(self):
        return f"Class Portifolio: {self.name} | {self.vlrTotal} | {self.composicao} "

print("### 3 ### - Composicao Portifaolio Preco Atual")
MinhaCarteira = Portifolio("Minha Carteira")
MinhaCarteira.add_asset(SAPR)
MinhaCarteira.add_asset(MRVE)
MinhaCarteira.add_asset(ITSA)
MinhaCarteira.add_asset(ABEV)
MinhaCarteira.add_asset(HGLG)
MinhaCarteira.add_asset(IRDM)
MinhaCarteira.add_asset(KNRI)
MinhaCarteira.add_asset(HGRE)

print(MinhaCarteira)

# funcao para calcular percentual de cada ativo em relacao ao patrimonio total

MinhaCarteira.calc_perc()
print("### 4 ### Carteira apos apuracao do percentual vs patrimonio total ")
print(MinhaCarteira)

