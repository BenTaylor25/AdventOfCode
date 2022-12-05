
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

        // columns are represented with 3 characters, joined by a space
        // `123 123 123`
        // note that there is no whitespace following the last character
        //
        // let c = colCount
        // let l = lineLength
        // l = 3c + (c-1)
        // l = 4c - 1
        // c = (l + 1) / 4
        int colCount = (crateLines[0].Length + 1) / 4;

        Console.WriteLine(colCount);

        return new List<char>();
    }

    public static void Main() {
        string filename = "./cratesSample.txt";

        List<char> crates = ReadCrateState(filename);
    }
}

