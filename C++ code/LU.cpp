// Matrices LU factorization
// Taken some parts from https://www.geeksforgeeks.org/doolittle-algorithm-lu-decomposition/

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

void pivot_mat(double a[][SIZE], double id[][SIZE]) {
    
    for (unsigned i =0; i<SIZE; i++) {
        for (unsigned j = i; j<SIZE; j++) {
            if (abs(a[j][i]) > a[i][i]) {
                for (unsigned k = 0; k <SIZE; k++) {
                    swap(a[j][k], a[i][k]);
                    swap(id[j][k], id[i][k]);
                }
            }
        }
    }
}

void lu(double mat[][SIZE], double lower[][SIZE], double upper[][SIZE]) {

    int n = SIZE;
    
    // Decomposing matrix into Upper and Lower
    // triangular matrix
    for (int i = 0; i < n; i++) {
        
        // Upper Triangular
        for (int k = i; k < n; k++) {
            
            // Summation of L(i, j) * U(j, k)
            int sum = 0;
            for (int j = 0; j < i; j++)
                sum += (lower[i][j] * upper[j][k]);
            
            // Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum;
        }
        
        // Lower Triangular
        for (int k = i; k < n; k++) {
            if (i == k)
                lower[i][i] = 1; // Diagonal as 1
            else {
                
                // Summation of L(k, j) * U(j, i)
                int sum = 0;
                for (int j = 0; j < i; j++)
                    sum += (lower[k][j] * upper[j][i]);
                
                // Evaluating L(k, i)
                lower[k][i] = (mat[k][i] - sum) / upper[i][i];
            }
        }
    }
}

int main(int argc, char** argv) {
    
    double a[4][4] = {{1.,0.,-2.,3.},
                      {6.,7.,-1.-1.},
                      {9.,0.,1.,0.},
                      {2.,9.,0.,-7.}};
    
    double id[SIZE][SIZE];
    double PA[SIZE][SIZE];
    double L[SIZE][SIZE];
    double U[SIZE][SIZE];
    
    // Identity matrix inizialization, will be manipulated during pivoting
    for (unsigned i=0; i <SIZE; i++) {
        for (unsigned j=0; j <SIZE; j++) {
            if (i == j) {
                id[i][j] = 1.;
            }
            else id[i][j] = 0.;
        }
    }
    pivot_mat(a, id);  // Computes the pivoting matrix of a
    dot(id, a, PA);
    lu(PA, L, U);
    
    // Displaying results
    cout <<"[ ";
    for (unsigned i = 0; i<4; i++) {
        if (i != 0) cout <<endl;
        for (unsigned j = 0; j<4; j++) {
            cout << L[i][j] <<", ";
        }
    }
    cout <<"]"<<endl<<endl;
    
    cout <<"[ ";
    for (unsigned i = 0; i<4; i++) {
        if (i != 0) cout <<endl;
        for (unsigned j = 0; j<4; j++) {
            cout << U[i][j] <<", ";
        }
    }
    cout <<"]"<<endl;

    return 0;
}
