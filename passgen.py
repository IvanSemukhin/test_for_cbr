ALPHA_BETA = ['9', '0', '1', '2', '3', '4', '5', '6', '7', '8']
LEN_ALPHA = len(ALPHA_BETA)
LEN_PASSWORD = 4


def shift(lst):
    tmp = lst[1:LEN_ALPHA]
    tmp.append(lst[0])
    return tmp


def init():
    tmp = []
    global ALPHA_BETA
    for n in range(0, LEN_PASSWORD):
        ALPHA_BETA = shift(ALPHA_BETA)
        tmp.append(ALPHA_BETA)
    return tmp


lock = init()
# for el in lock:
#     print(el)
# print("")

all_pwd = []
for z in range(1, LEN_PASSWORD):
    for k in range(1, LEN_ALPHA-LEN_PASSWORD):
        for i in range(0, LEN_ALPHA):
            pwd = ""
            for j in range(0, LEN_PASSWORD):
                pwd += lock[j][i]
            all_pwd.append(pwd)
        lock[-z] = shift(lock[-z])
        # print("OLOLO = ", -z)
        # for el in lock:
        #     print(el)

# for el in all_pwd:
#     if '0' in el and '3' in el and '6' in el and '7' in el:
#         print(el)
#     if '1' in el and '2' in el and '6' in el and '8' in el:
#         print(el)
#     if '4' in el and '5' in el and '7' in el and '9' in el:
#         print(el)

ALPHA_BETA = ['9', '0', '1', '5', '4', '3', '2', '6', '7', '8']

lock = init()
# for el in lock:
#     print(el)
# print("")

for z in range(1, LEN_PASSWORD):
    for k in range(1, LEN_ALPHA-LEN_PASSWORD):
        for i in range(0, LEN_ALPHA):
            pwd = ""
            for j in range(0, LEN_PASSWORD):
                pwd += lock[j][i]
            all_pwd.append(pwd)
        lock[-z] = shift(lock[-z])

print(len(all_pwd))

for el in all_pwd:
    if '0' in el and '3' in el and '6' in el and '7' in el:
        print(el)
    if '1' in el and '2' in el and '6' in el and '8' in el:
        print(el)
    if '4' in el and '5' in el and '7' in el and '9' in el:
        print(el)
    if '4' in el and '3' in el and '0' in el and '9' in el:
        print(el)