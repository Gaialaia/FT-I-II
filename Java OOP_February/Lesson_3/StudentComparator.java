package Lesson_3;

import java.util.Comparator;

public class StudentComparator implements Comparator <Student> {

    @Override
    public int compare(Student o1, Student o2) {
        int resultOfComparing = o1.secondname.compareTo(o2.secondname);
        if (resultOfComparing == 0) {}
            resultOfComparing = o1.firstname.compareTo(o2.firstname);
            if(resultOfComparing == 0) {
                return o1.lastname.compareTo(o2.lastname);
            } else {
                return resultOfComparing;
           
                
            }
    } 
}




    

