def find_element_in_matrix(matrix, element):
    r=len(matrix)
    c=len(matrix[0])
    i=0
    j=c-1
    print("on i, j", i, j)
    print("r, c", r, c)
    while (i<r & j<c):
        if matrix[i][j]==element:
            print("found element ",  element, "at", i, j)
            return i, j
        if matrix[i][j]>element:
            print(matrix[i][j], "element", element, "second if", i, j)
            j -= 1;
        if matrix[i][j]<element:
            print(matrix[i][j], "element", element, "second if", i, j)
            i += 1;

    print("none found")
    return 0

matrix = [[1, 5, 10, 15],
          [4, 8, 12, 16],
          [7, 9, 13, 17]]

element = 18

find_element_in_matrix(matrix, element)





