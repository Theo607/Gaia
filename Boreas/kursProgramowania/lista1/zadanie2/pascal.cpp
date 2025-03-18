#include <iostream>
#include <stdexcept>
#include <string>

class PascalRow {
public:
  int row[100];
  PascalRow(int rowNumber) {
    for (int i = 0; i <= rowNumber; i++) {
      row[i] = 0;
    }

    row[0] = 1;
    while (row[rowNumber - 1] == 0) {
      for (int arrayIndex = rowNumber - 1; arrayIndex > 0; arrayIndex--) {
        row[arrayIndex] += row[arrayIndex - 1];
      }
    }
  }

  int rowElement(int elemNumber) { return row[elemNumber]; }
};

int main(int argc, char *argv[]) {
  if (argc < 2) {
    std::cout << "Brak argumentow" << std::endl;
    return 1;
  }

  try {
    int triangleSize = std::stoi(argv[1]);
    if (triangleSize < 0) {
      std::cout << argv[1] << " niepoprawne dane" << std::endl;
      return 1;
    }

    PascalRow triangle(triangleSize);

    for (int inputIndex = 2; inputIndex < argc; inputIndex++) {
      try {
        int input = std::stoi(argv[inputIndex]);
        if (input < 0 || input > triangleSize) {
          std::cout << argv[inputIndex] << " liczba wykracza zakres"
                    << std::endl;
        } else {
          std::cout << argv[inputIndex] << " - " << triangle.rowElement(input)
                    << std::endl;
        }
      } catch (const std::invalid_argument &) {
        std::cout << argv[inputIndex] << " nieprawidlowe" << std::endl;
      } catch (const std::out_of_range &) {
        std::cout << argv[inputIndex] << " nieprawidlowe" << std::endl;
      }
    }
  } catch (const std::invalid_argument &) {
    std::cout << argv[1] << " blad" << std::endl;
  } catch (const std::out_of_range &) {
    std::cout << argv[1] << " blad" << std::endl;
  }

  return 0;
}
