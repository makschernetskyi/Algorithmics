#include <iostream>
using namespace std;


// Stein's Algorithm is an algorithm to find the greatest
// common divisor of the 2 numbers using bit operators
// it faster than euclidean algorithm, but, in terms of
// complexity it is equal.

int steinsAlgorithm(int a, int b){

    if(a==b){
        return a;
    }
    if(a==0){
        return b;
    }
    if(b==0){
        return a;
    }

    if(~a&1){
        if(b&1){
            return steinsAlgorithm(a>>1, b);
        }else{
            return steinsAlgorithm(a>>1, b>>1)<<1;
        }
    }

    if(~b&1){
        return steinsAlgorithm(a,b >> 1);
    }
    if(a>b){
        return steinsAlgorithm((a-b)>>1,b);
        }
    return steinsAlgorithm((b-a)>>1,a);


}

int main() {
    int a,b;
    cin >> a >> b;


    cout << steinsAlgorithm(a, b);
    return 0;

    }
