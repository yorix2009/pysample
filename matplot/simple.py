# coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
img = BytesIO()
plt.savefig(img, format='png')
img.seek(0)
# img转义base64编码
img_base64 = base64.b64encode(img.getvalue()).decode('utf8')
print('hello',img_base64)
#plt.show()