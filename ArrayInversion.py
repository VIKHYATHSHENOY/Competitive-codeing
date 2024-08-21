def count_inversions(matrix, N):
    inversions = 0
    for i in range(N):
        for j in range(N):
            for p in range(i, N):
                for q in range(j + 1, N):  # Only need to check elements to the right
                    if matrix[i][j] > matrix[p][q]:
                        inversions += 1
            for p in range(i + 1, N):  # Check elements below
                for q in range(j, N):
                    if matrix[i][j] > matrix[p][q]:
                        inversions += 1
    return inversions

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the size of the matrix
    N = int(input())
    
    # Read the matrix
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    
    # Calculate the number of inversions
    result = count_inversions(matrix, N)
    
    # Print the result
    print(result)
