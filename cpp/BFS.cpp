#include <iostream>
#include <vector>
#include <climits>
using namespace std;



int main()
{

    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int verteces, edges;
    cin >> verteces >> edges;

    vector<int> Graph[verteces];

    bool fixed[verteces] = {0};
    int distances[verteces] = {INT_MAX};
    distances[0] = 0;
    visited[0] = true;
    vector<int> toVisit;


    while(edges){

        int a,b;
        cin >> a >> b;
        a--;
        b--;
        Graph[a].push_back(b);
        Graph[b].push_back(a);


        edges--;
    }

    int pivot = 0;
    while(!toVisit.empty()){
        for(int i = 0, len = Graph[pivot].size(); i<len; i++ ){
            if(distances[Graph[pivot][i]]>distances[pivot]+1){
                distances[Graph[pivot][i]] = distances[pivot]+1;
            }
        }
    }






    return 0;
}

