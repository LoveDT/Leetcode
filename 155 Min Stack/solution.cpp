class MinStack {
public:
    stack<int> result;
    stack<int> minstack;
    void push(int x) {
        result.push(x);
        if (minstack.empty()||x<=minstack.top())
            minstack.push(x);
        
    }

    void pop() {
        if (result.empty())
            return;
        if (minstack.top()==result.top())
            minstack.pop();
        result.pop();
        
    }

    int top() {
        return result.top();
    }

    int getMin() {
        return minstack.top();
    }
};