import java.util.*;

class Result {

    public static int simpleArraySum(List<Integer> ar) {
        int sum = 0;

        for (int i = 0; i < ar.size(); i++) {
            sum += ar.get(i);
        }

        return sum;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        List<Integer> ar = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            ar.add(sc.nextInt());
        }

        int result = Result.simpleArraySum(ar);

        System.out.println(result);

        sc.close();
    }
}
