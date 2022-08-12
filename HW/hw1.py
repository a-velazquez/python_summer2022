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

    def addCash(self, amount, transaction_nm="Cash Transaction"):
        self.investments["cash"] += amount
        if amount < 0:
            amount = "\t" + str(amount)
        self.transactions.append(f"{transaction_nm} : {amount}\n")

    def withdrawCash(self, amount, transaction_nm="Cash Transaction"):
        self.addCash(-1 * amount, transaction_nm)

    def __str__(self):
        # fix: display with $ and 2 decimal places
        portfolio_str = "\Holdings\n" + "-----------\n"
        portfolio_str += "Cash: $" + str(round(self.investments["cash"], 2)) + "\n"
        portfolio_str += "Stocks:\n"
        for symbol, info in self.investments["stock"].items():
            shares = info["shares"]
            portfolio_str += f"\t{symbol} - {shares}\n"
        portfolio_str += "Mutual Funds:\n"
        for symbol, info in self.investments["mutual_funds"].items():
            shares = round(info["shares"], 2)
            portfolio_str += f"\t{symbol} - {shares}\n"
        return portfolio_str

    def history(self):
        print("".join(self.transactions))

    def buyStock(self, shares: int, stock):
        self.investments["stock"][stock.symbol] = {
            "shares": shares,
            "purchase_price": stock.price,
        }
        amount = shares * stock.price
        self.withdrawCash(amount, transaction_nm=f"{stock.symbol} Stock Purchase")

    def sellStock(self, symbol, shares: int):
        self.investments["stock"][symbol]["shares"] -= shares
        selling_price = uniform(
            self.investments["stock"][symbol]["purchase_price"] * 0.5,
            self.investments["stock"][symbol]["purchase_price"] * 1.5,
        )
        amount = round(shares * selling_price, 2)
        self.addCash(amount, transaction_nm=f"{symbol} Stock Sale")

    def buyMutualFund(self, shares, mf):
        self.investments["mutual_funds"][mf.symbol] = {
            "shares": shares,
        }
        self.withdrawCash(shares, transaction_nm=f"{mf.symbol} MF Purchase")

    def sellMutualFund(self, symbol, shares):
        self.investments["mutual_funds"][symbol]["shares"] -= shares
        amount = round(shares * uniform(0.9, 1.2), 2)
        self.addCash(amount, transaction_nm=f"{symbol} MF Sale")


class Stock:
    def __init__(self, price, symbol):
        self.symbol = symbol
        self.price = price


class MutualFund:
    def __init__(self, symbol):
        self.symbol = symbol


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
