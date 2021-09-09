# import numpy as np

# a = [1,2]
# b = ([5] * len(a))

# print(a)
# print(b)

# def get_discrete_size(state):
#         discrete_state = (np.array(state) - b) / [2, 2]
#         return discrete_state.astype(np.int).tolist()

# print(get_discrete_size(a))


# def get_discrete_velocities(high, low = 0.0):
#     discrete_actions_number = 4
#     veloc = [low]
#     for i in range(1, discrete_actions_number):
#         veloc.append(i * (high/(discrete_actions_number - 1)))
#     return veloc

# print(get_discrete_velocities(7))

# def combine_actions(veloc_list, ang_list):
#         resultado = []
#         for i in veloc_list:
#             for j in ang_list:
#                 resultado.append([i, j])
#         return resultado

# actions = combine_actions([1,2,3], [4,5,6])
# print(actions)
# for i in actions:
#     print(i)

# print(actions[0])

# a = 5
# print(a)
# print(type(a))
# a = 'a'
# print(a)
# print(type(a))


# import sys
# for line in sys.stdin:
#     if 'Exit' == line.rstrip():
#         break
#     print(f'Processing Message from sys.stdin *****{line}*****')
# print("Done")


# from sys import argv
# print(__name__)
# print(argv)



