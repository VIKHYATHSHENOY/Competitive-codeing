import java.util.Scanner;

class RotateArray {
    public static void main(String args[] ) throws Exception {
        // Using Scanner for input
        Scanner sc = new Scanner(System.in);
        
        // Number of test cases
        int T = sc.nextInt();
        
        // Loop through each test case
        for (int t = 0; t < T; t++) {
            // Input array size and rotation count for the current test case
            int N = sc.nextInt();
            int K = sc.nextInt();
            int[] A = new int[N];
            
            // Input array elements
            for (int i = 0; i < N; i++) {
                A[i] = sc.nextInt();
            }
            
            // Handle the case where K is larger than N
            K = K % N;
            
            // Rotate the array
            rotateArray(A, N, K);
            
            // Output the rotated array
            for (int i = 0; i < N; i++) {
                System.out.print(A[i] + " ");
            }
            // Move to the next line after each test case output
            System.out.println();
        }
    }
    
    public static void rotateArray(int[] A, int N, int K) {
        // Step 1: Reverse the whole array
        reverse(A, 0, N-1);
        
        // Step 2: Reverse the first K elements
        reverse(A, 0, K-1);
        
        // Step 3: Reverse the remaining N-K elements
        reverse(A, K, N-1);
    }
    
    public static void reverse(int[] A, int start, int end) {
        while (start < end) {
            int temp = A[start];
            A[start] = A[end];
            A[end] = temp;
            start++;
            end--;
        }
    }
}
