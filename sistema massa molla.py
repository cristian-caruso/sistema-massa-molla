from matplotlib import pyplot as plt

k = float(input('k = '))
m = float(input('m = '))
b = float(input('b = '))
x0 = float(input('ampiezza: '))

delta_t = 1E-3

v0 = 0
t_i = [0]
x_i = [x0]
v_i = [v0]
a_i = [-k/m*x0-b/m*v0]

for i in range(5000):
    t_i.append((i+1)*delta_t)
    a = -k/m * x_i[i]-b/m*v_i[i]
    a_i.append(a)
    v = v_i[i] + a * delta_t
    v_i.append(v)
    x = x_i[i]+ v_i[i]*delta_t- 0.5*a_i[i]*delta_t**2
    x_i.append(x)

plt.plot(t_i, [0]*len(t_i))
plt.plot(t_i, x_i)
plt.show()
