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

class Asset(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="assetSector")

class Trade(models.Model):
    ticker = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="assetTrade")
    date = models.DateTimeField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)
    tax = models.DecimalField(max_digits=12,decimal_places=4)

class PorftfolioComp(models.Model):
    portifolio = models.ForeignKey(Portfolio, on_delete=models.Case, related_name="portfolio")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="assetPortfolio")
    Percentage = models.DecimalField(max_digits=10,decimal_places=4)