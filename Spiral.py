def layerTopRight(matrix):
  # remove and store the first row from matrix
    top = matrix.pop(0)

  # store the right column of the matrix
    right = []

  # remove the last column from the matrix
    for i in range(0, len(matrix)):
        e = matrix[i].pop()
        right.append(e)

  # return the top row and last column elements as a list
    return top + right


def layerBottomLeft(matrix):

  # remove and store the last row from matrix in reverse order
    bottom = matrix.pop()[::-1]

  # store the left column of the matrix
    left = []

  # remove the first column from the matrix
    for i in range(0, len(matrix)):
        e = matrix[i].pop(0)
        left.append(e)

  # return the top row and last column elements as a list
    return bottom + left[::-1]

# our main spiral function that will
# return a final spiral ordered list


def spiralPrint(m, n, a):
    k = 0
    l = 0

    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1


# Driver Code
one = [int(i) for i in input().split()]
m = one[0]
n = one[1]
l = []
for i in range(m):
    start_index = (n) * i
    end_index = (n) * (i + 1)
    next_row = one[start_index + 2:end_index + 2]
    l.append(next_row)

spiralPrint(m, n, l)
