# Understand that we get a list consisting of stock prices
# Our goal is to buy the stocks when they are cheap and sell them when there value
# is highest
# Ex) prices = [6, 3, 1, 2, 5, 4] -> 4
# Plan
# Search and filter for the numbers in the list that give the biggest positive difference btween them
# Then take the difference btw these two number
# Need to check that the stock increase at some point

# Sol has long exec Time
def buyAndSellStock(prices):
    max_profit = 0
    total_stocks = len(prices)
    for i in range(0, total_stocks):
        for j in range(i + 1, total_stocks):
            if (prices[j] - prices[i]) < 0:
                continue
            elif (prices[j] - prices[i]) > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit


def buyAndSellStock(prices):
    max_profit = 0
    total_stocks = len(prices)
    min_element = prices[0]
    for i in range(1, total_stocks):
        if (prices[i] - min_element) > max_profit:
            max_profit = prices[i] - min_element
        # This line updates the minimum element
        # Ensures that every time were comparing fairly to the max profit
        if prices[i] < min_element:
            min_element = prices[i]
    return max_profit


# Understand: we want to replace the letter to the one that comes after in the alpah bet
# use asc2 codes to identify the character, specifcally use ord in python
# Plan:
# Run a for loop and replace at the same time
# ex) for input_string[i] = char(ord(input_string)+1)
# if input_string[i] == "z" then input_string[i] = "a"

def alphabeticShift(inputString):
    inputString = list(inputString)
    for index, char in enumerate(inputString):
        if char == "z":
            inputString[index] = "a"
        else:
            inputString[index] = chr(ord(inputString[index]) + 1)
    return "".join(inputString)


# Resource To Solve This Problem:
# https: // www.geeksforgeeks.org / maximum - difference - between - two - elements /
#

# Understand:
# Check weather the sequence s is regular that is that for every first paranthesis
# That is actually closes
# Plan
# Check weather this is a regular seq by assign
# ( to 1 and ) to -1.
# Hace a counter that keeps track of the sequenec
# Have a case where the counter!= ; for every ( we need a ) in order for it to be reg sequ otherwise
# The counter should spit False as the counter will either be > or < 0
def validParenthesesSequence(s):
    # Have a flag that keeps track of the current loop wheather is currently a false or true situation
    # Counter keeps track of weather the seq is reg or not
    flag = True
    counter = 0
    for i in range(len(s)):
        if s[i] == "(":
            counter += 1
        else:
            counter += -1
        if counter < 0:
            # We are breaking and setting flag equal to True b/c currently the sequence is not equal 0 so that is
            # false regular sequence
            # We break b/c we want to check if in the next loop it closes
            flag = False
            break
    if counter != 0:
        flag = False
    return flag

# https://www.geeksforgeeks.org/check-if-given-parentheses-expression-is-balanced-or-not/

def buyAndSellStock(prices):
    max_profit = 0
    min = price[0]
    for index, price in enumerate(prices):
        if price < min:
            min = price
            # max profit is still 0 b/c price is found to be a  min
        elif price - min > max_profit:
            max_profit = price - min
    return max_profit