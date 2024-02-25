package Lesson_3;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        
        Student student1 = new Student(123, "Jose", "Ramon", "Velaskess");
        Student student2 = new Student(345, "Juan", "Carlos", "Castaneda");
        Student student3 = new Student(678, "Petr", "Ivanovich", "Sveridof");
        Student student4 = new Student(876, "Malena", "Ramon", "Heito");
        Student student5 = new Student(543, "Svetlana", "Igorevna", "Popova");
        Student student6 = new Student(23, "Azetdinne", "Asad", "Tirel");
        Student student7 = new Student(1231, "Jenya", "Vladimirovna", "Chistyakova");

        List <Student> studentList = new ArrayList<>();

       StudentGroup studentGroup1 = new StudentGroup(studentList);
       StudentGroup studentGroup2 = new StudentGroup(studentList);
      

        studentGroup1.add(student1);
        studentGroup1.add(student2);
        studentGroup1.add(student3);
        studentGroup1.add(student4);
        studentGroup1.add(student7);

        studentGroup2.add(student5);
        studentGroup2.add(student6);








        // StudentGroupIterator iterator = new StudentGroupIterator(studentGroup1);
        // while (iterator.hasNext()) {
        //     Student student = iterator.next();
        //     if(student.studentID == 23)  
        //     iterator.remove();
        //     else
        //     System.out.println(student);
        //  {  
        // }  не надо так как теперь ест Iterable

        for(Student student : studentGroup1) {
            System.out.println(student);
        }
    

    StudentGroupService service = new StudentGroupService(studentGroup1);

    for (Student st : service.getSortedStudentGroup()) {
        System.out.println("sorted gtoup: " + st);
    }


    for (Student st : service.getSortedStudentGroupbyName()) {
        System.out.println("sorted by name :" + st);
    }

    List <StudentGroup> studentGroup1List = new ArrayList<>();

    studentGroup1List.add(studentGroup2);
    for (StudentGroup sGroup : studentGroup1List) {
        System.out.println("student group: " + sGroup);
    }


    Flow flow1 = new Flow(studentGroup1List);

    FlowGroupIterator flowGroupIterator1 = new FlowGroupIterator(studentGroup1List);


    




    }


    }

