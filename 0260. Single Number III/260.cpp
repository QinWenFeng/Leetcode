class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        unordered_map<int, int> mp;
        vector<int> arr;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]]++;
        }
        int i = 0;
        for(auto x: mp){
            if(x.second == 1){
                arr.push_back(x.first);
            }
        } 
        return arr;
    }  
};