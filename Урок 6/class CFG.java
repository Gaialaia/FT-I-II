
import java.util.*;

class GFG {
     
    // Driver code
    public static void main(String[] args) {
     
    // Creating an Integer HashSet
    Set<Integer> set = new HashSet<>();
     
    // adding elements in set
    set.add(2);
    set.add(4);
    set.add(6);
    set.add(8);
    set.add(10);
    set.add(12);
     
    // converting Set to Stream
    Set<Integer> stream = set.stream();
     
    // displaying elements of Stream using lambda expression
    stream.forEach(elem->System.out.print(elem+" "));
     
    }
}