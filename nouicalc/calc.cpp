#include <iostream>
#include <cmath>
#include <string>
using namespace std;
float a,b,c;

void input(){
	cout << "A: ";
	cin >> a;
	cout << "B: ";
	cin >> b;
}

int main()
{
	int sel;
	cout << "Simple calculator" << endl;
	cout << endl << "1.Plus (+)" << endl << "2.Minus (-)" << endl << "3.Multiply (*)" << endl << "4.Divide (/)" << endl ;
	cout << "5.Power (^)" << endl << "6.Square root" << endl << "7.Sin, Cos & Tan" << endl << endl;
	cout << "Select opt (1-7): ";
	cin >> sel;
	switch (sel){
		case 1:cout << "Enter 2 numbers below (a+b)" << endl;
			   input();
			   cout << a << "+" << b << endl << "Answer: " << a+b;
			   break;
		case 2:cout << "Enter 2 numbers below (a-b): " << endl;
			   input();
			   cout << a << "-" << b << endl << "Answer: " << a-b;
			   break;
		case 3:cout << "Enter 2 numbers below (a*b): " << endl;
			   input();
			   cout << a << "*" << b << endl << "Answer: " << a*b;
			   break;	
		case 4:cout << "Enter 2 numbers below (a/b): " << endl;
			   input();
			   cout << a << "/" << b << endl << "Answer: " << a/b;
			   break;		
		case 5:cout << "Enter 2 numbers below (a^b): " << endl;
			   input();
			   cout << a << "^" << b << endl << "Answer: " << pow(a,b);
			   break;	
		case 6:cout << "Enter number here: ";
			   cin >> a;
			   cout << "Square root of " << a << endl << "Answer: " << sqrt(a);
			   break;
		case 7:cout << "Enter degrees here (0-360): ";
			   cin >> a;
			   b = a*3.14159265/180;
			   cout << "Sin " << a << ": " << sin(b) << endl;
			   cout << "Cos " << a << ": " << cos(b) << endl;
			   cout << "Tan " << a << ": " << tan(b) << endl;
			   break;
		default:cout << "Wrong input or out of limit";
	}
}
