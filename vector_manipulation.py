

def vector_length(vector):
    temp = float(0)
    for x in vector:
        temp += x*x
    temp = temp**(1/float(len(vector)))
    return temp


def get_direction(start, end):
    if not len(start) == len(end):
        raise ValueError("get_direction function got Vectors of unequal length as input")
    temp = []
    for i, x in enumerate(start):
        temp.append(end[i]-start[i])
    return temp


def add(vectors):
    vec_len = None
    for vector in vectors:
        if vec_len is None:
            vec_len = len(vector)
        if not len(vector) == vec_len:
            raise ValueError("add function got input vectors of unequal length")
    temp = []
    for i, x in enumerate(vectors[0]):
        temp.append(0)
        for vector in vectors:
            temp[i] += vector[i]
    return temp


# the first vector gets subtracted by all others
def subtract(vectors):
    vec_len = None
    for vector in vectors:
        if vec_len is None:
            vec_len = len(vector)
        if not len(vector) == vec_len:
            raise ValueError("subtract function got input vectors of unequal length")
    temp = vectors[0].copy()
    for i, vector in enumerate(vectors):
        if i == 0:
            continue
        for j, x in enumerate(temp):
            temp[j] -= vector[j]
    return temp


def multiply(vector, factor):
    temp = []
    for i, x in enumerate(vector):
        temp.append(vector[i] * factor)
    return temp


def divide(vector, dividend):
    temp = []
    for i, x in enumerate(vector):
        temp.append(vector[i] / dividend)
    return temp
