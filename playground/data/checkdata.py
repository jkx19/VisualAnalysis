import json
import os
from tqdm import tqdm

f = open("llava_v1_5_mix665k.json")
data = json.load(f)
f.close()

new_data = []
abandon = 0
for img in tqdm(data, total=len(data)):
    if "image" not in img.keys():
        # abandon += 1
        continue

    path = img["image"]
    if os.path.exists(path):
        new_data.append(img)
    else:
        print(path)
        abandon += 1


print(len(data))
print(abandon)
f = open("llava_v1_5_mix664k.json", "w")
json.dump(new_data, f)
f.close()
