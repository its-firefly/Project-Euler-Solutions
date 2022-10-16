#include <iostream>

int main (){

    int sum = 0, sqSum = 0, max = 100;

    for (int i = 1; i <= max; i++){
        sum += i;
        sqSum += i*i;
    }

    std::cout << (sum*sum) - sqSum << std::endl;

    return 0;
}