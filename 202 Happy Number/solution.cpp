class Solution {
public:
    bool isHappy(int n) {
       set<int> resultset;
       while (n!=1&&resultset.find(n)==resultset.end()){
           resultset.insert(n);
           int result = 0;
           while (n!=0){
               int digit = n%10;
               result+=digit*digit;
               n = n/10;
           }
           n = result;
       }
       return n==1;
    }
};