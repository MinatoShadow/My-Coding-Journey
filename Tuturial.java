import java.util.Scanner; // Import Scanner class for taking user input

public class Tuturial {
    public static void main(String[] args) {

        // Variables to store rectangle dimensions, unit and area
        double length = 0;
        double breadth = 0;
        double area = 0;
        String unit;

        // Create Scanner object to read input from keyboard
        Scanner scanner = new Scanner(System.in);

        // Ask user for length of rectangle
        System.out.print("Enter length of rectangle: ");
        length = scanner.nextDouble(); // Read length

        // Ask user for breadth of rectangle
        System.out.print("Enter breadth of rectangle: ");
        breadth = scanner.nextDouble(); // Read breadth

        // Consume the leftover newline character
        scanner.nextLine();

        // Ask user for unit of measurement
        System.out.print("Enter Unit: ");
        unit = scanner.nextLine(); // Read unit

        // Calculate area of rectangle
        area = length * breadth;

        // Display the calculated area with unit
        System.out.print("Area of rectage is " + area + unit + "²");

        // Close the scanner to free resources
        scanner.close();
    }
}
