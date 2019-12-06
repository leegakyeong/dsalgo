public class Codeup1905 {
    public static int sum(int n) { // 왜 public static이어야 하는 거지?
        if (n == 1) {
            return n;
        } else {
            return n + sum(n-1);
        }
    }

    public static void main(String[] args) {
        System.out.println(sum(10));
    }
}
