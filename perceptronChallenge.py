from PyPerceptron import *
from random import randint

weights = newPerceptron(2)

for i in range(1000):
    inputs = []
    inputs.append(randint(0,1000))
    inputs.append(randint(0,1000))   
    if inputs[0] > inputs[1]:
        label = 1
    else:
        label = -1
    
    weights = train(inputs, weights, label, 0.1)

while True:
    inputs[0] = int(input("Input1 "))
    inputs[1] = int(input("Input2 "))

    output = feedForward(inputs, weights)
    #print(feedForward(inputs, weights))
    print()
    if output == -1:
        print("{0} is smaller than {1} ".format(inputs[0], inputs[1]))
    else:
        print("{0} is greater than {1} ".format(inputs[0], inputs[1]))
    print()
