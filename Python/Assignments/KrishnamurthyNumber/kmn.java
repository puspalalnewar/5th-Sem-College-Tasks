
// A Krishnamurthy number (also called a Strong number or Peterson number) is a special number in mathematics whose sum of the factorials of its digits is equal to the original number itself.
// Example : 1! + 4! + 5! = 1 + 24 + 120 = 145
import java.util.Scanner;

public class kmn {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your number : ");
        int number = sc.nextInt();
        int store = number;
        int sum = 0;
        while (number > 0) {
            int lastDig = number % 10;
            sum += findFacteriol(lastDig);
            number = number / 10;
        }
        if (store == sum) {
            System.out.println("Yes " + store + " is a Krishnamurty number");
        } else {
            System.out.println("The number " + store + " is not Krishnamurthy number");
        }
    }

    public static int findFacteriol(int n) {
        int facteriol = 1;
        if (n == 0) {
            return 1;
        }
        for (int i = 1; i <= n; i++) {
            facteriol = facteriol * i;
        }
        return facteriol;
    }
}
