//  Evaluating an ODE with Runge-Kutta's method of 4th order

#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

double eval(double t, double x) {
    return 3*pow(2,t) +  pow(t,2) + 4*x;
}

void solve(double x0, double t0, double T, unsigned N, double times[], double sol[]) {
    
    double dt = .0;
    dt = (double)(T-t0)/N;
    sol[0] = x0;
    double mid = dt/2.0;
    
    for (unsigned i = 1; i<N; i++) {
        double tau = times[i-1];
        double k1 = eval(tau, sol[i-1])*dt;
        double k2 = eval(mid+tau, sol[i-1]+k1/2.0)*dt;
        double k3 = eval(mid+tau, sol[i-1]+k2/2.0)*dt;
        double k4 = eval(dt+tau, sol[i-1]+k3)*dt;
        
        sol[i] = sol[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6.0;
    }
}

int main(int argc char** argv) {
    unsigned N = 30;
    
    double t0 = 0.0;
    double x0 = 1.0;
    
    double T = 10.0;
    
    double times[N];
    double sol[N];

    solve(x0, t0, T, N, times, sol);

    cout <<"SOLUTIONS: [";
    for (unsigned i =0; i<N; i++) {
        cout <<sol[i] <<", ";
    }
    cout <<"]" <<endl;
    
    return 0;
}
