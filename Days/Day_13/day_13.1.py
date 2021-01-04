# 1000390
# 23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37

busses = [13, 17, 23, 29, 37, 41, 383, 503]

time = 1000390

def closestNum(n, m):
  q = int(n/m)
  n1 = m * q

  if ((n * m) > 0):
    n2 = (m * (q + 1))
  else:
    n2 = (m * (q - 1))

  if (abs(n - n1) < abs(n - n2)):
    return n1

  return n2 


def find_times(list_array, num):
  for x in list_array:
    new_num = closestNum(num, x)
    if new_num < num:
      final_num = new_num + x
    else:
      final_num = new_num
    
    print([x, final_num])

print(find_times(busses, time))

