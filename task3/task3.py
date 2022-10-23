import numpy as np

def tosize(a, n=100):
    a = np.asarray(a)
    x = np.zeros(n, dtype=a.dtype)
    m = min(n, len(a))
    x[:m] = a[:m]
    return x

def histDistanve(hist1, hist2):
    square = np.square(tosize(hist2) - tosize(hist1))
    sum_square = np.sum(square)

    return np.sqrt(sum_square) 


class NNClassifier:
    def __init__(self):
        self.type_and_hist = dict()



    def read_file(self):
        with open('task3/texts.txt', 'r', encoding='utf-8') as file:
            for line in file:
                type_text = line[:line.find('=') - 1]
                hist = np.array([round(len(i)/len(line), 3) for i in line[line.find('=') + 1:].split()])

                self.type_and_hist[type_text] = hist


if __name__ == '__main__':
    text = input()
    hist_text = np.array([round(len(i)/len(text), 3) for i in text.split()])

    available_cls = NNClassifier()
    available_cls.read_file()

    res_distance_hist = []
    min_distance = 1
    for k, v in available_cls.type_and_hist.items():
        temp = histDistanve(hist_text, v)
        res_distance_hist.append(temp)
        if temp < min_distance:
            min_distance = temp
            min_type = k
        
    print(res_distance_hist)
    print(f'Новый текст похож на "{min_type}" c расстоянием {min_distance}')
