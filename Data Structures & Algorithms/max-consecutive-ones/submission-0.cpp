class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        int cumul = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 1){
                cumul++;
            }else{
                cumul = 0;
            }
            if(max < cumul){
                max = cumul;
            }
        }
        return max;
        
    }
};