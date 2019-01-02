from random import randint
def createPerceptron(I):
    weights = []
    for i in range(I):
        weights.append(randint(-10, 10)/10)
    return(weights)
def testPerceptron(Inputs, Weights):
    Wsum = 0
    for i in range (len(Inputs)):
        Wsum += Inputs[i] * Weights[i]
    if Wsum > 0:
        Output = 1
    else:
        Output = 0
    return (Output)
def changeWeight(expected, guess, Input, weight, lr):
    newW += lr * (expected - guess) * Input
    return(newW)
def changeWeights(answers, guess, inputs, weights, lr):
        newWeights = []
        for i in range(0,len(answers)):
            newWeights.append(changeWeight(answers[i], guess, inputs[i]), Weights[i], lr)
        return(newWeights)
def trainPerceptron(inputs, answers, lr):
        Inputs = inputs
        Weights = createPerceptron(len(inputs))
        for answer in answers:
            guess = testPerceptron(inputs, Weights)
            if not(guess == answer):
                newWeights = changeWeights(answers, guess, inputs, weights, lr)
            else:
                newWeights = Weights
        return(newWeights)
#inputs = [2, 5, 7]
#answers = [0, 1, 1]
#lr = 0.1
#print(trainPerceptron(inputs, answers, lr))

