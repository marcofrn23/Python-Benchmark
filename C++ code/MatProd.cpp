// Matrices Product

#include <iostream>
#include <cmath>

// Choose matrices here, must be square (nxn)
#define MATRIX1 {{1.,0.,-2.,3.},{6.,7.,-1.-1.},{9.,0.,1.,0.},{2.,9.,0.,-7.}}
#define MATRIX2 {{4.,-1.,-3.,3.},{8.,0.,-1.-0.},{2.,1.,-1.,-3.},{9.,4.,-3.,-2.}}
#define SIZE 4

using namespace std;

// Calculates the matrices product between A and B and uses C as the output matrix
void dot(double A[][SIZE], double B[][SIZE], double C[][SIZE]) {
    
    for (int row = 0; row < SIZE; row++) {
        for (int col = 0; col < SIZE; col++) {
            for (int k = 0; k < SIZE; k++) {
                C[row][col] += A[row][k] * B[k][col];
            }
        }
    }
}

int main(int argc, char** argv) {
    
    // Static inizialization
    double mat1[][4] = MATRIX1;
    double mat2[][4] = MATRIX2;
    double result[][4] = MATRIX1;
    
    dot(mat1,mat2,result);
    
    return 0;
    
}
