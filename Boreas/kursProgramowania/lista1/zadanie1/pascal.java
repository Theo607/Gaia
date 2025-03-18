class pascalRow {
  public int[] row;

  public pascalRow(int rowNumber) {
    row = new int[rowNumber + 1];
    row[0] = 1;
    while (row[rowNumber - 1] == 0) {
      for (int arrayIndex = rowNumber - 1; arrayIndex > 0; arrayIndex--) {
        row[arrayIndex] = row[arrayIndex] + row[arrayIndex - 1];
      }
    }
  }

  public int rowElement(int elemNumber) {
    return row[elemNumber];
  }
}

public class pascal {
  public static void main(String[] Args) {
    try {
      int triangleSize = Integer.parseInt(Args[0]);
      if (triangleSize < 0) {
        System.out.println(Args[0] + "niepoprawne dane");
      } else {
        pascalRow triangle = new pascalRow(triangleSize);
        for (int inputIndex = 1; inputIndex < Args.length; inputIndex++) {
          try {
            int input = Integer.parseInt(Args[inputIndex]);
            if (input < 0 || input > triangleSize) {
              System.out.println(Args[inputIndex] + " liczba wykracza zakres");
            } else {
              System.out.println(Args[inputIndex] + " -  " + triangle.rowElement(input));
            }
          } catch (NumberFormatException exception) {
            System.out.println(Args[inputIndex] + " nieprawidlowe");
          }
        }
      }
    } catch (NumberFormatException exception) {
      System.out.println(Args[0] + "blad");
    }
  }
}
