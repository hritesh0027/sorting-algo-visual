import time


def bubble_sort(data, drawbar, delaytime):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawbar(data, ['green' if x == j or x == j+1 or x >
                               (len(data)-i-1) else 'red' for x in range(len(data))])
                time.sleep(delaytime)
    drawbar(data, ['green' for x in range(len(data))])
