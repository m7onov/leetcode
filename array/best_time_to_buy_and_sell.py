"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/

Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


def max_profit(prices: List[int]) -> int:

    if len(prices) < 2:
        return 0

    have_papers = False
    total = 0

    for i, price in enumerate(prices):
        if i == 0:
            if price < prices[i + 1]:
                total -= price
                have_papers = True

        elif i == len(prices) - 1:
            if prices[i - 1] <= price:
                if have_papers:
                    total += price
                    have_papers = False

        else:
            if prices[i - 1] <= price and price > prices[i + 1]:
                if have_papers:
                    total += price
                    have_papers = False

            if prices[i - 1] >= price and price < prices[i + 1]:
                if not have_papers:
                    total -= price
                    have_papers = True

    return total

