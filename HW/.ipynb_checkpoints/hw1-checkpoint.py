#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 1

Created on Tue Aug  9 19:59:04 2022

@author: Alma Velazquez
"""

from random import uniform


class Portfolio:
    def __init__(self):
        self.investments = {"cash": 0, "stock": {}, "mutual_funds": {}}
        self.transactions = []

    def addCash(self, amount):
        self.investments["cash"] += amount
        self.transactions.append(f"Cash Deposit : {amount}\n")

    def withdrawCash(self, amount):
        self.addCash(-1 * amount)
        self.transactions.append(f"Cash Withdrawal : \t{amount}\n")

    def __str__(self):
        # fix: display with $ and 2 decimal places
        portfolio_str = "\nInvestments\n" + "-----------\n"
        portfolio_str += "Cash: $" + str(round(self.investments["cash"], 2)) + "\n"
        portfolio_str += "Stocks:\n"
        for symbol, info in self.investments["stock"].items():
            shares = info["shares"]
            portfolio_str += f"\t{symbol} : {shares}\n"
        portfolio_str += "Mutual Funds:\n"
        for symbol, info in self.investments["mutual_funds"].items():
            shares = round(info["shares"], 2)
            portfolio_str += f"\t{symbol} : {shares}\n"
        return portfolio_str

    def buyStock(self, shares: int, stock):
        self.investments["stock"][stock.symbol] = {
            "shares": shares,
            "purchase_price": stock.price,
            "selling_price": stock.sell(),
        }
        amount = shares * stock.price
        self.withdrawCash(amount)
        self.transactions.append(f"{stock.symbol} Stock Purchase : \t{amount}\n")

    def sellStock(self, symbol, shares: int):
        self.investments["stock"][symbol]["shares"] -= shares
        amount = shares * self.investments["stock"][symbol]["selling_price"]
        self.addCash(amount)
        self.transactions.append(f"{symbol} Stock Sale : {amount}\n")

    def buyMutualFund(self, shares, mf):
        self.investments["mutual_funds"][mf.symbol] = {
            "shares": shares,
            "selling_price": mf.sell(),
        }
        self.withdrawCash(shares)
        self.transactions.append(f"{mf.symbol} MF Purchase : \t{shares}\n")

    def sellMutualFund(self, symbol, shares):
        self.investments["mutual_funds"][symbol]["shares"] -= shares
        amount = shares * self.investments["mutual_funds"][symbol]["selling_price"]
        self.addCash(amount)
        self.transactions.append(f"{symbol} MF Sale : {amount}\n")


class Stock:
    def __init__(self, price, symbol):
        self.symbol = symbol
        self.price = price

    def sell(self):
        return uniform(self.price * 0.5, self.price * 1.5)


class MutualFund:
    def __init__(self, symbol):
        self.symbol = symbol

    def sell(self):
        return uniform(0.9, 1.2)


# Testing
portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(50)
print(portfolio)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
print(portfolio)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.history()
