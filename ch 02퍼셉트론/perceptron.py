import numpy as np

# AND GATE
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    else:
        return 1

print("*** AND GATE RESULT ***")
print("INPUT :", 0, 0 ,"=>","AND GATE's Result : ",AND(0,0))
print("INPUT :", 0, 1 ,"=>","AND GATE's Result : ",AND(0,1))
print("INPUT :", 1, 0 ,"=>","AND GATE's Result : ",AND(1,0))
print("INPUT :", 1, 1 ,"=>","AND GATE's Result : ",AND(1,1))

print("")
print("*** ANOTHER VERSION OF AND GATE USING NUMPY")

def AND_Gate_using_np(x1,x2):
    inputs = np.array([x1,x2])
    weights = np.array([0.5,0.5])
    bias = -0.7
    temp = np.sum(weights * inputs) + bias
    if temp <= 0:
        return 0
    else:
        return 1

print("*** AND GATE RESULT Using np ***")
print("AND GATE's Result : ",AND_Gate_using_np(0,0))
print("AND GATE's Result : ",AND_Gate_using_np(0,1))
print("AND GATE's Result : ",AND_Gate_using_np(1,0))
print("AND GATE's Result : ",AND_Gate_using_np(1,1))
print("")
# print("*** NAND GATE USING NUMPY ***")
def NAND_Gate(x1,x2):
    inputs = np.array([x1,x2])
    weights = np.array([-0.5,-0.5])
    bias = 0.7
    temp = np.sum(weights * inputs) + bias
    if temp <= 0:
        return 0
    else:
        return 1

print("*** NAND GATE RESULT Using np ***")
print("NAND GATE's Result : ",NAND_Gate(0,0))
print("NAND GATE's Result : ",NAND_Gate(0,1))
print("NAND GATE's Result : ",NAND_Gate(1,0))
print("NAND GATE's Result : ",NAND_Gate(1,1))
print("")
# print("*** NAND GATE USING NUMPY ***")
def OR_Gate(x1,x2):
    inputs = np.array([x1,x2])
    weights = np.array([0.5,0.5])
    bias = -0.2
    temp = np.sum(weights * inputs) + bias
    if temp <= 0:
        return 0
    else:
        return 1

print("*** OR GATE RESULT Using np ***")
print("OR GATE's Result : ",OR_Gate(0,0))
print("OR GATE's Result : ",OR_Gate(0,1))
print("OR GATE's Result : ",OR_Gate(1,0))
print("OR GATE's Result : ",OR_Gate(1,1))
print("")

def XOR_Gate(x1,x2):
    s1 = NAND_Gate(x1,x2)
    s2 = OR_Gate(x1,x2)
    y = AND_Gate_using_np(s1,s2)
    return y
    
print("*** XOR GATE RESULT Using np ***")
print("XOR GATE's Result : ",XOR_Gate(0,0))
print("XOR GATE's Result : ",XOR_Gate(0,1))
print("XOR GATE's Result : ",XOR_Gate(1,0))
print("XOR GATE's Result : ",XOR_Gate(1,1))
