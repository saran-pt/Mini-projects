def done_or_not(board):
    if check_row(board):    
        if check_coloumn(board):
            if check_box(board):
                return True
    return False  

def check_row(board):  # To check the number in row
    a = []
    for row in board:
        for i in row:
            if i not in a:
                a.append(i)
            else:
                return False
        a = []
    return True
    
def check_coloumn(board): # To check the number in column
    a, y = [], 0
    while y < 9:
        for var in board:
            if var[y] not in a:
                a.append(var[y]) 
            else:
                return False
        y += 1
        a = []
    return True



def check_box(inner): # To check the number in each 3*3 matrix
    val, l1, l2 = [], 0, 3
    while l1 < 9:
        for row in inner:
            for i in range(l1, l2):
                if row[i] not in val:
                    val.append(row[i])
                else:
                    return False
            if len(val)==9:
                print(val)
                val = []
        l1 += 3
        l2 += 3            
    return True        

