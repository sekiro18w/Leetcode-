class Solution {
public:
        int longestOnes(vector<int>& A, int K) {
        vector<int> freq(2);
        int i = 0, r=0;
        for(int j = 0; j < A.size(); j++){
            freq[A[j]] ++;
            while(freq[0] > K && i <= j){
                freq[A[i]] --;
                i++;
            }
            r = max(r, j-i+1);
        }
        return r;
    }
};