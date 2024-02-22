import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

  public static void main(String[] args) {


    Laptops Laptop1 = new Laptops("Asus", "Vivobook 17", "white", "Intel Core3", "Ubuntu", 6);
    Laptops Laptop2 = new Laptops("Dell", "Inspiron", "navy", "Opteron", "Windows", 8);
    Laptops Laptop3 = new Laptops("Acer", "Aspire", "grey", "Intel Core i5", "Linux", 16);
    Laptops Laptop4 = new Laptops("Huawei", "Matebook", "space grey", "Intel Core i5", "Windows 11", 8);
    Laptops Laptop5 = new Laptops("Thunderobot 911", "911 MG 3", "grey", "Intel Core i7", "Windows 11",16);
    Laptops Laptop6 = new Laptops(" Apple", "MacBook Air", "silver", "Apple M", "MacOS", 8);

    Set<Laptops> LaptopSet = new HashSet<Laptops>();

    LaptopSet.add(Laptop3);
    LaptopSet.add(Laptop2);

    System.out.println(LaptopSet);


    // Set<String> LaptopSetName = new HashSet<>();

    // LaptopSetName.add(Laptop1.name);
    //  LaptopSetName.add(Laptop2.name);
    //   LaptopSetName.add(Laptop3.name);

    //  System.out.println(LaptopSetName);

    // Stream<String> stream1 = LaptopSetName.stream();

    // stream1.filter(el -> el == "Asus") 
    //         .forEach(System.out::println); 


    // Set<Integer> LaptopsRam = new HashSet<Integer>();
      
    //  LaptopsRam.add(Laptop2.getRam());
    //  LaptopsRam.add(Laptop1.getRam());
    //  LaptopsRam.add(Laptop3.getRam());
    //  LaptopsRam.add(Laptop4.getRam());

    //   System.out.println(LaptopsRam);

    //       Stream<Integer> stream2 = LaptopsRam.stream();

    // stream2.filter(el -> el == 16) 
    //         .forEach(System.out::println); 


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
          
            Collection<String> collectionValues = criteriaLaptop.values();
		        for(String s: collectionValues){
			        System.out.println(s);
		            }

    
            // Set<String> criteriaFilter = new HashSet<> (criteriaLaptop.values());
            
    
            // Stream<String> stream4 = criteriaFilter.stream();
            // System.out.println(criteriaFilter);
           


            //         Set<Laptops> filteredSet = LaptopSet.stream()
            //         .filter(el -> el == criteriaFilter.get(criteriaFilter.values()) = LaptopSet.get(LaptopSet.values()))
            //                         .collect(Collectors.toSet());

            //                         System.out.println(filteredSet);
  
  
  }



}

    

    


    




     

  

    

      
      

    // Stream<Laptops> LaptopsStream = Stream.of(new Laptops("Acer", "Aspire", "pink", "Intel", "Windows", 8), 
    // new Laptops("Choser", "Aspirin", "pink", "Intel", "Windows", 8),
    // new Laptops("Huawei", "Pirat", "white", "Intel", "Ubuntu", 16));

    // LaptopsStream.map(p-> "название: " + p.getName() + " цена: " + p.getOS())
    // .forEach(s->System.out.println(s));

    // Stream <String> stream = LaptopsSet.stream();
    // LaptopsSet.forEach(elem -> System.out.print(elem+" "));

  







  














	
// Stream<Phone> phoneStream = Stream.of(new Phone("iPhone 6 S", 54000), new Phone("Lumia 950", 45000),
//                 new Phone("Samsung Galaxy S 6", 40000));




//     Map<String, Object> filtration = new HashMap<>();

//     Scanner LaptopsScanner = new Scanner(System.in);

//     System.out.println("Выберите критерии для фильтрации:");
//     System.out.println("1 - процессор");
//     System.out.println("2 - память");
//     System.out.println("3 - операционная система");
//     System.out.println("4 - цвет");
//     System.out.println("0 - Завершить выбор");

//     int choice;
//     while (true) {
//         choice = LaptopsScanner.nextInt();
//         if (choice == 0) {
//             break;
//         }
//         switch (choice) {
//             case 1:
//                 System.out.println("Процессор?");
//                 filtration.put("cpu", LaptopsScanner.nextLine());
//                 //break;
//             case 2:
//                 System.out.println("Min Ram?");
//                 filtration.put("ram", LaptopsScanner.nextInt());
//                 //break;
//             case 3:
//                 System.out.println("Операционная система?");
//                 filtration.put("os", LaptopsScanner.next());
//                 //break;
//             case 4:
//                 System.out.println("Цвет?");
//                 filtration.put("color", LaptopsScanner.next());
//                 break;
//             default:
//                 System.out.println("Неверный выбор. Попробуйте снова.");
//         }
//     }

  

//     Set<Laptops> filteredLaptops = LaptopsSet.stream()

//             //.filter(Laptops-> filtration.getOrDefault("cpu", "") instanceof String && Laptops.cpu >= (String) filtration.getOrDefault("cpu", ""))
//             .filter(Laptops -> filtration.getOrDefault("ram", 0) instanceof Integer && Laptops.ram >= (int) filtration.getOrDefault("ram", 0))
//             .filter(Laptops -> filtration.getOrDefault("os", "").equals("") || Laptops.OS.equalsIgnoreCase((String) filtration.getOrDefault("os", "")))
//             .filter(Laptops -> filtration.getOrDefault("color", "").equals("") || Laptops.color.equalsIgnoreCase((String) filtration.getOrDefault("color", "")))
//             .collect(Collectors.toSet());

//     System.out.println("Отфильтрованные ноутбуки:");
//     for (Laptops Laptops : filteredLaptops) {
//         System.out.println(LaptopsSet);

//     }


   


