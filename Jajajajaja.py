import matplotlib.pyplot as plt
import numpy as np

#Data for plotting
t=np.arange(0,1,0.01)
y=np.sin(2*np.pi*t)

fig,ax=plt.subplots()
ax.plot(t,y)

ax.set(xlabel="time(s)", ylabel="voltage (mV)", title="Grafico del seno")
ax.grid()

fig.savefig("seno.png")
plt.show()
