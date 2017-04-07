# ##
# You can and should use the Step activation function for the OR perceptron.
# Multilayer neural networks are trained using backpropagation. A requirement
# for backpropagation is a differentiable activation function due to its use of
# gradient descent to update the weights. The step function is not differentiable
# at x=0, and its derivative is 0 elsewhere; thus, gradient descent won't be able
# to update the weights and backpropagation will fail. The sigmoid function does
# not have this problem, so use it for the multilayer neural network.
#
# step activation function
#
# JUSTIN:
# perceptron is supervised, how will we decide that our output is expected, without
# any sort of target output given? Should we create our own expected array by
# examining if '1' is in the input?
#
# PROF:
# The picture I included in the assignment didn't include a bias because I didn't
# want you to use one for this, or Bias = 0, in other words.
# You will need to train your perceptron.

import random

NUM_INPUTS = 4
LEARNING_RATE = 0.1

def createTestDataFile(filename, trainingData):
  with open(filename, 'w') as f:
    for testcase in trainingData:
      f.write("[")
      i = 0
      for i in range(NUM_INPUTS): # don't read the solution (last value in length 5 array)
        f.write(str(testcase[i]))
        if i != NUM_INPUTS - 1:
          f.write(" ")
      f.write("]\n\n")
  return

def createTrainingData():
  numTrainingSets = 2**NUM_INPUTS
  trainingData = [None] * (numTrainingSets) # each input has 2 options: 1 or 0
  i = 0
  for x1 in range(2):
    for x2 in range(2):
      for x3 in range(2):
        for x4 in range(2):
          orSolution = x1 or x2 or x3 or x4
          testcase = [x1, x2, x3, x4, orSolution]
          trainingData[i] = testcase
          i += 1
  return trainingData

def readDataFromFile(filename):
  with open(filename, 'r') as f:
    inputLinesFromFile = f.readlines()
  inputCases = []
  for line in inputLinesFromFile:
    if line != "" and line.isspace() == False: # skip blank lines
      inputSet = [None] * NUM_INPUTS
      i = 0
      for literal in line:
        if literal != "[" and literal != "]" and literal.isspace() == False:
          inputSet[i] = int(literal)
          i += 1
      inputCases.append(inputSet)
  return inputCases

def writeSolutionToFile(filename, solutionSet):
  with open(filename, 'w') as f:
    for solution in solutionSet:
      f.write("[")
      f.write(str(solution))
      f.write("]\n\n")
  return

def trainPerceptron(trainingData):

  # initialize weights randomly
  weights = [None] * NUM_INPUTS
  for i in range(NUM_INPUTS):
    weights[i] = random.uniform(-1, 1)

  print ("initially, weights are " + str(weights))

  trainingComplete = False

  while trainingComplete == False:
    trainingComplete = True # assume weights are good unless find a case where trained guess different from target

    for dataSet in trainingData:
      target = dataSet[NUM_INPUTS] # last value is the correct 'OR' value

      # compute answer using weights
      computed = 0
      for i in range(NUM_INPUTS):
        computed += weights[i] * dataSet[i]

      # compute error
      error = float(target) - computed

      # classify as 1 or 0 based on computed answer
      if computed > 0:
        computedAnswer = 1
      else:
        computedAnswer = 0

      if computedAnswer != target:
        trainingComplete = False
        # adjust weights accordingly
        for i in range(NUM_INPUTS):
          weights[i] += LEARNING_RATE * dataSet[i] * error

  print "done training"

def classifyData():
  pass


def main():

  testFile = "testFile.txt"

  inFile = "in.txt"
  outFile = "out.txt"

  #read tranining data from file
  trainingData = createTrainingData()

  print(trainingData)


  #createTestDataFile(testFile, trainingData)
  #testCases = readDataFromFile(testFile)
  #print testCases


  #train perceptrons to get weights
  trainPerceptron(trainingData)

  #use weights to classify input file

  #write classifications to file

  print ("curry")
  pass

if __name__ == "__main__":
  main()