import time


def partition(data, start, end, drawbar, delaytime):
    border = start
    pivot = data[end]

    barcolor = findcolor(len(data), start, end, border, border)
    drawbar(data, barcolor)
    time.sleep(delaytime)

    for j in range(start, end):
        if data[j] < pivot:
            barcolor = findcolor(len(data), start, end, border, j, True)
            drawbar(data, barcolor)
            time.sleep(delaytime)

            data[border], data[j] = data[j], data[border]
            border += 1

        barcolor = findcolor(len(data), start, end, border, j)
        drawbar(data, barcolor)
        time.sleep(delaytime)

    barcolor = findcolor(len(data), start, end, border, end, True)
    drawbar(data, barcolor)
    time.sleep(delaytime)

    data[border], data[end] = data[end], data[border]
    return border


def quick_sort(data, start, end, drawbar, delaytime):
    if start < end:
        partionind = partition(data, start, end, drawbar, delaytime)
        quick_sort(data, start, partionind-1, drawbar, delaytime)
        quick_sort(data, partionind+1, end, drawbar, delaytime)


def findcolor(len, start, end, border, ind, swap=False):
    barcolor = []
    for i in range(len):
        if i >= start and i <= end:
            barcolor.append('red')
        else:
            barcolor.append('green')

        if i == end:
            barcolor[i] = 'blue'
        elif i == border:
            barcolor[i] = 'blue'
        elif i == ind:
            barcolor[i] = 'yellow'

        if swap:
            if i == border or i == ind:
                barcolor[i] = 'grey'
    return barcolor
