public class program {
  public static int div(int n) {
    for (int i = 2; i <= n; i++) {
      if (n % i == 0) {
        int ans = n / i;
        return ans;
      }
    }
    return 1;
  }

  public static void main(String[] args) {
    for (int i = 0; i < args.length; i++) {
      try {
        int n = Integer.parseInt(args[i]);
        System.out.println(args[i] + " - " + div(n));
      } catch (NumberFormatException ex) {
        System.out.println(args[i] + " nie jest liczba calkowita");
      }
    }
  }
}
