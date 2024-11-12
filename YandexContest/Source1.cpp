#include <iostream>
#include <stdlib.h>

void countingSort(int** arr, int rows) {
	//int maxRange = _msize(arr)/sizeof(arr[0]);
	int maxRange = rows;
	int* count = new int[maxRange + 1];
	int count_index = 0;

	//count[maxRange] = { 0 };
	*count = { count_index };

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < rows; j++) {
			count[arr[i][j]]++;
		}
	}

	int index = 0;
	for (int i = 0; i <= maxRange; i++) {
		while (count[i] > 0) {
			for (int j = 0; j < rows; j++) {
				arr[index / rows][index % rows] = i;
				index++;
				count[i]--;
			}
		}
	}
	delete[](count);	// clean up
}

int main()
{
	std::cout << "cpp" << std::endl;
	int n;

	std::cin >> n;

	int* arr = new int[n];

	for (int i = 0; i < n; i++)
	{
		std::cin >> arr[i];
	}

	countingSort(&arr, n);

	for (int i = 0; i < n; i++)
		std::cout << arr[i];

	return 0;
}
