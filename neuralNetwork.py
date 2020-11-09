import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int)
    
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5,5,0.1)
y = step_function(x)

plt.plot(x,y,color = "blue", alpha = 0.5)
plt.title("Step Function Plot", fontsize = 20)
plt.ylim(-0.1,1.1)
plt.savefig("StepPlot.png")
plt.show()

x = np.arange(-5,5,0.1)
y = sigmoid(x)

plt.plot(x,y,color = "red", alpha = 0.5)
plt.title("Sigmoid Plot", fontsize = 20)
plt.ylim(-0.1,1.1)
plt.savefig("SigmoidPlot.png")
plt.show()

y = sigmoid(x)
y1 = step_function(x)
plt.plot(x,y1,color = "blue", alpha = 0.5)
plt.plot(x,y,color = "red", alpha = 0.5)
plt.title("Step & Sigmoid Plot", fontsize = 20)
plt.ylim(-0.1,1.1)
plt.savefig("Both.png")
plt.show()

def relu(x):
    return np.maximum(0,x)

y = relu(x)
plt.plot(x,y,color = "red", alpha = 0.5)
plt.title("ReLU Plot", fontsize = 20)
plt.ylim(-0.1,5.1)
plt.savefig("ReLU Plot.png")
plt.show()
