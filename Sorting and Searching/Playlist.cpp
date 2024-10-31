#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int>arr(n);
    for(int i=0;i<n;i++) cin>>arr[i];
    unordered_map<int,int>mp;
    int ans=0,i=0,j=0;
    while(j<n){
        if(mp.find(arr[j])!=mp.end()){
            ans=max(ans,j-i+1);
            i=max(i,mp[arr[j]]+1);
        }
        mp[arr[j]]=j;
        ans=max(ans,j-i+1);
        j++;
    }
    cout<<ans<<endl;
}