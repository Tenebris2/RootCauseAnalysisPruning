
#include <stdio.h>

// Function prototypes
void printArray(int arr[], int size);
int sumArray(int arr[], int size);

int main() {
    int numbers[5];
    int i;

    // Input
    printf("Enter 5 integers:\n");
    for (i = 0; i < 5; i++) {
        printf("Number %d: ", i + 1);
        scanf("%d", &numbers[i]);
    }

    // Process
    int sum = sumArray(numbers, 5);

    // Output
    printf("You entered: ");
    printArray(numbers, 5);
    printf("Sum of the numbers: %d\n", sum);

    return 0;
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to compute the sum of an array
int sumArray(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}
