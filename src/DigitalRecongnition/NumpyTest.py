# coding=UTF-8
import numpy as np


a = np.array([[1,2],
              [4,5]])
print a
print 'num of dim:',a.ndim
print 'shape:',a.shape
print 'size:',a.size

#
b = np.arange(4).reshape(2,2)
c = np.random.random((2,4))

print np.dot(a,b)
print a.dot(b)

print 'c:',c
# 对列求和 axis = 0
print 'np.sum(c,axis=0):',np.sum(c,axis=0)
# 对行求和 axis = 0
print 'np.sum(c,axis=1):',np.sum(c,axis=1)
print 'np.min(c):',np.min(c,axis=0)
print 'np.max(c):',np.max(c)
# a = np.array([10,12,14,20])
# b = np.arange(4)



# print a,b
# print 'a+b=',a+b
# # squar
# print 'b**2',b**2
#
# # sin,cos,tan
# print 10*np.sin(a)
#
# print 'a<13:',a<13
# print 'a==12:',a<12

a = np.arange(14,2,-1).reshape(3,4)
print a
print np.argmin(a)
print np.argmax(a)
# 平均值
print np.mean(a) # a.mean() ,a.average()

# 中位数
print np.median(a)

# 累加值
print np.cumsum(a)

print np.diff(a)


print np.nonzero(a)

print np.sort(a)

print np.transpose(a) # print a.T

print np.clip(a,6,10)

print np.mean(a,axis=0)
print a

print  a[1,2]
print  a[:,2]
print  a[1,:]
print  a[1,1:3]
print '---------------'
for row in a:
    print row


print '---------'
for row in a.T:
    print row

# a.flat 是个迭代器
# a.flattern() 返回一个一位数组
print '----a.flat-----'
for row in a.flat:
    print row

# array的合并

a = np.array([1,2,3,4,5])
b = np.array([2,5,6,7,3])
# 上下合并
print np.vstack((a,b))
# 左右合并
print np.hstack((a,b))

print a.shape

newa = a[:,np.newaxis]

print newa
print newa.shape