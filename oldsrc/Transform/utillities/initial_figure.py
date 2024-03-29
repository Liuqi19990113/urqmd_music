import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
path="../Initial"
x = np.arange(-13, 13.1, 0.1)
y = np.arange(-13, 13.1, 0.1)
X, Y = np.meshgrid(x, y)
x_bin=261
y_bin=261
u1=np.fromfile(path+"/u1.dat").reshape(x_bin,y_bin)
u2=np.fromfile(path+"/u2.dat").reshape(x_bin,y_bin)
ed=np.fromfile(path+"/ed.dat").reshape(x_bin,y_bin)
t00=np.fromfile(path+"/t00.dat").reshape(x_bin,y_bin)
t01=np.fromfile(path+"/t01.dat").reshape(x_bin,y_bin)
t02=np.fromfile(path+"/t02.dat").reshape(x_bin,y_bin)
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(t00).max(), vmin=-abs(t00).max())
csetu1 = ax.contourf(X, Y, t00, 40,norm=norm)
plt.title("t00")
plt.show()
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(ed).max(), vmin=-abs(ed).max())
csetu2 = ax.contourf(X, Y, ed, 40,norm=norm)
plt.title("ed")
plt.show()
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(t01).max(), vmin=-abs(t01).max())
csetu3 = ax.contourf(X, Y, t01, 40,norm=norm)
plt.title("t01")
plt.show()
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(u1).max(), vmin=-abs(u1).max())
csetu4 = ax.contourf(X, Y, u1, 40,norm=norm)
plt.title("u1")
plt.show()
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(t02).max(), vmin=-abs(t02).max())
csetu5 = ax.contourf(X, Y, t02, 40,norm=norm)
plt.title("t02")
plt.show()
fig, ax = plt.subplots()
norm = cm.colors.Normalize(vmax=abs(u2).max(), vmin=-abs(u2).max())
csetu1 = ax.contourf(X, Y, u2, 40,norm=norm)
plt.title("u2")
plt.show()