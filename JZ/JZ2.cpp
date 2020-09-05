class JZ4 {
public:
	void replaceSpace(char* str, int length) {
		if (nullptr == str)
			return;

		if (length <= 0)
			return;

		int count = 0;
		for (size_t i = 0; i < length; i++) {
			if (str[i] == ' ')
				count++;
		}

		char* ptr1 = str + length;
		char* ptr2 = str + length + count * 2;
		while (ptr1 != ptr2) {
			if (*ptr1 == ' ') {
				ptr1--;
				*ptr2 = '0';
				ptr2--;
				*ptr2 = '2';
				ptr2--;
				*ptr2 = '%';
				ptr2--;

			}
			else {
				*ptr2 = *ptr1;
				ptr1--;
				ptr2--;
			}
		}

	}

};

//int main() {
//	JZ2 s;
//
//	char str1[14] = "Hello World";
//	char str2[17] = "We Ara Happy";
//	char str3[12] = "We   ";
//
//	s.replaceSpace(str1, strlen(str1));
//	std::cout << str1 << std::endl;
//
//	s.replaceSpace(str2, strlen(str2));
//	std::cout << str2 << std::endl;
//
//	s.replaceSpace(str3, strlen(str3));
//	std::cout << str3 << std::endl;
//
//	s.replaceSpace(nullptr, 100);
//
//	s.replaceSpace(str1, 0);
//
//
//	return 0;
//}