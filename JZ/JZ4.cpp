#include <iostream>
#include <vector>

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class JZ4 {
public:
	TreeNode* reConstructBinaryTree(std::vector<int> pre, std::vector<int> vin) {
		return reConstructBinaryTreeImpl(0, pre.size(), pre, 0, vin.size(), vin);
	}

	TreeNode* reConstructBinaryTreeImpl(int preFrom, int preTo, std::vector<int> pre, int vinFrom, int vinTo, std::vector<int> vin) {
		if (pre.size() <= 0 || vin.size() <= 0)
			return nullptr;

		int value = pre[preFrom];
		if (preFrom == preTo) {
			TreeNode* node = new TreeNode(value);
			node->right = nullptr;
			node->right = nullptr;
			return node;
		}
		
		int index = -1;
		for (size_t i = vinFrom; i < vinTo; i++) {
			if (vin[i] == value)
				index = i;
		}
		if (-1 == index)
			return nullptr;

		int leftCount = index - vinFrom;
		int rightCount = vinTo - index - 1;
		
		TreeNode* leftNode = 0 == leftCount ? nullptr : reConstructBinaryTreeImpl(preFrom + 1, preFrom + 1 + leftCount, pre, vinFrom, index, vin);
		TreeNode* rightNode = 0 == rightCount ? nullptr : reConstructBinaryTreeImpl(preFrom + 1 + leftCount, preTo, pre, index + 1, vinTo, vin);

		TreeNode* node = new TreeNode(value);
		node->left = leftNode;
		node->right = rightNode;
		return node;
	}

};

void PrintNodePre(TreeNode* node) {
	if (nullptr == node)
		return;

	std::cout << node->val << "\t";
	PrintNodePre(node->left);
	PrintNodePre(node->right);
}

void PrintNodeVin(TreeNode* node) {
	if (nullptr == node)
		return;

	PrintNodeVin(node->left);
	std::cout << node->val << "\t";
	PrintNodeVin(node->right);
}
//
//int main() {
//
//	JZ4 s;
//
//	std::vector<int> pre = { 1,2,4,7,3,5,6,8 };
//	std::vector<int> vin = { 4,7,2,1,5,3,8,6 };
//
//	TreeNode* node = s.reConstructBinaryTree(pre, vin);
//	PrintNodePre(node);
//	std::cout << std::endl;
//	PrintNodeVin(node);
//
//	return 0;
//}