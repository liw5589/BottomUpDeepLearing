## BottomUpDeepLearing

### Activation Function

StepFunction            |  Sigmoid
:-------------------------:|:-------------------------:
<img src="Img/SigmoidPlot.png" width = "500px"/>  |  <img src="Img/Both.png" width = "500px"/>


Both            |  ReLU
:-------------------------:|:-------------------------:
<img src="Img/Both.png"  width = "500px"/>  | <img src="Img/ReLU_Plot.png" width = "500px"/>


#### StepFunctionPlot
```python
def step_function(x):
    y = x > 0
    return y.astype(np.int)
```

#### SigmoidPlot
```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

#### ReLU
```python
def relu(x):
    return np.maximum(0,x)
```
