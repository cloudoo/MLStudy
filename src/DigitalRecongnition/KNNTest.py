
from numpy import *
import KNN
import operator
import matplotlib
import matplotlib.pyplot as plt
import os


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = KNN.file2maxtrix('/Users/cloudpj/git/data/datingTestSet2.txt')
    normMat, ranges, minVals = KNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = KNN.classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],4)
        print "the classifier came back with:%d,the real answer is: %d" %(classifierResult,datingLabels[i])
        if(classifierResult !=datingLabels[i]): errorCount += 1.0

    print "the total error rate is: %f" %(errorCount/float(numTestVecs))

def showTest():
    group, labels = createDataSet()
    # print  group,labels
    # print classify([0,0],group,labels,3)
    datingDataMat, datingLabels = KNN.file2maxtrix('/Users/cloudpj/git/data/datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()

def test():
    print '__file__:'+os.path.dirname(os.path.abspath("__file__"))
    print os.path.pardir
    print os.path.join(os.path.dirname("__file__"), os.path.pardir)
    print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    ffMiles = float(raw_input("frequent filter miles earned per year?"))

    datingDataMat,datingLabels = KNN.file2maxtrix('/Users/cloudpj/git/data/datingTestSet2.txt')
    normMat,ranges,minVals = KNN.autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = KNN.classify((inArr-minVals)/ranges,normMat,datingLabels,3)

    print "You will probably like this person:",resultList[classifierResult -1]

if __name__ == "__main__":
    # datingDataMat, datingLabels = file2maxtrix('/Users/cloudpj/git/data/datingTestSet2.txt')
    # normMat,ranges,minVals = autoNorm(datingDataMat)
    # print normMat
    # print ranges
    # print datingDataMat
    # print datingLabels
    # showClass()
    classifyPerson()