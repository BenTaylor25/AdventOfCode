import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;

public class CommunicationDevice {

    private static String readFile(String filename) {
        String fileString = "";

        try {
            File f = new File(filename);
            Scanner s = new Scanner(f);
            if (s.hasNextLine()) {
                fileString = s.nextLine();
            }

            s.close();
        } catch (FileNotFoundException e) {
            System.out.println("couldn't find file");
        }

        return fileString;
    }

    private static boolean allUnique(LinkedList<Character> chars) {

        HashSet<Character> set = new HashSet<>(chars);
        // System.out.println(chars);
        // System.out.println(set);
        // System.out.println(set.size());
        // System.out.println();

        return set.size() == 4;
    }  

    private static int findFirstUniqueQuad(String fileString) {

        LinkedList<Character> chars = new LinkedList<>();

        int i;
        for (i = 0; i < 4; i++) {
            chars.add(fileString.charAt(i));
        }

        while (!allUnique(chars)) {
            chars.removeFirst();
            chars.add(fileString.charAt(i));
            i++;
        }

        return i;
    }

    public static void main(String[] args) {
        // given a string
        // find the first group of 4 unique characters
        // return the index of the 4th (1-indexed)

        String filename = "commSample5.txt";

        String fileString = readFile(filename);

        int firstUniqueQuad = findFirstUniqueQuad(fileString);

        System.out.println(firstUniqueQuad);
    }
}