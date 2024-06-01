import matplotlib.pyplot as plt
from numpy import arange
from math import log

constant = lambda n: 1
logarithmic = lambda n: log(n)
linear = lambda n: n
n_log_n = lambda n: n * log(n)
quadratic = lambda n: n ** 2
exponential = lambda n: 2 ** n

sample_range = arange(0.1, 5, 0.1)
plt.plot([constant(n) for n in sample_range], label="O(1)")
plt.plot([logarithmic(n) for n in sample_range], label="O(log n)")
plt.plot([linear(n) for n in sample_range], label="O(n)")
plt.plot([n_log_n(n) for n in sample_range], label="O(n log n)")
plt.plot([quadratic(n) for n in sample_range], label="O(n ** 2)")
plt.plot([exponential(n) for n in sample_range], label="O(2 * n)")

plt.xlabel("Ammount of Elements")
plt.ylabel("Ammount of Iterations")

plt.legend()
plt.show()