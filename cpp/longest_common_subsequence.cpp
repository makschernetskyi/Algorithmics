#include <iostream>
#include <string>
#include <algorithm>
using namespace std;




int main()
{
    string str1, str2;
    cin >> str1 >> str2;

    int len1 = str1.size(), len2 = str2.size();

    int dp[len1+1][len2+1];
    for(int i = 0; i<=len1; i++){
        dp[i][0] = 0;
    }
    for(int j = 0; j<=len2; j++){
        dp[0][j] = 0;
    }

    for(int i = 1; i<=len1; i++){
        for(int j = 1; j<=len2; j++){
            if(str1[i-1] == str2[j-1]){
                dp[i][j] = dp[i-1][j-1]+1;
            }else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    int maxV = dp[len1][len2];


    cout << maxV << endl;
    char letters[maxV];
    int l = maxV-1;
        for(int j = len2, i = len1; j>0&&i>0;){
            if(dp[i-1][j]==dp[i][j]){
                i--;
            }else if(dp[i][j-1]==dp[i][j]){
                j--;
            }else if(dp[i-1][j-1]==dp[i][j]-1){

                letters[l] = str1[i-1];
                l--;
                j--;
            }
        }
    for(char c:letters){
        cout<<c;
    }

}
