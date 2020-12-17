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

# print(len(test))


def add_seats(list_array):
  length = len(list_array[0])
  add = ['.' * (length)]
  new_array = add + list_array + add
  new_seating_plan = []

  for line in new_array:
    line = '.' + line + '.'
    line = line.replace('L', '1')
    line = line.replace('.', '0')
    new_seating_plan.append(line)

  return new_seating_plan 
  
# print(add_seats(test))

new_test = [
'000000000000', 
'010110110110', 
'011111110110', 
'010101001000', 
'011110110110', 
'010110110110', 
'010111110110', 
'000101000000', 
'011111111110', 
'010111111010', 
'010111110110', 
'000000000000']

new_new_test = [
'000000000000', 
'000101000000', 
'001110100000',
'000000000000'
]

def find_seats(array):
  index_of_line = 1
  index_in_line = 1
  new_array = []

  while index_of_line < len(array) - 1:
    while index_in_line < len(array[0]) - 1:

      if array[index_of_line][index_in_line] == '1':
        if (int(array[index_of_line - 1][index_in_line - 1]) + int(array[index_of_line - 1][index_in_line]) + int(array[index_of_line - 1][index_in_line + 1]) + int(array[index_of_line][index_in_line - 1]) + int(array[index_of_line][index_in_line + 1]) + int(array[index_of_line + 1][index_in_line - 1]) + int(array[index_of_line + 1][index_in_line]) + int(array[index_of_line + 1][index_in_line + 1])) <= 8:
          array[index_of_line] = array[index_of_line].replace('1', '2', index_in_line)
          
      index_in_line += 1
    new_array.append(array[index_of_line])
    
    index_in_line = 1
    index_of_line += 1
  return new_array
    

print(find_seats(new_test))


def test_limits(array):
  index_of_line = 1
  index_in_line = 1
  print(array[index_of_line - 1][index_in_line - 1])
  print(array[index_of_line - 1][index_in_line])
  print(array[index_of_line - 1][index_in_line + 1])
  print(array[index_of_line][index_in_line - 1])
  # print(array[index_of_line][index_in_line])
  print(array[index_of_line][index_in_line + 1])
  print(array[index_of_line + 1][index_in_line - 1])
  print(array[index_of_line + 1][index_in_line])
  print(array[index_of_line + 1][index_in_line + 1])

# print(test_limits(new_test))