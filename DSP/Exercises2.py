import numpy as np
import matplotlib.pyplot as plt

def getSine(duration = 1, samplerate = 100, amplitude= 1, frequency= 1, phase_shift=0, time_shift = 0):
    y = np.array([])
    x = np.arange(0, duration, 1/samplerate)
    for i in x:
        angle_rad = np.deg2rad((((i - (time_shift / 100))  * 360) - phase_shift) * frequency % 360)
        y = np.append(y, np.sin(angle_rad) * amplitude)
    return x,y

x1, y1 = getSine()
x2, y2 = getSine(1, 100, 0.5, 3, 90, 0)

n_averager = 20
averager = np.array([1 / n_averager] * n_averager)

plt.figure(figsize=(10,5))
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x2,np.convolve(y2, averager, mode='same'))
plt.title('Sinus over time')
plt.xlabel('time in seconds')
plt.ylabel('sinus value')
plt.show()
