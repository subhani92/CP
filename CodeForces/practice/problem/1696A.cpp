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


int main()
{     
    ios_base::sync_with_stdio(false);cin.tie(NULL);

    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // // freopen("error.txt", "w", stderr);
    // freopen("output.txt", "w", stdout);
    // #endif
    
    int t;
    cin>>t;
    while(t--){
       
        ll n, z;
        cin>>n>>z;
        vector<ll >  a(n);
        for(ll i =0;i<n;i++){
            cin>>a[i];
        }

        ll ans = INT_MIN;
        for(ll i =0;i<n;i++){
            a[i] |= z;
            z  &=z ;
            ans = max(ans, a[i]);
        }
        cout<<ans<<endl;

    }
    


}
