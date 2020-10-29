import numpy as np

sd = np.array([[0, 2, 0, 3, 0, 0, 9, 0, 0],
               [0, 0, 0, 7, 5, 2, 0, 3, 0],
               [1, 0, 5, 0, 8, 0, 2, 0, 6],
               [6, 0, 0, 0, 3, 8, 7, 5, 1],
               [0, 0, 2, 0, 4, 7, 0, 0, 3],
               [0, 0, 0, 6, 0, 0, 4, 0, 0],
               [0, 0, 9, 0, 0, 3, 5, 1, 0],
               [5, 8, 1, 0, 0, 4, 3, 0, 0],
               [4, 7, 0, 1, 0, 0, 0, 2, 9]])

print(sd)


# Function to check if the user inputs letters instead of integers
def input_check():
    global value, line, column
    while True:
        try:
            value = int(input("Enter a value(1-9): "))
            line = int(input("Enter line(0-8): "))
            column = int(input("Enter column(0-8): "))
            if not value_range(value, line, column):
                continue
            return value, column, line
        except ValueError:
            print("Please enter only numbers, not letters or symbols!")


# Check the range of the value
def value_range(value, line, column):
    if value < 1 or value > 9:
        print("Value out of range!")
        return False
    elif line < 0 or line > 9:
        print("Line out of range!")
        return False
    elif column < 0 or column > 9:
        print("Column out of range!")
        return False
    else:
        return True


input_check()


# check if value is on line or column
def check_lines_rows():
    global line, value, column
    for i in range(9):
        if sd[line][i] == value:
            print(f"Number in row {line} already exists! Try again!")
            return sd
        if sd[i][column] == value:
            print(f"Number in column {column} already exists!")
            return sd


check_lines_rows()


# check if the cell is empty or not( can store if and only the cell is 0) We do this, not to overwrite the cell
def cell_is_empty():
    global line, value, column
    cell_boolean = False
    for i in range(9):
        if sd[line][i] != 0:
            print(f"Cell in line {line} not emtpy!")
            return sd
        if sd[i][column] != 0:
            print(f"Cell in column {column} is not empty!")
            return sd
        if sd[line][i] == 0 and sd[column][i] == 0:
            print("Cell is empty!")
            cell_boolean = True
            add_to_cell(cell_boolean)
            return sd, cell_boolean


# Store the value the user entered, in the cell
def add_to_cell(cell_boolean):
    if cell_boolean:
        sd[line][column] = value
        print(sd)


cell_is_empty()
