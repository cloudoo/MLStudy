# coding=utf-8

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
import os

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

"""
    classfiy
"""
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2maxtrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normdataSet = zeros(shape(dataSet))

def showClass():
    group, labels = createDataSet()
    # print  group,labels
    # print classify([0,0],group,labels,3)
    datingDataMat, datingLabels = file2maxtrix('/Users/cloudpj/git/MLStudy/data/datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()

def test():
    print '__file__:'+os.path.dirname(os.path.abspath("__file__"))
    print os.path.pardir
    print os.path.join(os.path.dirname("__file__"), os.path.pardir)
    print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

if __name__ == "__main__":
    showClass()

