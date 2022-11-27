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

int gcd(int a, int b)
{
  if (a == 0)
    return b;
  return gcd(b % a, a);
}

int findGCD(int arr[], int n)
{
  int result = arr[0];
  for (int i = 1; i < n; i++)
  {
    result = gcd(arr[i], result);
 
    if(result == 1)
    {
    return 1;
    }
  }
  return result;
}


int main()
{     
    ios_base::sync_with_stdio(false);cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    // freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
    #endif
    
    int n ;
    cin>>n;
    int a[n];
    int sum = INT_MAX;
    for(int i =0;i<n;i++){
        int x;
        cin>>x;
        a[i] = x;
        if (x<sum && x != 1)
        sum =  x;
        // sum +=x;
    }
    set<int> s;

    for(int i =0;i<n;i++){
        a[i] = a[i]%sum;
        s.insert(a[i]);
    }

     cout<<s.size()<<endl;
    // cout<<findGCD(a, n)<<endl;


}
