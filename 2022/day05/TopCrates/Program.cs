
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

    private static List<List<char>> GetCrateState(string filename) {

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
        int rowCount = crateLines.Length;

        List<List<char>> cratesAsList = new List<List<char>>();

        for (int c = 0; c < colCount; c++) {
            int cInd = c*4 + 1;

            List<char> crateStack = new List<char>();
            for (int r = rowCount-2; r >= 0; r--) {
                if (crateLines[r][cInd] != ' ') {
                    crateStack.Add(crateLines[r][cInd]);
                }
            }

            cratesAsList.Add(crateStack);
        }

        return cratesAsList;
    }

    public static void Main() {
        string filename = "./cratesSample.txt";

        List<List<char>> crates = GetCrateState(filename);

        foreach (List<char> crateLine in crates) {
            foreach (char crate in crateLine) {
                Console.Write(crate + " ");
            }
            Console.WriteLine();
        }
    }
}

