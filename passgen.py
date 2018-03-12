import itertools
ab = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
len_pass = 4
pwd = [''.join(x) for x in list(itertools.combinations(ab, len_pass))]
print("LIB SOLUTION:")
print(pwd)
pwd = []


def combination(arr, n, r):
    data = arr[0:r]
    combination_util(arr, data, 0, n-1, 0, r)


def combination_util(arr, data, start, end, index, r):
    if index == r:
        el = ""
        for j in range(0, r):
            el += data[j]
        pwd.append(el)
        return
    i = start
    while i <= end and end-i+1 >= r-index:
        data[index] = arr[i]
        combination_util(arr, data, i+1, end, index+1, r)
        i += 1


combination(ab, len(ab), len_pass)
print("MY SOLUTION:")
print(pwd)
