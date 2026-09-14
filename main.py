import math
import random
import matplotlib.pyplot as plot

def get_average(points):
	x_total = 0
	y_total = 0
	for point in points:
		x_total += point[0]
		y_total += point[1]
	return x_total / len(points), y_total / len(points)

def sum_list(l, f):
    out = 0
    for item in l:
        out += f(item)
    return out

def get_points(f, r):
    out = []
    for x in r:
        out += [(x, f(x))]
    return out

def get_stuff(points):
    average_x, average_y = get_average(points)

    sxx = sum_list(points, lambda point: (point[0] - average_x) ** 2)
    syy = sum_list(points, lambda point: (point[1] - average_y) ** 2)
    sxy = sum_list(points, lambda point: (point[0] - average_x) * (point[1] - average_y))
    
    gradient_sum = sum_list(points, lambda p: (p[1] - average_y) / (p[0] - average_x))

    return {
        "r": sxy / math.sqrt(sxx * syy),
        "gradient": gradient_sum / len(points),
        "average_x": average_x,
        "average_y": average_y,
    }

X_MIN = 0
X_MAX = 100
X_STEP = 1
RANDOM_PLUS_MINS = 5
PLOT_FUNC = lambda x: x + (random.random() - 0.5) * RANDOM_PLUS_MINS

points = get_points(PLOT_FUNC, range(X_MIN, X_MAX, X_STEP))

# Write the graph to a file
plot.scatter(
    list(map(lambda p: p[0], points)),
    list(map(lambda p: p[1], points)),
)
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.savefig("plot.png", dpi=300)

# Print the r value
stuff = get_stuff(points)
print(stuff)