class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        unordered_map<char,int> m_map = {{'M',1000},{'D',500},{'C',100},{'L',50},{'X',10},{'V',5},{'I',1}};
        if (s.size()==1)
            return m_map[s[0]];
        for (int i=0;i<s.size()-1;i++){
            if (m_map[s[i]]<m_map[s[i+1]])
                result-=m_map[s[i]];
            else
                result+=m_map[s[i]];
        }
        return result+m_map[s[s.size()-1]];
    }
};