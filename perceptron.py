# AND GATE
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    else:
        return 1

print("*** AND GATE RESULT ***")
print("ADD GATE's Result : ",AND(0,0))
print("ADD GATE's Result : ",AND(0,1))
print("ADD GATE's Result : ",AND(1,0))
print("ADD GATE's Result : ",AND(1,1))