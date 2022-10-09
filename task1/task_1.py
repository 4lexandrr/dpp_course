from statistics import mean
import time
import random
import numpy as np
import matplotlib.pyplot as plt


def calcHist(tdata):
    hist = [0]*10

#   TODO

#   Calculate histogram for tdata List

    # for num in tdata:
    #     if len(str(num)) > 2:
    #         hist[int(str(num)[0])] += 1
    #     else:
    #         hist[0] += 1

    for num in tdata:
        if num < 100:
            hist[0] += 1
        elif 99 < num < 200:
            hist[1] += 1
        elif 199 < num < 300:
            hist[2] += 1
        elif 299 < num < 400:
            hist[3] += 1
        elif 399 < num < 500:
            hist[4] += 1
        elif 499 < num < 600:
            hist[5] += 1
        elif 599 < num < 700:
            hist[6] += 1
        elif 699 < num < 800:
            hist[7] += 1
        elif 799 < num < 900:
            hist[8] += 1
        elif num >= 900:
            hist[9] += 1


    return hist


def initListWithRandomNumbers():
    rand_list = []
    n = 1000000
    for _ in range(n):
        rand_list.append(random.randint(0,999))

    return rand_list


def calcSumm(arr):
    summ = 0
    for val in arr:
        summ += val

    return summ


def draw_hist(arr):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot()

    x = [i for i in range(len(arr))]
    y = np.asarray(arr)
    # ax.hist(y, 10)
    ax.bar(x, y, width=0.5, linewidth=2)
    ax.grid()

    plt.show()


if __name__ == '__main__':
    data = initListWithRandomNumbers()  # lst with 1_000_000 randint
    ans = calcHist(data)
    hist_time = []

    
    start = time.time()
    ans = calcHist(data)
    end = time.time()
    hist_time.append(end - start)

    print(ans)
    print(f'Максимальное время работы: {max(hist_time)}')
    print(f'Среднее время работы: {mean(hist_time)}')
    print(f'Минимальное время работы: {min(hist_time)}')
    draw_hist(hist_time)