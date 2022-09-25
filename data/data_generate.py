import numpy as np
import json

start = np.array([np.random.rand(336, 10, 10)])
print(start.shape)

list_start = start.tolist()

json_start = json.dumps(list_start)

with open('data/city_sample/start.json', 'w') as f:
    f.write(json_start)