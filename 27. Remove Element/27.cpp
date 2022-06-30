class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        for (int i = length - 1; i >= 0; i--) {
            if (nums[i] == val) {
                for (int j = i + 1; j < length; j++) {
                    nums[j - 1] = nums[j];
                }
                length--;
            }
        }
        return length;        
    }        
};