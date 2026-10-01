import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            long ans = 0;

            // First k-1 withdrawals give 2 each
            ans = 2L * (k - 1);

            // Last withdrawal gets all the remaining growth
            ans += (1L << (n - k + 1));

            System.out.println(ans);
        }

        sc.close();
    }
}