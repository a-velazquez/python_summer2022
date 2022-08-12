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
        """"Constructor of class Portfolio; 
        tracks user holdings across 3 asset types"""

        # instantiate empty dict of holdings
        self.investments = {"cash": 0, "stock": {}, "mutual_funds": {}}

        # instantiate empty list of cash transactions
        self.transactions = []

    def __str__(self):
        """"Define print method of class Portfolio; 
        displays a formatted string version of the portfolio dict 
        """

        # begin string with informative header
        portfolio_str = "\nCurrent Holdings\n" + "-----------------\n"

        # format and add each key of dict to the printed string:
        # cash
        pretty_cash = round(self.investments["cash"], 2)
        portfolio_str += f"Cash: $ {pretty_cash:.2f} \n"

        # stocks
        portfolio_str += "Stocks:\n"
        for symbol, info in self.investments["stock"].items():
            shares = info["shares"]
            portfolio_str += f"\t{symbol} : {shares}\n"

        # mutual funds
        portfolio_str += "Mutual Funds:\n"
        for symbol, info in self.investments["mutual_funds"].items():
            shares = round(info["shares"], 2)
            portfolio_str += f"\t{symbol} : {shares}\n"

        return portfolio_str

    def history(self):
        """"Define history method of class Portfolio; 
        displays a formatted string version of the transaction list 
        """

        # print informative header and each cash transaction made in chronological order
        print("\nTransaction Log\n" + "----------------\n" + "".join(self.transactions))

    def addCash(self, amount, transaction_nm="Cash Deposit"):
        """"Define method addCash; 
        allows for user cash deposits to Portfolio;
        passes default name for entry in transaction log"""

        # add desired amount to cash key in dict
        self.investments["cash"] += amount

        # and append to transaction list
        self.transactions.append(f"{transaction_nm} : {amount:.2f}\n")

    def withdrawCash(self, amount, transaction_nm="Cash Withdrawal"):
        """"Define method withdrawCash; 
        allows for user cash withdrawals from Portfolio;
        passes default name for entry in transaction log"""

        # define as negative of addCash method, with custom transaction name
        self.addCash(-1 * amount, transaction_nm)

    def buyStock(self, shares: int, stock):
        """"Define buyStock method of class Portfolio; 
        withdraws cash from portfolio to purchase whole units from
        object of class Stock
        """

        # check that whole shares are purchased
        if not isinstance(shares, int):
            raise TypeError("Stock shares can only be whole numbers.")

        else:

            # adds desired units of given stock to portfolio
            self.investments["stock"][stock.symbol] = {
                "shares": shares,
                # store purchase price to use if selling shares later
                "purchase_price": stock.price,
            }

            # withdraws cash necessary to pay for purchase
            amount = shares * stock.price
            self.withdrawCash(amount, transaction_nm=f"{stock.symbol} Stock Purchase")

    def sellStock(self, symbol, shares: int):
        """"Define sellStock method of class Portfolio; 
        deposits cash to portfolio from sale of whole stocks 
        held by user
        """

        # check that whole shares are sold
        if not isinstance(shares, int):
            raise TypeError("Stock shares can only be whole numbers.")

        else:

            # remove sold units from portfolio
            self.investments["stock"][symbol]["shares"] -= shares

            # generate selling price based on stored purchase price
            selling_price = uniform(
                self.investments["stock"][symbol]["purchase_price"] * 0.5,
                self.investments["stock"][symbol]["purchase_price"] * 1.5,
            )

            # add cash from sale to holdings
            amount = round(shares * selling_price, 2)
            self.addCash(amount, transaction_nm=f"{symbol} Stock Sale")

    def buyMutualFund(self, shares, mf):
        """"Define buyMutualFund method of class Portfolio; 
        withdraws cash from portfolio to purchase units from
        object of class MutualFund
        """

        # add purchased shares to portfolio
        self.investments["mutual_funds"][mf.symbol] = {
            "shares": shares,
        }

        # withdraw cash needed to pay for the purchase
        self.withdrawCash(shares, transaction_nm=f"{mf.symbol} MF Purchase")

    def sellMutualFund(self, symbol, shares):
        """"Define sellMutualFund method of class Portfolio; 
        deposits cash to portfolio from sale of stocks 
        held by user
        """

        # remove sold units from portfolio
        self.investments["mutual_funds"][symbol]["shares"] -= shares

        # generate selling price
        amount = round(shares * uniform(0.9, 1.2), 2)

        # add cash from sale to holdings
        self.addCash(amount, transaction_nm=f"{symbol} MF Sale")


class Stock:
    def __init__(self, price, symbol):
        """"Constructor of class Stock; 
        contains attributes symbol and purchase price"""

        self.symbol = symbol
        self.price = price


class MutualFund:
    def __init__(self, symbol):
        """"Constructor of class Stock; 
        contains attribute symbol """

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
print(portfolio)

portfolio.buyStock(5.2, s)
