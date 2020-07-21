import time


def merge_sort(data, drawbar, delaytime):
    merge_algo(data, 0, len(data)-1, drawbar, delaytime)


def merge_algo(data, left, right, drawbar, delaytime):
    if left < right:
        mid = (left+right)//2
        merge_algo(data, left, mid, drawbar, delaytime)
        merge_algo(data, mid+1, right, drawbar, delaytime)
        merge(data, left, mid, right, drawbar, delaytime)


def merge(data, left, mid, right, drawbar, delaytime):
    drawbar(data, findcolor(len(data), left, mid, right))
    time.sleep(delaytime)

    fir = data[left:mid+1]
    lst = data[mid+1:right+1]

    lind = rind = 0
    for i in range(left, right+1):
        if lind < len(fir) and rind < len(lst):
            if fir[lind] <= lst[rind]:
                data[i] = fir[lind]
                lind += 1
            else:
                data[i] = lst[rind]
                rind += 1

        elif lind < len(fir):
            data[i] = fir[lind]
            lind += 1
        else:
            data[i] = lst[rind]
            rind += 1

    drawbar(data, ['green' if x >= left and x <=
                   right else 'red' for x in range(len(data))])
    time.sleep(delaytime)


def findcolor(length, left, middle, right):
    color = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                color.append("orange")
            else:
                color.append("yellow")
        else:
            if i < left:
                color.append("green")
            elif i > right:
                color.append("red")
    return color
