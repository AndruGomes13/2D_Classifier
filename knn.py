import torch

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
            count[dot_class[ix]] 
            count[dot_class[ix]] = count.get(dot_class[ix], 0) + 1

        return max(count, key=count.get)

        


    def dist_square(self, coord1, coord2):
        return (coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 


