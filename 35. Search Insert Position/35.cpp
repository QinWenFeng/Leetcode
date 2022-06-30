class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size();
        int pos;
        while(high - low > 1){
            int mid = (high + low)/2;
            if(nums[mid] < target){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        if(nums[low] <= target){
            pos = low;
        }
        if(nums[high-1] <= target){
            pos = high;
        }
        if(nums[0] == target){
            pos = 0;
        }
        if(nums[high-1] == target){
            pos = high-1;
        }
        return pos;
    }
};