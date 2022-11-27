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
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            if(i>0){
                v.push_back(x + v.back());
            }
            else{
                 v.push_back(x);
            }
        }
        // cout<<"query: "<<i<<endl;
        for (auto &a:v){
            cout<<a<<" ";
        }
        cout<<endl;
        i++;
       
    }
    
    return 0;

}
