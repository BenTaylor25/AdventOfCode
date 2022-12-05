
class Program {
    private static List<char> ReadCrateState(string filename) {

        string[] lines = System.IO.File.ReadAllLines(filename);
        int delim = -1;
        for (int i = 0; i < lines.Length; i++) {
            if (lines[i] == "") {
                delim = i;
            } 
        }

        for (int i = 0; i < delim; i++) {
            Console.WriteLine(lines[i]);
        }

        return new List<char>();
    }

    public static void Main() {
        string filename = "./cratesSample.txt";

        List<char> crates = ReadCrateState(filename);
    }
}

