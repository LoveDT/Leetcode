class Stack {
public:
    // Push element x onto stack.
    void push(int x) {
        m_queue.push(x);
        m_top = x;
    }

    // Removes the element on top of the stack.
    void pop() {
        int leng = m_queue.size();
        for (int i=0;i<leng-1;i++){
            int tmp = m_queue.front();
            m_helper.push(tmp);
            m_queue.pop();
        }
        m_queue.pop();
        for (int i=0;i<leng-1;i++){
            int tmp = m_helper.front();
            m_queue.push(tmp);
            m_top = tmp;
            m_helper.pop();
        }
    }

    // Get the top element.
    int top() {
        return m_top;
    }

    // Return whether the stack is empty.
    bool empty() {
        return m_queue.empty();
    }
private:
    queue<int> m_queue;
    queue<int> m_helper;
    int m_top=0;
};