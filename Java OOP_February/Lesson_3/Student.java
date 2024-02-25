package Lesson_3;

public class Student implements Comparable<Student> {
    
    public Integer studentID;
    public String firstname;
    public String secondname;
    public String lastname;

    public Student(Integer studentID, String firstname, String secondname, String lastname) {
        this.studentID = studentID;
        this.firstname = firstname;
        this.secondname = secondname;
        this.lastname = lastname;
    }

    @Override
    public String toString() {
        return "Student [studentID=" + studentID + ", firstname=" + firstname + ", secondname=" + secondname
                + ", lastname=" + lastname + "]";
    }

    @Override
    public int compareTo(Student o) {
        // if(studentID > o.studentID )
        // return 1;
        // if(studentID < o.studentID)
        // return -1;

        // return 0;
        return studentID.compareTo(o.studentID);
        
        
    }

    
    
}
