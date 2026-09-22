import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd

# 1
x = np.arange(0,1,0.01)
# print(time)

# 2
y1 = np.array([])
for i in x:
    angle_rad = np.deg2rad(i * 360)
    y1 = np.append(y1, np.sin(angle_rad))

# print(sinus)

# 3
# plt.figure(figsize=(10,5))
# plt.stem(x,y1)
# plt.title('Sinus over time', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
# plt.xlabel('time in seconds')
# plt.ylabel('sinus value')
# plt.show()

# 4
y2 = np.array([])
for i in x:
    angle_rad = np.deg2rad(((i * 360) * 3) % 360 )
    y2 = np.append(y2, np.sin(angle_rad) * 0.5)

# 5   
# plt.figure(figsize=(10,5))
# plt.stem(x,y2)
# plt.title('Sinus over time', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
# plt.xlabel('time in seconds')
# plt.ylabel('sinus value')
# plt.show()


fig, axs = plt.subplots(1, 3, figsize=(18,5))
axs[0].stem(x, y1)
axs[0].set_title('Sinus over time')
axs[0].set_xlabel('time in seconds')
axs[0].set_ylabel('sinus value')
axs[1].stem(x, y2)
axs[1].set_title('3 Sinuses over time')
axs[1].set_xlabel('time in seconds')
axs[1].set_ylabel('sinus value')
axs[2].stem(x, y1 + y2)
axs[2].set_title('Combined Sinuses over time')
axs[2].set_xlabel('time in seconds')
axs[2].set_ylabel('sinus value')
plt.tight_layout()
plt.show()