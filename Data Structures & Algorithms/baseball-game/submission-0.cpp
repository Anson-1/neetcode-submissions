class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record;
        for (int i=0; i<operations.size(); i++){
            if(operations[i] != "+" && operations[i] != "D" && operations[i] != "C"){
                record.push_back(stoi(operations[i]));
            }else if(operations[i] == "+"){
                int n = record.size();
                record.push_back(record[n-1]+record[n-2]);
            }else if(operations[i] == "D"){
                int n = record.size();
                record.push_back(record[n-1]*2);
            }else{
                record.pop_back();
            }
        }
        int sum = 0;
        for(int j=0; j<record.size(); j++){
            sum += record[j];
        }
        return sum;
    }
};