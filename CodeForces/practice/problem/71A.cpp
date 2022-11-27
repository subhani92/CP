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

void solve(int arr[],int n){
    int prev = arr[0];
    bool flag = 0;
    for(int i =1;i<n;i++){
        if(arr[i]-prev <0){
            cout<<"NO"<<endl;
            flag =1;
            break;
        }
        prev = arr[i];
    }

    if(flag==0)
    cout<<"YES"<<endl;

}


int main()
{     
    ios_base::sync_with_stdio(false);cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    // freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
    #endif
    
    int n;
    cin>>n;
    while(n--){
        string s;
        cin>>s;

        int len = s.size();
        if(len<= 10){
            cout<<s<<endl;

        }
        else{
            cout<<s[0]<<len-2<<s[len-1]<<"\n";
        }

    }
    


}
