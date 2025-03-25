#include <iostream>

extern "C" {
    const int r = 8, c = 8;
    double arr[r][c] = {0};

    double (*getarr())[c] {
        return arr;
    }
}

int main() {
    // Modify some values
    arr[1][2] = 1;
    arr[1][3] = 1;
    arr[2][2] = 1;
    arr[2][3] = 1;
    arr[3][2] = 1;
    arr[3][3] = 1;

    // Get array pointer
    double (*matrix)[c] = getarr();

    // Print array
    std::cout << "C++ Matrix Output:\n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
