#include<iostream>
#include<cmath>
using namespace std;




bool sito(bool primes[],int n){
    for(int i= 1; i< sqrt(n); i++){
  if(primes[i] == true){
   int prime = i+1;
   for(int j = 2; j*prime-1< n; j++){
    primes[j*prime-1] = false;
   }
  }
 }
 return primes;
}




int main()
{
 int n;
 cin >> n;
 bool primes[n];
 fill(primes,primes+n, true);
 primes[0]= false;


 sito(primes,n);


 for(int i=0; i<n;++i){
  if(primes[i]==true){
   cout <<i+1<< " ";
  }
 }





return 0;
}
