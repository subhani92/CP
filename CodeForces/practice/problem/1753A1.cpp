#include<bits/stdc++.h>
using namespace std;
#define ld long double
#define ull unsigned long long
#define ll long long
#define mod 1000000007
//#define f(i,n) for( ll (i)= 0;(i)<(n);(i)++)
#define faster ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define lp pair<ll,ll>
#define mp make_pair
#define mt make_tuple
//#define M_H priority_queue<lp ,vector<lp >,greater<lp > >
#define rep(i,j,n) for( ll (i)= j;(i)<(n);(i)++)

void solve(vector<ll> &v){
    
    
}


int main()
{     
    ios_base::sync_with_stdio(false);cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    // freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
    #endif
    
    ll t;
    cin>>t;
    int i=1;
    while(t--){
        
        ll n;
        cin>>n;
        
        vector<ll> v(n);
        // vector<ll> prefix(n);
        v.clear();
        ll sum = 0;
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            sum += x;
            v.push_back(x);
        }
        // cout<<"query: "<<i<<endl;
        vector<ll> ans;
        if(sum&1){
            cout<<-1<<endl;
        }
        else{

            for(ll i =0;i<n;i+=2){   
            
                if(n%2==0 && v[i]==v[i+1]){
                    ans.push_back(i);
                    ans.push_back(i+1);
                }
                else{
                    ans.push_back(i);
                    ans.push_back(i);
                    ans.push_back(i+1);
                    ans.push_back(i+1);
                }
            }
            
            cout<<ans.size()/2<<endl;
            for(ll i =1;i<ans.size();i+=2){
                cout<<ans[i-1]+1<<' '<<ans[i]+1<<endl;
            }
        }
       
        
       
    }
    
    return 0;

}
