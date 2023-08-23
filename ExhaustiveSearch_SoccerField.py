from datetime import datetime
'''
soccer_field = [".", ".", ".", ".", ".", ".", "X", ".", "X",
                "X", ".", ".", ".", ".", ".", ".", ".", ".",
                ".", ".", ".", "X", ".", ".", ".", "X", ".",
                ".", ".", "X", ".", ".", ".", ".", "X", ".",
                ".", "X", ".", ".", ".", ".", "X", ".", ".",
                ".", ".", ".", ".", "X", ".", ".", ".", ".",
                ".", ".", "X", ".", ".", ".", ".", ".", "X",
                ".", ".", ".", ".", ".", ".", ".", ".", "."]
'''
#start timer
start_time = datetime.now()

#Create field
r = 8
c = 9
soccer_field = [['.' for j in range (c)] for i in range (r)]

#Add players
soccer_field[0][6] = 'X'
soccer_field[0][8] = 'X'
soccer_field[1][0] = 'X'
soccer_field[2][3] = 'X'
soccer_field[2][7] = 'X'
soccer_field[3][2] = 'X'
soccer_field[3][7] = 'X'
soccer_field[4][1] = 'X'
soccer_field[4][6] = 'X'
soccer_field[5][4] = 'X'
soccer_field[6][2] = 'X'
soccer_field[6][8] = 'X'

# print the field
for row in soccer_field:
    print(' '.join(row))


def exhaustive_search(field):
  #length of array rows\
  row = len(field)
  #length of colum 0/columns of field
  column = len(field[0])


  #total num of moves
  total_moves = row + column - 2
  #all possible moves
  maxNum = 2**total_moves
  counter = 0

  for bits in range(0, maxNum - 1):
      candidate = []

      for current in range(0, total_moves):
          bit = (bits >> current) & 1
          if bit == 1:
          #if the current'TH bit of bits (all possible moves) is 1 (True/move is allowed)
          #move right
              candidate.append((0,1)) 
          else:
          #move down
              candidate.append((1,0))

      #now we check the candidates to see if they are valid
      down = 0
      right = 0

      #set the goal to be the bottom right of the array
      goal_row = row - 1
      goal_column = column - 1
      valid = True

      for i, j in candidate:
          down += i
          right += j

          #check boundry of current location
          #if i is greater than row, j is greater than col, or location is X, break

          if down >= row or right >= column or field[down][right] == "X":
              valid = False
              break
      #now, lets see if the goal was reached
      if valid:
          if down == goal_row and right == goal_column:
              counter += 1            
  return counter

total_paths = exhaustive_search(soccer_field)
print("There are", total_paths,"available paths in your soccer field by Exhaustive Search")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))