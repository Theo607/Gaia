#ifndef PASCAL_H
#define PASCAL_H

class PascalRow {
public:
  int row[100];
  PascalRow(int rowNumber);
  int rowElement(int elemNumber);
  ~PascalRow();
};

#endif
