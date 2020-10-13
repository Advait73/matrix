import random
import matplotlib.pyplot as plt

heads = 0
tails = 0
iterations = 0
results = []

def askUserHowManyFlips():
    amountOfFlips = int(input("How many flips?:"))
    return amountOfFlips

def flip(flips):
    global heads, tails, iterations
    for i in range(flips):
        flip = random.randrange(2)
        results.append(flip)
        if flip == 0:
            heads += 1
            iterations += 1
        elif flip == 1:
            tails += 1
            iterations += 1
def calculateTheAverage():
    sumOfValues = sum(results)
    average = sumOfValues / len(results)
    return f"The average was {average}, 0 being heads and 1 being tails"
def theDifference():
    if heads > tails:
        difference = heads - tails
        statement = f"There were {difference} more heads than tails"
    elif tails > heads:
        difference = tails - heads
        statement = f"There were {difference} more tails than heads"
    return statement

def winner():
    if heads > tails:
        winner = "heads"

    elif tails > heads:
        winner = "tails"
    return f"{winner} wins!"

def percentage():
    global heads, tails
    percentage_heads = str(heads / iterations * 100) + '%'
    percentage_tails = str(heads / iterations * 100) + '%'
    return f"heads was flipped {percentage_heads} of the time, tails was flipped {percentage_tails} of the time"

def plot():
    global heads, tails
    labels = "heads", "tails"
    sizes = [heads, tails]
    colors = ['red', 'yellow']
    if heads > tails:
        explode = [0.5, 0]
    elif tails > heads:
        explode = [0, 0.5]
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow = True)
    plt.axis('equal')
    plt.show()

def run():
    amountOfFlips = askUserHowManyFlips()
    flip(amountOfFlips)
    print(calculateTheAverage())
    print(f"{heads} heads and {tails} tails")
    print(theDifference())
    print(percentage())
    print(winner())
    plot()
run()