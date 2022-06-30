class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        for (int i = length - 2; i >= 0; i--) {
            if (nums[i] == nums[i + 1]) {
                for (int j = i + 1; j < length; j++) {
                    nums[j - 1] = nums[j];
                }
                length--;
            }
        }
        return length;        
    }
};