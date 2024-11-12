// YandexContest.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int fib(int n);

int fib2(int n, int a, int b)
{
	if (n == 0) return a;
	if (n == 1) return b;
	if (n == 2) return a ^ b;
	return fib2(n % 3, a, b);
}


int remainder(int n, int m)
{
	return n % m;
}

/*/
int main()
{
	std::cout << "cpp" << std::endl;
	int n, m;
	std::cout << "enter n and m: " << std::endl;
	std::cin >> n >> m;

	int m_n = fib(n);
	//m = fib(m);

	std::cout << "fib(" << n << ")=" << fib(n) << "\tfib(" << m << ")=" << fib(m) << std::endl;
	std::cout << "F(n) mod m=" << fib2(m_n, 0, 1) << std::endl;

	return 0;
}
*/
int fib(int n)
{
	int f0 = 0, f1 = 1;

	for (int i = 0; i < n; i++)
	{
		int temp = f0;
		f0 = f1;
		f1 = temp + f1;
	}
	return f0;
}
