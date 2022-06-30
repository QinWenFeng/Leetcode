class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> mp;
        int single;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]]++;
        }
        for(auto x: mp){
            if(x.second == 1){
                single = x.first;
            }
        } 
        return single;
    }
};