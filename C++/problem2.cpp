#include <iostream>

int main(){

    int max = 4000000, a = 1, b = 2, c = 0, sum = 0;

    while (b<max){
        c = a + b;
        if (b%2 ==0){
            sum+=b;
        }
        a = b;
        b = c;
    }
    
    std::cout << sum <<std::endl;

    return 0;
}