import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def height()
df = pd.read_csv('data2.csv')


input_data = df[['身長', '体重']][:]
input_data_np = input_data.to_numpy()

data_number = input_data_np.shape[0]

input_data_min = np.min(input_data_np, axis=0, keepdims=True)
x_min = input_data_min[0, 0]
y_min = input_data_min[0, 1]

input_data_max = np.max(input_data_np, axis=0, keepdims=True)
x_max = input_data_max[0, 0]
y_max = input_data_max[0, 1]

input_data_normalized = (input_data_np - np.array([[x_min,y_min]])) / np.array([[(x_max - x_min),(y_max - y_min)]])


epochs = 100
alpha = 0.01

w0 = 0.1
w1 = 0.1

for t in range(epochs):
    dw0 = 0
    dw1 = 0
    for i in range(data_number):
        dw0 = dw0 + 2*w0 + 2*w1*input_data_normalized[i,0] -2*input_data_normalized[i,1]
        dw1 = dw1 + input_data_normalized[i,1]*(2*w1*input_data_normalized[i,0] +2*w0 -2*input_data_normalized[i,1])


    w0 = w0 - alpha*(dw0)
    w1 = w1 - alpha*(dw1)
    
x = np.linspace(x_min-5,x_max+5,100)

'''
(1/14)*y = w0 + w1*(1/10)*x
y = 14(w0 + (1/10)*w1*x)
y - 30 = 14(w0 + w1*(x-20)/10)
'''
y = (y_max - y_min)*(w0 + w1*(x-x_min)/(x_max - x_min)) + y_min



plt.plot(x,y)


for u in range(data_number):
    plt.scatter(input_data_np[u,0], input_data_np[u,1])
