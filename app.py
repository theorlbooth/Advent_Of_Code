test = [
'L.LL.LL.LL', 
'LLLLLLL.LL', 
'L.L.L..L..', 
'LLLL.LL.LL', 
'L.LL.LL.LL', 
'L.LLLLL.LL', 
'..L.L.....', 
'LLLLLLLLLL', 
'L.LLLLLL.L', 
'L.LLLLL.LL']

print(len(test))

def add_seats(list_array):
  length = len(list_array[0])
  add = ['x' * (length)]
  new_array = add + list_array + add
  new_seating_plan = []

  for line in new_array:
    line = 'x' + line + 'x'
    new_seating_plan.append(line)
  return new_seating_plan 
  

print(add_seats(test))