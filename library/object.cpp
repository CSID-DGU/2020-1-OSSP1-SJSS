#include <windows.h>
#include <string>
#include "objectDetection.h"
#include <fstream>
#include <iostream>
using namespace std;


void objectDetection(){
	system("start.bat");
}

string object(){
	ifstream readFile;
	readFile.open("output.txt");
	char arr[100];
	while (!readFile.eof()) {
		readFile.getline(arr, 100);
	}
	readFile.close();

	return arr;
}

//int main() {
//	objectDetection();
//	cout<<object();
//}
