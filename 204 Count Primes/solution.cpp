class Solution {
public:
    int countPrimes(int n) {
        bool isprime[n];
        for (int i=0;i<n;i++){
            isprime[i] = true;
        }
        isprime[0] = isprime[1] = false;
        int start = 2;
        int count = 0;
        while (start*start<n){
            if (isprime[start]){
                int mark = start*start;
                while (mark<n){
                    isprime[mark] = false;
                    mark+=start;
                }
            }
            start+=1;
        }
        for (int i=0;i<n;i++){
            if (isprime[i])
                count++;
        }
        return count;
    }
};