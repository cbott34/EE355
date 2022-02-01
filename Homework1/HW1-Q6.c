// C Review Unit: Page 16: Write a short C program (No C++ allowed here) to swap the 2 variables 
// without using a temporary variable. Also, explain the cases (if any) where your program might fail.
#include <stdio.h>
int main()
{
    int x = 0, y = -2;
 
    // Swap 'x' and 'y'
    x = x + y; 
    y = x - y; 
    x = x - y; 
 
    // Print swapped variables
    printf("x = %d, y = %d", x, y);
 
    return 0;
}
