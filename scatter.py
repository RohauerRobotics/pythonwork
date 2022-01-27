import matplotlib.pyplot as plt
import numpy as np

deg3 = [2.9,11.8,5.1,0.8603,0.8273]
deg5 = [3.3,14.6,6.5,1.119,1.083]
deg8 = [3.4,15.6,7,1.128,1.1]
deg10 = [3.8,19.6,9.1,1.52,1.476]
deg12 = [4,27.1,13.4,2.261,2.131]

full_list = [deg3,deg5,deg8,deg10,deg12]


N = 100
r0 = 0.6
xvals = []
yvals = []
for x in range(0, len(full_list)):
    xvals.append(np.sin(full_list[awdax][2]))

for y in range(0, len(full_list)):
    yvals.append(full_list[y][4])


y = 0.9 * np.random.rand(N)
area = 2  # 0 to 10 point radii
plt.scatter(xvals, yvals)
# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
