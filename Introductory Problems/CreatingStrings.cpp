#include <bits/stdc++.h>
#include <fstream>
using namespace std;

void solve(int ind,int n,string s,set<string>&strs){
    if(ind==n){
        strs.insert(s);
        return;
    }

}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    string s;
    cin >> s;
    set<string>strs;
    int n=s.size();
    solve(0,n,s,strs);

    vector<string>ans(strs.begin(),strs.end());
    sort(ans.begin(),ans.end());.git
    cout<<ans.size()<<endl;
    for(string i:ans) cout<<i<<endl;
    return 0;
}
