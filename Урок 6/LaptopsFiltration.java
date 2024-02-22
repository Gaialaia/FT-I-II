import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Stream;

    class LaptopsFiltration {

    public static void main(String[] args)  {
        HashMap<Integer, String> criteriaLaptop = new HashMap<>();
        boolean loopAgain = true;
        Scanner scan = new Scanner(System.in);
        System.out.println("Chose criteria for filtration:");
        System.out.println("1 - CPU");
        System.out.println("2 - RAM");
        System.out.println("3 - OS");
        System.out.println("4 - color");

        do {
            System.out.print("Enter criteria number :");
            Integer criteriaNumber = Integer.parseInt(scan.nextLine());

            System.out.print("Enter criteria :");
            String criteria = scan.nextLine();

            String preVal = criteriaLaptop.put(criteriaNumber, criteria);

            if (preVal!=null) {
                System.out.println("Criteria number:" + criteriaNumber + " is "
                        + preVal + " and has been overwritten by " + criteria);
            }
            System.out.print("Do you want to enter another criteria, press y or n ?");
            String answer = scan.nextLine();


            if (answer.equals("y") || answer.equals("Y")) {
                continue;
            } else {
                break;
            }

        } while (loopAgain);
        scan.close();

        System.out.println("Laptops you search :");
        System.out.println("   Criteria number  "+ "      criteria");
        for(int cn:criteriaLaptop.keySet()){
            System.out.println("   "+cn+"     "+criteriaLaptop.get(cn));
        }

        System.out.println(criteriaLaptop);
    

        Set<String> criteriaFilter = new HashSet<> (criteriaLaptop.values());
        

        Stream<String> stream4 = criteriaFilter.stream();
        System.out.println(criteriaFilter);

        //   stream4.filter(el -> el == "intel");
        // //          .forEach(System.out::println);


    }

}




    

