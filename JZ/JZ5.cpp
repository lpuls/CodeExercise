#include <stack>
#include <iostream>

class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        int temp = -1;
        while (!stack1.empty()) {
            temp = stack1.top();
            stack1.pop();
            stack2.push(temp);
        }

        if (!stack2.empty()) {
            stack2.pop();
        }

        while (!stack2.empty()) {
            int temp2 = stack2.top();
            stack2.pop();
            stack1.push(temp2);
        }

        return temp;
    }

private:
    std::stack<int> stack1;
    std::stack<int> stack2;
};

//int main() {
//    Solution s;
//
//    s.push(1);
//    s.push(2);
//    s.push(3);
//
//    std::cout << s.pop() << std::endl;
//    std::cout << s.pop() << std::endl;
//    std::cout << s.pop() << std::endl;
//    std::cout << s.pop() << std::endl;
//
//    return 1;
//}