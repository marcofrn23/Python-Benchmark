#include <iostream>
#include <ctime.h>

using namespace std;

void TEST() {
    // Define input Parameters here
    
    unsigned nt = 20;
    double test[nt];
    double sum = .0;
    double avg, max, min = .0;
    
    for (unsigned i =0; i<nt; i++) {
        clock_t start = clock();
        // Call to function with given inputs here
        clock_t end = clock();
        test[i] = ((double)(end-start))/CLOCKS_PER_SEC;
    }
    max = test[0];
    min = max;
    for (unsigned i =0; i<nt; i++) {
        sum += test[i];
        if (test[i] > max) swap(test[i], max);
        if (test[i] < min) swap(test[i], min);
    }
    avg = sum/nt;
    
    cout <<"SOLUTIONS: [";
    for (unsigned i =0; i<N; i++) {
        cout <<sol[i] <<", ";
    }
    cout <<"]" <<endl;
    cout <<"TEST:\nFastest: " <<min <<"\nSlowest: " <<max <<"\n**Average**: " <<avg <<endl;

}
int main(int argc, char** argv) {
    TEST();
    
    return 0;
}
