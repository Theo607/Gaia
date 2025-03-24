#include "pascal.hpp"
#include <iostream>
#include <stdexcept>
#include <string>

PascalRow::PascalRow(int rowNumber) {
  for (int i = 0; i <= rowNumber; i++) {
    row[i] = 0;
  }

  row[0] = 1;
  while (row[rowNumber] == 0) {
    for (int arrayIndex = rowNumber; arrayIndex > 0; arrayIndex--) {
      row[arrayIndex] += row[arrayIndex - 1];
    }
  }
}

int PascalRow::rowElement(int elemNumber) { return row[elemNumber]; }
PascalRow::~PascalRow() { delete[] row; }
