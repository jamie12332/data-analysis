import math
import random
import matplotlib.pyplot as plot
import numpy as np

def get_bounds(points):
	x_total = 0
	y_total = 0

	x_min = points[0][0]
	y_min = points[0][1]

	x_max = points[0][0]
	y_max = points[0][1]

	for point in points:
		x_total += point[0]
		y_total += point[1]

		if point[0] < x_min:
			min_x = point[0]
		if point[1] < y_min:
			min_y = point[1]

		if point[0] > x_max:
			x_max = point[0]
		if point[1] > y_max:
			y_max = point[1]

	return {
		"x_average": x_total / len(points),
		"y_average": y_total / len(points),

		"x_min": x_min,
		"y_min": y_min,

		"x_max": x_max,
		"y_max": y_max,
	}

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
	stuff = get_bounds(points)

	sxx = sum_list(points, lambda point: (point[0] - stuff["x_average"]) ** 2)
	syy = sum_list(points, lambda point: (point[1] - stuff["y_average"]) ** 2)
	sxy = sum_list(points, lambda point: (point[0] - stuff["x_average"]) * (point[1] - stuff["y_average"]))
	
	gradient_sum = sum_list(points, lambda p: (p[1] - stuff["y_average"]) / (p[0] - stuff["x_average"]))

	stuff["r"] = sxy / math.sqrt(sxx * syy)
	stuff["gradient"] = gradient_sum / len(points)
	stuff["best_fit_line"] = {
        "x0": stuff["x_min"],
        "x1": stuff["x_max"],
        "y0": stuff["y_average"] + ((stuff["x_min"] - stuff["x_average"]) * stuff["gradient"]),
        "y1": stuff["y_average"] + ((stuff["x_max"] - stuff["x_average"]) * stuff["gradient"]),
	}

	return stuff

X_MIN = 0
X_MAX = 100
X_STEP = 1
RANDOM_PLUS_MINS = 20
PLOT_FUNC = lambda x: x + (random.random() - 0.5) * RANDOM_PLUS_MINS

points = get_points(PLOT_FUNC, range(X_MIN, X_MAX, X_STEP))

# Print stuff
stuff = get_stuff(points)
print(stuff)

# Write the graph to a file
plot.scatter(
	list(map(lambda p: p[0], points)),
	list(map(lambda p: p[1], points)),
)
plot.plot(
    [stuff["best_fit_line"]["x0"], stuff["best_fit_line"]["x1"]],
    [stuff["best_fit_line"]["y0"], stuff["best_fit_line"]["y1"]],
    color = "orange",
)
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.savefig("plot.png", dpi=300)
