import java.io.File;
import java.io.FileNotFoundException;
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


    private static int findFirstUniqueQuad(String fileString) {

        LinkedList<Character> chars = new LinkedList<>();

        int i;
        for (i = 0; i < 4; i++) {
            chars.add(fileString.charAt(i));
        }

        while (!allUnique(chars)) {
            chars.removeFirst();
            i++;
            chars.add(fileString.charAt(i));
        }

        return i+1;
    }

    public static void main(String[] args) {
        // given a string
        // find the first group of 4 unique characters
        // return the index of the 4th (1-indexed)

        String filename = "commSample1.txt";

        String fileString = readFile(filename);

        int firstUniqueQuad = findFirstUniqueQuad(fileString);

        System.out.println(firstUniqueQuad);
    }
}