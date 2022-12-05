
class Program {
    private static string[] ReadCrateLines(string filename) {
        string[] lines = System.IO.File.ReadAllLines(filename);
        int delim = -1;
        for (int i = 0; i < lines.Length; i++) {
            if (lines[i] == "") {
                delim = i;
            } 
        }

        return lines.Where((n, i) => i < delim).ToArray();
    }

    private static List<char> ReadCrateState(string filename) {

        string[] crateLines = ReadCrateLines(filename);
        int colCount = (crateLines[0].Length + 1) / 4;

        Console.WriteLine(colCount);

        return new List<char>();
    }

    public static void Main() {
        string filename = "./cratesSample.txt";

        List<char> crates = ReadCrateState(filename);
    }
}

