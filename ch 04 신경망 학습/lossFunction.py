import numpy as np
import matplotlib.pyplot as plt
#오차제곱합
def sum_sqaured_error(y,t):
    return 0.5 * np.sum((y-t)**2)

#교차 엔트로피 오차
def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2 * h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

def tangent_line(f, x):
        d = numerical_diff(f, x)
        # print(d)
        y = f(x) - d*x
        return lambda t: d*t + y

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical_diff", fontsize = 20)
plt.plot(x,y, color = "red", alpha = 0.5, linewidth = 6)
plt.savefig("../Img/Original_Function_Plot.png" )
plt.show()

# diff_1 = numerical_diff(function_1,5)
# diff_2 = numerical_diff(function_1,10)

# tf = tangent_line(function_1, 5)
# y2 = tf(x)
# plt.plot(x, y2, color = "blue", alpha = 0.5, linewidth = 6)
# # plt.show()

# tf = tangent_line(function_1, 10)
# y3 = tf(x)
# plt.plot(x, y3, color = "blue", alpha = 0.5, linewidth = 6)

# plt.axhline(function_1(5), 0, 0.25, color='black', linestyle='--', linewidth='3')
# plt.axvline(5, 0, 0.25,color='black', linestyle='--', linewidth='3')
# plt.axhline(function_1(10), 0, 0.5, color='black', linestyle='--', linewidth='3')
# plt.axvline(10, 0, 0.43,color='black', linestyle='--', linewidth='3')
# # plt.axvline(1, 0, 0.16, color='lightgray', linestyle=':', linewidth='2')

# plt.plot([5], [function_1(5)], marker='o', markersize=10, color="black", alpha = 0.5)
# plt.plot([10], [function_1(10)], marker='o', markersize=10, color="black", alpha = 0.5)
# plt.savefig("../Img/Numerical_diff_Plot.png")
# plt.show()