class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record;
        int sum = 0;
        for (const string& op : operations){
            if(op != "+" && op != "D" && op != "C"){
                record.push_back(stoi(op));
                sum += record.back();
            }else if(op == "+"){
                int n = record.size();
                record.push_back(record[n-1]+record[n-2]);
                sum += record.back();
            }else if(op == "D"){
                int n = record.size();
                record.push_back(record[n-1]*2);
                sum += record.back();
            }else{
                sum -= record.back();
                record.pop_back();
            }
        }
        return sum;
    }
};