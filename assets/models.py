from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Sector(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.id} - {self.name}"

class Operation(models.Model):
    name = models.CharField(max_length=64)
    factor = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
           return f"{self.factor}"
    
class Asset(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="assetSector")

    def __str__(self):
        return f"{self.ticker}"
    
class Trade(models.Model):
    ticker = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="assetTrade")
    date = models.DateField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)
    tax = models.DecimalField(max_digits=12,decimal_places=4)
    operator = models.ForeignKey(Operation, on_delete= models.CASCADE, related_name="operation")

    def __str__(self):
        return f"{self.ticker} {self.date} {self.quantity} {self.price} {self.tax} {self.operator}"

class PortfolioComp(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.Case, related_name="portfolio", default=1)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="assetPortfolio")
    percentage = models.DecimalField(max_digits=10,decimal_places=4)

    def __str__(self):
        return f"{self.id} : {self.portfolio} {self.asset} - {self.percentage}"
