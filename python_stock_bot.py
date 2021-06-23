#!/usr/bin/python3
from datetime import datetime, timedelta
import yfinance as yf

def avg_low(ticker, two_hund):
    total = 0
    two_hund_days = yf.download(ticker, two_hund, datetime.now())
    for index, row in two_hund_days.iterrows():
        total += row['Low']

    average_low = total / len(two_hund_days)
    return average_low


def avg_high(ticker, sixty):
    total = 0
    sixty_days = yf.download(ticker, sixty, datetime.now())
    for index, row in sixty_days.iterrows():
        total += row['High']

    average_high = total / len(sixty_days)
    return average_high

def main():
    sixty = datetime.today() - timedelta(days=60)
    two_hund = datetime.today() - timedelta(days=200)
    stocks = {'Palantir': 'PLTR',
              'Jacobs': 'J',
              'ATT': 'T',
              'AMC': 'AMC',
              'S&P': 'SPYD'
              }

    for key in stocks:
        print(key)
        print("Average High: {:0.2f}".format(avg_high(stocks[key], sixty)))
        print("Average Low: {:0.2f}".format(avg_low(stocks[key], two_hund)))
        print("\n")

main()
