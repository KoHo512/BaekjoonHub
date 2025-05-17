import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String isEven = "even";
        
        if (n % 2 == 1) {
            isEven = "odd";
        }
        
        System.out.printf("%d is %s", n, isEven);
    }
}