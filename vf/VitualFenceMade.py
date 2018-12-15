import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111) #创建子图，将画布分割成1行1列，图像画在从左到右从上到下的第1块
rect = plt.Rectangle((0.1,0.1),0.5,0.3) #(左下角的坐标)，宽，高
ax.add_patch(rect)
plt.show()