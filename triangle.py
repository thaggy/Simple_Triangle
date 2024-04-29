import math

# Returns and prints out a equilateral triangle of X size
def Triangle(size):
    # Columns will be Size, Rows are Columns*2 -1
    line_length = (size * 2) -1
    # Creating 2D array
    triangle_array = [[' ' for i in range(line_length)] for j in range(size)]
    # Boolean used to basically not check bad memory
    has_made_tip = False
    # Getting the middle point of the triangle
    middle_point = math.ceil(line_length/2)
    for i in range(size):
        for j in range(line_length):
            # If we have not made the top tip of the triangle yet and we hit the middle of the top row
            if i == 0 and j+1 == middle_point and not has_made_tip:
                # Then that will the the tip of the triangle
                triangle_array[i][j] = 'x'
                # We have now made the tip
                has_made_tip = True
            # We check if we have made the tip first so we dont check out of bounds of the array
            if has_made_tip:
                # Checking diagnol right on the left side
                if j+1 < middle_point and triangle_array[i-1][j+1] == 'x':
                    triangle_array[i][j] = 'x'
                # Checking diagnol left on the right side
                if j+1 > middle_point and triangle_array[i-1][j-1] == 'x':
                    triangle_array[i][j] = 'x'
                # If we are at the bottom row, then that will be all Xs
                if i+1 == len(triangle_array):
                    triangle_array[i][j] = 'x'
    # Printing it out nice and pretty :)
    for row in triangle_array:
        print(*row, sep="\t")
    # Return the array
    return triangle_array
        
# Call Triangle of X size
Triangle(14)