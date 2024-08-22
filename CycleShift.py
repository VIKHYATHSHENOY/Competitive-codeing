def find_kth_occurrence(N, K, A):
    max_bin = A
    current_shift = A
    occurrences = 0
    
    # Find the maximum possible binary string through all shifts
    for i in range(1, N):
        current_shift = current_shift[1:] + current_shift[0]
        if current_shift > max_bin:
            max_bin = current_shift

    # Count how many times the maximum binary string occurs
    total_shifts = 0
    current_shift = A
    for i in range(N * K):  # loop to cover up to K occurrences
        if current_shift == max_bin:
            occurrences += 1
            if occurrences == K:
                return total_shifts
        total_shifts += 1
        current_shift = current_shift[1:] + current_shift[0]

    return -1  # if somehow not found

# Reading input
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = input().strip()
    result = find_kth_occurrence(N, K, A)
    print(result)
