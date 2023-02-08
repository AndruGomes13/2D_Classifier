import torch
import random

class KNN:
    def __init__(self, n=1):
        self.n = n

    def classify_point(self, coord, dot_list, dot_class):
        point = torch.tensor(coord).float()
        dots = torch.tensor(dot_list).float()

        c = ((point-dots)**2).sum(1)
        d = torch.argsort(c)
        indices = []
        for i in range(self.n):
            index = (d == i).nonzero(as_tuple=True)[0]
            indices.append(index)
        
        count = {}
        for ix in indices:
            count[dot_class[ix]] = count.get(dot_class[ix], 0) + 1

        return max(count, key=count.get), count

    def classify_point_notensor(self, coord, dot_list, dot_class):    
        dots = []
        for dot in dot_list:
            dots.append(self.dist_square(coord, dot))
        indices = numpy.argsort(dots).tolist()
        count = {}
        for i in range(self.n):
            ix = indices.index(i)
            count[dot_class[ix]] = count.get(dot_class[ix], 0) + 1

        return max(count, key=count.get), count
        

    def dist_square(self, coord1, coord2):
        return (coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 



size = (200, 200)

dot_list1 = []
dot_class1 = []
for _ in range(15):
    dot_list1.append([random.random() * 0.5, random.random() * 0.5])
    dot_class1.append("green")

for _ in range(15):
    dot_list1.append([random.random() * 0.5 + 0.5, random.random() * 0.5 + 0.5])
    dot_class1.append("red")


model = KNN(10)
point = (0,0)
print(model.classify_point(point, dot_list1 , dot_class1))


screen_size = (10, 10)

a = [[None for _ in range(size[0])] for _ in range(size[0])]

for i in range(size[0]):
    for j in range(size[1]):
        coord = (i / size[0], j / size[1])
        a[i][j] = model.classify_point(coord, dot_list1, dot_class1)[0]

print(a)




