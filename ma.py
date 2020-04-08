import numpy as np

def moving_average(arr, l):
	lenarr = len(arr)

	if lenarr % 2 == 1 and l % 2 == 1:
		return conv(arr, l)
	elif lenarr % 2 == 0 and l % 2 == 1:
		return np.append(conv(arr[:lenarr - 1], l), arr[-1])
	elif lenarr % 2 == 1 and l % 2 == 0:
		return conv(arr, l-1)
	else:
		return np.append(conv(arr[:lenarr - 1], l - 1), arr[-1])

def conv_left(arr):
	lenarr = len(arr)

	if lenarr == 1:
		return arr
	else:
		left = conv_left(arr[:lenarr - 2])
		center = np.convolve(arr, np.ones(lenarr) / float(lenarr), mode='valid')
		return np.hstack((left, center))

def conv_right(arr):
	lenarr = len(arr)

	if lenarr == 1:
		return arr
	else:
		center = np.convolve(arr, np.ones(lenarr) / float(lenarr), mode='valid')
		right = conv_right(arr[2:])
		return np.hstack((center, right))

def conv(arr, l):
	lenarr = len(arr)

	if lenarr == 1:
		return arr
	elif lenarr < l:
		return conv(arr, l - 2)
	else :
		left = conv_left(arr[:l - 2])
		center = np.convolve(arr, np.ones(l) / float(l), mode='valid')
		right = conv_right(arr[lenarr - l + 2:])

		return np.hstack((left, center, right))

if __name__ == "__main__":
	arr = np.array([i for i in range(31)])
	print(moving_average(arr, 9))
