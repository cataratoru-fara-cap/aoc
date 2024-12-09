D = open('input.txt').read().strip()
D = [(i//2 if i%2 else None, int(d)) for i,d in enumerate(D, 1)]

for i in range(len(D))[::-1]:
    for j in range(i):
        i_data, i_size = D[i]
        j_data, j_size = D[j]

        if i_data is not None and j_data is None and i_size <= j_size:
            D[i] = (None, i_size)
            D[j] = (None, j_size - i_size)
            D.insert(j, (i_data, i_size))


# flatten = lambda x: [x for x in x for x in x]
# print(sum(i*c for i,c in enumerate(flatten([d]*s for d,s in D)) if c))
# print(D)

flatened = []

for i, j in D:
    flatened += [i] * j
# print(flatened)
print(sum(i*num for i, num in enumerate(flatened) if num))