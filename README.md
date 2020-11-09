# BottomUpDeepLearing

## Activation Function
#### StepFunctionPlot
```python
def step_function(x):
    y = x > 0
    return y.astype(np.int)
```
<img src="Img/StepPlot.png">

#### SigmoidPlot
```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```
<img src="Img/SigmoidPlot.png" style = "width : 200px">

#### Both

<img src="Img/Both.png">

#### ReLU
```python
def relu(x):
    return np.maximum(0,x)
```
<img src="Img/ReLU_Plot.png">