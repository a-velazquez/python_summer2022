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
        for asset, amount in self.investments.items():
            portfolio_str += f"{asset} : {amount}\n"
        return portfolio_str

    def buyStock(self, shares: int, stock):
        self.investments["stock"][stock.symbol] = shares
        amount = shares * stock.price
        self.withdrawCash(amount)
        self.transactions.append(f"Stock Purchase : \t{amount}\n")

    def sellStock(self, shares: int, stock):
        self.investments["stock"][stock.symbol] -= shares
        amount = shares * stock.sell()
        self.addCash(amount)
        self.transactions.append(f"Stock Sale : {amount}\n")


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


portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(50)
print(portfolio)
