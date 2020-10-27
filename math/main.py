import matplotlib.pyplot as plt
import numpy as np


"""
для запуска раскомментировать блоки кода
"""

""" 
x**2
# D(f) = (-inf:inf)
y = lambda x: x**2
fig = plt.subplots()
x = np.linspace(-10, 10, 100)
plt.plot(x, y(x))
plt.show()
"""

"""
x**3
D(f) = (-inf:inf)
y = lambda x: x**3
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
x**(2*n)
D(f) = (-inf:inf)
y = lambda x,n: x**(2*n)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x, randint(-10, 10)))
plt.show()
"""

"""
x**(3*n)
D(f) = (-inf:inf)
y = lambda x,n: x**(3*n)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x, randint(1, 10)))
plt.show()
"""

"""
1/x
D(f) = (-inf:0) U (0:inf)
y = lambda x: 1 / x
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
1/x**2
D(f) = (-inf:0) U (0:inf)
y = lambda x: 1 / x**2
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
sqrt(x)
D(F) = [0:inf)
y = lambda x: np.sqrt(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
cbrt(x)
D(f) = (-inf:0) U (0:inf)
y = lambda x: np.cbrt(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""


"""
Не уверен, что правильно работает
a**x при a > -1, a < 1
y = lambda x, a: a**x
x = np.linspace(-10, 10, 100)
a = np.linspace(-1, 1, 100)
fig = plt.subplots()
plt.plot(x, y(x, a))
plt.show()
"""

"""
sin(x)
d(f) = (-inf:inf)
y = lambda x: np.sin(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""


"""
arcsin(x)
y = lambda x: np.arcsin(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
cos(x)
y = lambda x: np.cos(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
arccos(x)
y = lambda x: np.arccos(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
tan(x)
y = lambda x: np.tan(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""
# arctan(x)
y = lambda x: np.arctan(x)
x = np.linspace(-10, 10, 100)
fig = plt.subplots()
plt.plot(x, y(x))
plt.show()
"""

"""ctg в библиотеке я почему не нашёл"""