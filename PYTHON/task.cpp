
 
using namespace std;
 
int main()
{
    int n(0),count(0),temp;
    
    cin >> n;
    for(int i = 0;i<n;++i){
        cin >> temp;
        if(temp)++count;
    }
    cout << min(count,n-count);
    cout << endl;
    return 0;    
}

int main(5)