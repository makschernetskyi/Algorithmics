#include <iostream>
#include<vector>
#include<math.h>
using namespace std;

struct heap{
    vector<int> _h;
    int size(){
        return _h.size();
    }
    int height(){
        if(size() == 0){return 0;}
        return ceil(log2(size()));
    }
    void pull(int a){
        _h.push_back(a);
        int len = size();
        for(int i = len-1; i>0; ){
                    if(_h[i] > _h[(i-1)/2]){
                        int t = _h[(i-1)/2];
                        _h[(i-1)/2] = _h[i];
                        _h[i] = t;
                        i = (i-1)/2;
                    }else{
                        break;
                    }
        }
    }
    int get(){
        int highest = _h[0];

        int len = _h.size();
        _h[0] = _h[len-1];
        _h.erase(_h.begin()+len-1);
        len = _h.size();
        for(int i = 0; i<len -1; ){
                   if(_h[i*2 + 1]>_h[i*2 + 2]){
                       if(_h[i]<_h[i*2 + 1]){
                           int t = _h[i*2 + 1];
                           _h[i*2 + 1] = _h[i];
                           _h[i] = t;
                           i = i*2 + 1;
                       }else{
                           break;
                       }
                   }else{
                       if(_h[i]<_h[i*2 + 2]){
                           int t = _h[i*2 + 2];
                           _h[i*2 + 2] = _h[i];
                           _h[i] = t;
                           i = i*2 + 2;
                       }else{
                           break;
                       }
                   }
        }

        return highest;
    }

    int max(){
        return _h[0];
    }
};



int main()
{
    heap a;
    int q;
    cin >> q;
    for(int i = 0; i<q; i++){
        int t;
        cin >> t;
        a.pull(t);
    }
    cout << a.max();
    cout << endl;
    for(int i = 0; i<q; i++){
        int t = a.get();
        cout << t << " ";
    }


    return 0;
}
