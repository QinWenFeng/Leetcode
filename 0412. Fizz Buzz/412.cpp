class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        while(n != 0){
            if(n % 3 == 0 && n % 5 == 0){
                answer.push_back("FizzBuzz");
                n--;
            }
            else if(n % 3 == 0){
                answer.push_back("Fizz");
                n--;
            }
            else if(n % 5 == 0){
                answer.push_back("Buzz");
                n--;
            }
            else{
                answer.push_back(to_string(n));
                n--;
            }
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};