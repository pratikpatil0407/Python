import java.util.* ;
import java.io.*; 
public class temp {
	public static void printPattern(int n){
		// Write your code here.
		int rows = n;
        for (int i = 0; i < rows; i++) {
            // Print spaces to center the stars
            for (int j = 0; j < rows - i - 1; j++) {
                System.out.print(" ");
            }
            // Print stars (2*i + 1 gives the odd number of stars)
            for (int k = 0; k < (2 * i + 1); k++) {
                System.out.print("*");
            }
            // Move to the next line
            System.out.println();
		}
	}
    public static void main(String[] args) {
        temp.printPattern(4);
    }
}
