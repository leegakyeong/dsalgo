import java.util.Scanner;

public class Codeup1920 {

    static String result = "";

    public static String decimalToBinary(int n) {
        if (n == 0 || n == 1) {
            result = Integer.toString(n) + result;
            return result;
        } else {
            result = Integer.toString(n%2) + result;
            return decimalToBinary(n/2);
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int i = s.nextInt();
        System.out.println(decimalToBinary(i));
    }
}
