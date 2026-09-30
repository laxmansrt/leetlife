import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length() - 1; i++) {
            String pair = s.substring(i, i + 2);

            map.put(pair, map.getOrDefault(pair, 0) + 1);
        }

        int answer = 0;

        for (int count : map.values()) {
            if (count >= 2) {
                answer++;
            }
        }

        System.out.println(answer);

        sc.close();
    }
}