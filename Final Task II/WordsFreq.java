import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class WordsFreq {  
    public static void main(String[] args) throws IOException {

        File file = new File("/home/gaia/input.txt");
        Scanner scanner = new Scanner(file);
        int maxWordLen = 0;
        String maxWord = null;
        

        HashMap<String, Integer> map = new HashMap<>();
        while(scanner.hasNext()) {
            String word = scanner.next();
            if(map.containsKey(word)) {         
                int count = map.get(word)+1;
                map.put(word,count);
            }
            else {
               
                int count = 1;
                map.put(word, count);             
                if (word.length() > maxWordLen) {
                    maxWordLen = word.length();
                    maxWord = word;
                }
                
            }
            int count1 = 0;
            FileInputStream fis = new FileInputStream(file);
            byte[] bytesArray = new byte[(int)file.length()];
            fis.read(bytesArray);
            String s = new String(bytesArray);
            String [] data = s.split(" ");
            for (int i = 0; i < data.length; i++) {
                count1 ++;
            }
 
        TreeMap<String, Integer> sorted = new TreeMap<>();
        sorted.putAll(map);
        for (Map.Entry<String, Integer> entry: sorted.entrySet()) {
            System.out.println(entry);
        }
        System.out.printf("\n File contains " + count1 + " words." );
        System.out.println("\n The longest word is " +  maxWord + " & has " + maxWordLen + " characters");           
      
   }
   } 
}





