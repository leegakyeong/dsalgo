import java.util.Scanner;

public class Codeup1905 {
    public static int sum(int n) {
        if (n == 1) {
            return n;
        } else {
            return n + sum(n-1);
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int i = s.nextInt();
        System.out.println(sum(i));
    }
}
