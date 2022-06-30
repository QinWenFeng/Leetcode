class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int closest_sum = 30000;
        for(int i = 0; i < nums.size() -2; i++){
            int ptr1 = i + 1;
            int ptr2 = nums.size() - 1;
            while(ptr1 < ptr2){
                int sum = nums[i] + nums[ptr1] + nums[ptr2];
                if(sum == target) return sum;
                if(abs(target-sum) < abs(target-closest_sum)){
                    closest_sum = sum;
                }
                if(sum > target){
                    ptr2--;
                }
                else{
                    ptr1++;
                }
            }
        }
        return closest_sum;
    }
};