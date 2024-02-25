package Lesson_3;

import java.util.Iterator;
import java.util.List;

public class StudentGroup implements Iterable<Student> {
    
    
    
    List<Student> studentList;  // список студентов, из которого состоит группа


    // int StudentGroup;




    public StudentGroup(List<Student> studentList) {
        this.studentList = studentList;
    }

    public void add(Student student) {
        studentList.add(student);
    }

    @Override
    public Iterator<Student> iterator() {
        return new StudentGroupIterator(this); //передаём ссылку на экзепляр, с которым сейчас работаем
        
    }


    
}
