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

test_2 =[
'#.##.##.##', 
'#######.##', 
'#.#.#..#..', 
'####.##.##', 
'#.##.##.##', 
'#.#####.##', 
'..#.#.....', 
'##########', 
'#.######.#', 
'#.#####.##']



def change_seats(list_array):
  length = len(list_array[0])
  add = ['.' * (length)]
  new_array = add + list_array + add
  new_seating_plan = []

  for line in new_array:
    line = '.' + line + '.'
    line = line.replace('#', '2')
    line = line.replace('L', '1')
    line = line.replace('.', '0')
    new_seating_plan.append(line)

  return new_seating_plan 

# print(change_seats(test))

def return_seats(final_array):
  new_final_array = []
  for x in final_array:
    new_x = x[1:]
    new_new_x = new_x[:-1]
    new_new_x = new_new_x.replace('2', '#')
    new_new_x = new_new_x.replace('1', 'L')
    new_new_x = new_new_x.replace('0', '.')
    new_final_array.append(new_new_x)
  return new_final_array

# print(return_seats(new_test))

def seat_count(array):
  total_count = 0
  for seat in array:
    x = seat.count('2')
    total_count += x
  return total_count

# def test_limits(array):
#   index_of_line = 1
#   index_in_line = 1
#   print(array[index_of_line - 1][index_in_line - 1])
#   print(array[index_of_line - 1][index_in_line])
#   print(array[index_of_line - 1][index_in_line + 1])
#   print(array[index_of_line][index_in_line - 1])
  # print(array[index_of_line][index_in_line])
  # print(array[index_of_line][index_in_line + 1])
  # print(array[index_of_line + 1][index_in_line - 1])
  # print(array[index_of_line + 1][index_in_line])
  # print(array[index_of_line + 1][index_in_line + 1])

# print(test_limits(new_test))

def find_seats(array):
  index_of_line = 1
  index_in_line = 1
  new_array = []
  changed_array = change_seats(array)
  while index_of_line < len(changed_array) - 1:
    while index_in_line < len(changed_array[0]) - 1:

      if changed_array[index_of_line][index_in_line] == '2':
        if (int(changed_array[index_of_line - 1][index_in_line - 1]) + int(changed_array[index_of_line - 1][index_in_line]) + int(changed_array[index_of_line - 1][index_in_line + 1]) + int(changed_array[index_of_line][index_in_line - 1]) + int(changed_array[index_of_line][index_in_line + 1]) + int(changed_array[index_of_line + 1][index_in_line - 1]) + int(changed_array[index_of_line + 1][index_in_line]) + int(changed_array[index_of_line + 1][index_in_line + 1])) >= 8:
          new_line = changed_array[index_of_line].replace('2', '1', index_in_line)
        else:
          new_line = changed_array[index_of_line]

      if changed_array[index_of_line][index_in_line] == '1':
        if (int(changed_array[index_of_line - 1][index_in_line - 1]) + int(changed_array[index_of_line - 1][index_in_line]) + int(changed_array[index_of_line - 1][index_in_line + 1]) + int(changed_array[index_of_line][index_in_line - 1]) + int(changed_array[index_of_line][index_in_line + 1]) + int(changed_array[index_of_line + 1][index_in_line - 1]) + int(changed_array[index_of_line + 1][index_in_line]) + int(changed_array[index_of_line + 1][index_in_line + 1])) < 1:
          new_line = changed_array[index_of_line].replace('1', '2', index_in_line)
        else:
          new_line = changed_array[index_of_line]

      if changed_array[index_of_line][index_in_line] == '0':
        new_line = changed_array[index_of_line]

      index_in_line += 1
    new_array.append(new_line)
    
    index_in_line = 1
    index_of_line += 1
  return return_seats(new_array)
    

print(find_seats(test_2))




