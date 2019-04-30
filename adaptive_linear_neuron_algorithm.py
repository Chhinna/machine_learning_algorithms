from array import *
import random

input_x = array('i',[])

input_y = array('i',[])

for p in range (100):

    a=random.randint(1,10)
    input_x.append(a)
    b=random.randint(1,10)
    input_y.append(b)

learning_fac = 0.01

wx = ((random.randint(-10,10))/10)

wy = ((random.randint(-10,10))/10)

for z in range (100):
    guess_output = wx*input_x[z] + wy*input_y[z]

    true_output = input_x[z] - input_y[z]

    del_wx = learning_fac*(true_output - guess_output)*input_x[z]

    del_wy = learning_fac*(true_output - guess_output)*input_y[z]

    wx = wx + del_wx

    wy = wy + del_wy

print (wx)

print (wy)
        

