n = int(input("Enter size of square matrix: "))
  
current_vertical_direction = 0
current_horizontal_direction = 1

matrix = [[0 for x in range(0, n)] for y in range(0, n)]

posX = 0
posY = 0

c = 1
while(matrix[posY][posX] == 0):
    matrix[posY][posX] = c
    c += 1
    
    new_posX = posX + current_horizontal_direction
    new_posY = posY + current_vertical_direction
    condition1 = new_posX < 0 or new_posX >= n or new_posY < 0 or new_posY >= n
    condition2 = False
    if(not condition1):
        condition2 = matrix[new_posY][new_posX] != 0
    
    if(condition1 or condition2):
        if(current_horizontal_direction == 0):
            current_horizontal_direction = -current_vertical_direction
            current_vertical_direction = 0
        else:
            current_vertical_direction = current_horizontal_direction
            current_horizontal_direction = 0
        
    posX = posX + current_horizontal_direction
    posY = posY + current_vertical_direction

for x in matrix:
    for y in x:
        print(f"{y}\t", end="")
    print()
