import numpy as np
import json
import os
import torch

r = 10  # num of regions
age65_rate = [18.20, 18.20,14.30, 15.80, 16.40, 13.10, 14.80, 13.20, 11.50, 10.80, 9.72, 9.70, 12.80, 16.40, 15.20, 15.70]  # rate of 65 up of each region
population = [708829,1106214,3452460,2019764,567851,3133469,392606,1312778,1840295,1324044,2269487,1993591,441040,457313,527683,345671] # pop of each region

prob = np.zeros((336, r, r))
list_prob = prob.tolist()
json_prob = json.dumps(list_prob)
print("flow:")
print(list_prob)
with open('data/city_sample/prob.json', 'w') as f:
    f.write(json_prob)

flow = np.ones(r)
list_flow = flow.tolist()
json_flow = json.dumps(list_flow)
print("flow:")
print(list_flow)
with open('data/city_sample/flow.json', 'w') as f:
    f.write(json_flow)


# dense = np.ones(r)
list_dense = age65_rate
json_dense = json.dumps(list_dense)
print("dense:")
print(list_dense)
with open('data/city_sample/dense.json', 'w') as f:
    f.write(json_dense)

pop = np.multiply(age65_rate, np.divide(population, 100))
list_pop = pop.tolist()
json_pop = json.dumps(list_pop)
print("pop:")
print(list_pop)
with open('data/city_sample/pop.json', 'w') as f:
    f.write(json_pop)

start = np.zeros((16, 8))
for i in range(16):
    start[i, :] = np.random.dirichlet(np.ones(8))
list_start = start.tolist()
json_start = json.dumps(list_start)
print("start:")
print(list_start)
with open('data/city_sample/start.json', 'w') as f:
    f.write(json_start) 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("device:")
print(device)