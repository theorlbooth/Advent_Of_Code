adapters = [
152, 
18, 
146, 
22, 
28, 
133, 
114, 
67, 
19, 
37, 
66, 
14, 
90, 
163, 
26, 
149, 
71, 
106, 
46, 
143, 
145, 
12, 
151, 
105, 
58, 
130, 
93, 
49, 
74, 
83, 
129, 
122, 
63, 
134, 
86, 
136, 
166, 
169, 
159, 
3, 
178, 
88, 
103, 
97, 
110, 
53, 
125, 
128, 
9, 
15, 
78, 
1, 
50, 
87, 
56, 
89, 
60, 
139, 
113, 
43, 
36, 
118, 
170, 
96, 
135, 
23, 
144, 
153, 
150, 
142, 
95, 
180, 
35, 
179, 
80, 
13, 
115, 
2, 
171, 
32, 
70, 
6, 
72, 
119, 
29, 
79, 
27, 
47, 
107, 
73, 
162, 
172, 
57, 
40, 
48, 
100, 
64, 
59, 
175, 
104, 
156, 
94, 
77, 
65, 
0]


test = [
16, 
10, 
15, 
5, 
1, 
11, 
7, 
19, 
6, 
12, 
4
]

test_2 = [
28, 
33, 
18, 
42, 
31, 
14, 
46, 
20, 
48, 
47, 
24, 
23, 
49, 
45, 
19, 
38, 
39, 
11, 
1, 
32, 
25, 
35, 
8, 
17, 
7, 
9, 
4, 
2, 
34, 
10, 
3, 
]

# print(len(adapters))
# print(len(test))
# print(len(test_2))


# def find_gaps(list_array):
#   y = 1
#   x = 0
#   count_one = 0
#   count_three = 0
#   sorted_a = sorted(list_array)
#   max_num = sorted_a[-1] + 3
#   print(max_num)
#   new_array = [0] + [max_num] + list_array
#   sorted_b = sorted(new_array)
#   while y < len(sorted_b):
#     if sorted_b[y] - sorted_b[y-1] == 1:
#       count_one += 1
#     elif sorted_b[y] - sorted_b[y-1] == 3:
#       count_three += 1
#     y += 1
#     x += 1
#   return [count_one, count_three, (count_one * count_three)]

# print(find_gaps(adapters))

#  ! -----------

from itertools import combinations

# a_list = [1, 2, 3]

# all_combinations = []
# for r in range(len(a_list) + 1):
#   combinations_object = combinations(a_list, r)
#   combinations_list = list(combinations_object)
#   all_combinations += combinations_list
# print(all_combinations)


def find_gaps(list_array):
  y = 1
  x = 0
  count_one = 0
  count_three = 0
  sorted_b = sorted(list_array)
  while y < len(sorted_b):
    if sorted_b[y] - sorted_b[y-1] == 1:
      count_one += 1
    elif sorted_b[y] - sorted_b[y-1] == 3:
      count_three += 1
    elif sorted_b[y] - sorted_b[y-1] > 3:
      return
    y += 1
    x += 1
  return 1

# print(find_gaps(test))


def find_num_comb(list_to_check):
  sorted_a = sorted(list_to_check)
  max_num = sorted_a[-1] + 3

  new_array = [0] + [max_num] + sorted_a
  sorted_c = sorted(new_array)

  total_count = 0

  all_combinations = []
  for r in range(len(sorted_c) + 1):
    combinations_object = combinations(sorted_c, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list

  for a in all_combinations:
    abc = list(a)
    if len(abc) != 0:
      if abc[0] == 0 and abc[-1] == max_num:
        if find_gaps(abc) == 1:
          print(abc)
          total_count += 1
  return total_count


print(find_num_comb(test_2))


