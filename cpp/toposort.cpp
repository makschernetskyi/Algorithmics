#include<iostream>
#include<vector>
using namespace std;


bool visited[int(10e5)];

void dfs(int at, vector<int> visitedByDFS, bool visited[], int V,vector<int> Graph[]){

    visitedByDFS.push_back(at);
    visited[at] = 1;

    for(int next : Graph[at]){
        if(!visited[next]){
            dfs(next, visitedByDFS, visited, V, Graph);
        }
    }

}



int main(){


    int V, E;
    cin >> V >> E;
    vector<int> Graph[V];


    while(E){

        int a, b;
        cin >> a,b;
        a--;
        b--;
        Graph[a].push_back(b);



        E--;
    }


    // fill(visited, visited+V, 0);

    int order[V];
    int pos = V-1;

    for(int i = 0; i < V; i++){
        if(!visited[i]){
            vector<int> visitedByDFS;
            dfs(i, visitedByDFS, visited, V, Graph);
            for(int j = 0, len = visitedByDFS.size(); j<len; j++){
                order[pos] = visitedByDFS[j];
                pos--;
            }
        }
    }


    for(int node : order){
        cout << node << " ";
    }





}

