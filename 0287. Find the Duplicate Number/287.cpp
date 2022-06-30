class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        int repeat;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]]++;
        }
        for(auto x: mp){
            if(x.second >= 2){
                repeat = x.first;
            }
        } 
        return repeat;
    }        
};