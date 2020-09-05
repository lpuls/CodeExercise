#include <iostream>
#include <vector>

struct ListNode {
	int val;
	struct ListNode* next;
	ListNode(int x) :
		val(x), next(NULL) {
	}
};

class JZ3 {
public:
	std::vector<int> printListFromTailToHead(ListNode* head) {
		std::vector<int> result;

		ListNode* node = head;
		while (nullptr != node) {
			result.insert(result.begin(), node->val);
			node = node->next;
		}

		return result;
	}
};

//void PrintList(std::vector<int> v) {
//	for (size_t i = 0; i < v.size(); i++) {
//		std::cout << v[i] << "\t";
//	}
//	std::cout << std::endl;
//}
//
//int main() {
//
//	JZ3 s;
//
//	PrintList(s.printListFromTailToHead(nullptr));
//
//	ListNode* node1 = new ListNode(1);
//	ListNode* node2 = new ListNode(2);
//	ListNode* node3 = new ListNode(3);
//	ListNode* node4 = new ListNode(4);
//	node1->next = node2;
//	node2->next = node3;
//	node3->next = node4;
//	node4->next = nullptr;
//	PrintList(s.printListFromTailToHead(node1));
//
//
//	return 0;
//}