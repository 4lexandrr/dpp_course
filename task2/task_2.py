import numpy as np


def triangle(a):
    for i in range(a + 1):
        print(' ' * (a - i) + '*' * (i * 2 + 1) , end='\n')

def histDistanve(hist1, hist2)->float:
    square = np.square(hist2 - hist1)
    sum_square = np.sum(square)

    return np.sqrt(sum_square) 

def writeHist(hist1, hist2):
    with open("task2/hist.txt", "w") as file:
        hist1 = hist1.tolist()
        hist2 = hist2.tolist()
        file.write(' '.join((str(x) for x in hist1)))
        file.write('\n')
        file.write(' '.join((str(x) for x in hist2)))

def readHist():
    data = np.loadtxt('task2/readhist.txt', delimiter=' ', dtype=np.int32)

    return data

if __name__ == '__main__':
    triangle(5)

    n = 20  # Vector dimension
    h1, h2 = readHist()


    cartesian_distance = histDistanve(h1, h2)
    print(f'cartesian_distance = {cartesian_distance}')

    writeHist(h1, h2)
