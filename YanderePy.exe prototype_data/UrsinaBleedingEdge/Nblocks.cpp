#include<iostream>

using namespace std;

int main() {
	std::cout<< "Nblock has the i value" <<std::endl; 
	
	int Nblock = 10;
	float i = 15;
	
	if (i < 20) {
		std::cout<<"Moved"<<std::endl;
	}else{
		std::cout<<"unmoved"<<std::endl;
	}
	if (Nblock < 20) {
		std::cout<<"Moved"<<std::endl;
	}else{
		std::cout<<"unmoved"<<std::endl;
	}
	return 0;
}

