
from numpy import *
from os import listdir
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

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('D:\\02_code_program\\05_python\\digits\\trainingDigits')
    m =  len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split(',')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = KNN.img2vector('D:\\02_code_program\\05_python\\digits\\trainingDigits\\%s' % fileNameStr)

    testFileList = listdir('D:\\02_code_program\\05_python\\digits\\testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = KNN.img2vector('D:\\02_code_program\\05_python\\digits\\testDigits\\%s' % fileNameStr)
        classifierResult = KNN.classify(vectorUnderTest,trainingMat,hwLabels,3)
        print "the classifier came back with:%d,the real answer is :%d" %(classifierResult,classNumStr)
        if(classifierResult != classNumStr):errorCount += 1.0
    print " total number of errors is: %d" % errorCount
    print " error rate is:%f" %(errorCount/float(mTest))
if __name__ == "__main__":
    # datingDataMat, datingLabels = file2maxtrix('/Users/cloudpj/git/data/datingTestSet2.txt')
    # normMat,ranges,minVals = autoNorm(datingDataMat)
    # print normMat
    # print ranges
    # print datingDataMat
    # print datingLabels
    # showClass()
    # classifyPerson()
    # fileName = 'D:\\02_code_program\\05_python\\digits\\trainingDigits\\0_0.txt'
    # resultVect = KNN.img2vector(fileName)
    # print resultVect
    handwritingClassTest()