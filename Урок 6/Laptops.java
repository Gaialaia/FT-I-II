
public class Laptops {

    String name;
    String model;
    String color;
    String cpu;
    // String graphics;
    // double driveCapacity;
    String OS;
    int ram;
    // short OStype;
    // double screenSize;
    
    Laptops ( String name,
    String model,
    String color, String cpu, String OS,
    int ram ) {
    // String graphics,
    // double driveCapacity,
    // String OS,
    // short OStype,
    // double screenSize) {
        this.name = name;
        this.model = model;
        this.color = color;
        this.cpu = cpu;
        this.OS = OS;
        this.ram = ram;
        // this.graphics = graphics;
        // this.driveCapacity = driveCapacity;
        // this.OS = OS;
        // this.OStype = OStype;
        // this.screenSize = screenSize;


        
    
    }
    public String toString() {
        return name + "\n" + model + "\n" + color + "\n" + cpu + "\n" + OS + "\n" + ram;  //"name : " +
    }

    public String getName() {
        return name;
    }

    public String getModel() {
        return model;
    }

    
    public String getColor() {
        return color;
    }

      public String getCPU() {
        return cpu;
    }

      public String getOS() {
        return OS;
    }

    public Integer getRam() {
        return ram;

    }


    







   
}
    

    
   
    
    
    






   