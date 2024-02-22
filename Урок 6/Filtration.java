import java.util.stream.Stream;
import java.util.*;

public class Filtration {
  
    public static void main(String[] args) {
        
        Map<Integer, String> criteria = new HashMap<Integer, String>();
        criteria.put(1, null);
          criteria.put(2, null);
            criteria.put(3, null);
              criteria.put(4, null);

        


              System.out.println(criteria);
              System.out.println(criteria.get(criteria.values()));
              System.out.println(criteria.get(1));
          
        Scanner scanner = new Scanner(System.in);
        System.out.println(" Chose criteria number " );
        
      
        switch (scanner.nextInt()) {
            case 1:
                  System.out.println(" Enter CPU " );
                  String cpu = scanner.nextLine();
                  scanner.nextLine();
                  criteria.put(1, cpu);
                  

                  System.out.println(criteria);
                 
                
                  break;
            case 2:

                  System.out.println(" Enter RAM " );
                  String ram = scanner.nextLine();
                  scanner.nextLine();
                  criteria.put(2, ram);  
                  break;
            case 3:

                  System.out.println(" Enter RAM " );
                  String OS = scanner.nextLine();
                  scanner.nextLine();
                  criteria.put(2, OS);  
                  break;
            case 4:
             System.out.println(" Enter color " );
         String color = scanner.nextLine();
         scanner.nextLine();
         criteria.put(4, color);
         scanner.close();

         System.out.println(criteria);

            

                   
        }

        //  System.out.println(" Enter CPU " );
        //  String cpu = scanner.nextLine();
        //  criteria.put(1, cpu);          
           
        //  System.out.println(" Enter RAM " );
        //  String ram = scanner.nextLine();
        //  criteria.put(2, ram);


        
        //  System.out.println(" Enter OS" );
        //  String OS = scanner.nextLine();
        //  criteria.put(3, OS);

 
        //  System.out.println(" Enter color " );
        //  String color = scanner.nextLine();
        //  criteria.put(4, color);
        //  scanner.close();

        //   System.out.println(criteria.values());  //cpu...
        //  System.out.println(criteria.keySet());  // 1..
        //  System.out.println(criteria);

        //  Set<String> criteriaSet = new HashSet<> (criteria.values());
        //  System.out.println(criteriaSet);

        //  Stream<String> stream4 = criteriaSet.stream();

        //  stream4.filter(el -> el == "intel") 
        //          .forEach(System.out::println);

         //filter laptops with cpu = "..."  stream filter for this cpu...


      
    

         
        
      
    
        // Scanner criteriaScanner = new Scanner(System.in);
        // System.out.println("Enter criteria number  ");
        // int criterianumber = criteriaScanner.nextInt();



        //  Map<Integer, String> criteriaNames = new HashMap<Integer, String>();
        // switch (criterianumber) {
        //     case 1:
        //       System.out.println("Enter " + criteria.get(1));
        //       if (criteriaNames.containsKey(1)) {
        //         criteriaScanner.nextLine();
        //       String cpu = criteriaScanner.nextLine();
        //       criteriaNames.put(1, cpu);
        //       criteriaScanner.nextLine();
        //       break;
        //       }
             

        //     case 2:
        //        System.out.println("Enter " + criteria.get(2));
        //         criteriaScanner.nextLine();
        //         String ram = criteriaScanner.nextLine();
        //         criteriaNames.put(2, ram);
        //         criteriaScanner.nextLine();
                
                

        //     case 3:
        //      System.out.println("Enter " + criteria.get(3));
        //      criteriaScanner.nextLine(); 
        //      String OS = criteriaScanner.nextLine(); 
        //      criteriaNames.put(3, OS);
        //     criteriaScanner.nextLine();
            
               

        //     case 4:
        //      System.out.println("Enter " + criteria.get(4));
        //      String color = criteriaScanner.nextLine(); 
        //       criteriaScanner.nextLine();
        //       criteriaNames.put(4, color);
        //        criteriaScanner.nextLine();
        //       break;   

              

               
             
        // } 


        // System.out.println(criteriaNames);

    }

  }

         

    
  

    

              

        
    
         
    

    
    
    


    



        
        

      
