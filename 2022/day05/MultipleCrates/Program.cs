using System;
using System.Collections.Generic;

class Program {
    private static string[] ReadCrateLines(string filename) {
        string[] lines = System.IO.File.ReadAllLines(filename);
        int delim = -1;
        for (int i = 0; i < lines.Length; i++) {
            if (lines[i] == "") {
                delim = i;
            } 
        }

        List<string> listLines = new List<string>(lines);
        return listLines.GetRange(0, delim).ToArray();
    }

    private static string[] ReadCrateInstructions(string filename) {
        string[] lines = System.IO.File.ReadAllLines(filename);
        int delim = -1;
        for (int i = 0; i < lines.Length; i++) {
            if (lines[i] == "") {
                delim = i;
            }
        }

        List<string> listLines = new List<string>(lines);
        return listLines.GetRange(delim+1, lines.Length-delim-1).ToArray();
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

    private static List<List<int>> GetInstructions(string filename) {

        string[] lines = ReadCrateInstructions(filename);
        List<List<int>> instructions = new List<List<int>>();

        foreach (string line in lines) {
            string[] split = line.Split(' ');

            List<int> instruction = new List<int>{
                Int32.Parse(split[1]), 
                Int32.Parse(split[3]), 
                Int32.Parse(split[5])
            };

            instructions.Add(instruction);
        }

        return instructions;
    }

    private static void DoInstruction(List<List<char>> crates, int amount, int from, int to) {
        from--;   // 1-indexed to 0-indexed
        to--;

        for (int i = amount; i > 0; i--) {
            crates[to].Add(crates[from][crates[from].Count - i]);
        }
        for (int _ = 0; _ < amount; _++) {
            crates[from].RemoveAt(crates[from].Count - 1);
        }
    }

    public static void Main() {
        string filename = "./cratesSample.txt";

        List<List<char>> crates = GetCrateState(filename);

        // print crates
        foreach (List<char> crateLine in crates) {
            foreach (char crate in crateLine) {
                Console.Write(crate + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine();

        List<List<int>> instructions = GetInstructions(filename);

        // print instructions
        foreach (List<int> instruction in instructions) {
            foreach (int n in instruction) {
                Console.Write(n + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine();

        foreach (List<int> ins in instructions) {
            DoInstruction(crates, ins[0], ins[1], ins[2]);
        }

        // print crates
        foreach (List<char> crateLine in crates) {
            foreach (char crate in crateLine) {
                Console.Write(crate + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine();


        // final output
        foreach (List<char> crateLine in crates) {
            Console.Write(crateLine.Last());
        }
        Console.WriteLine();
    }
}

