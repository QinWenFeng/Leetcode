class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        vector<int> sol;
        for(int i = 0; i < nums.size(); i++){
            if(mp.find(target - nums[i]) != mp.end()){
                sol.push_back(mp[target - nums[i]]);
                sol.push_back(i);
            }
            
            mp[nums[i]] = i;
        }
        return sol;
    }
};