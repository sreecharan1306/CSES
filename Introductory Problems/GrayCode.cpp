#include <fstream>
#include <bits/stdc++.h>
using namespace std;

vector<string> solve(int n)
{
    if (n==1)
    {
        vector<string> ans={"0","1"};
        return ans;
    }
    vector<string>p=solve(n-1);
    vector<string>ans;
    for(string i:p){
        ans.push_back('0'+i);
    }
    reverse(p.begin(),p.end());
    for(string i:p){
        ans.push_back('1'+i);
    }
    return ans;

}
int main()
{
    // ifstream in("input.txt");
    // ofstream out("output.txt");
    // cin.rdbuf(in.rdbuf());
    // cout.rdbuf(out.rdbuf());
    int n;
    cin >> n;
    vector<string>sol=solve(n);
    for(string i:sol){
        cout<<i<<endl;
    }
}
