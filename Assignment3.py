def most_frequent(string):
    C = dict()
    for key in string:
        if key not in C:
            C[key] = 1
        else:
            C[key] += 1
    return C

print most_frequent('Mississippi')
