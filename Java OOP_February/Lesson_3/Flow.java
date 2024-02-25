
// — Создать класс Поток, содержащий в себе список УчебныхГрупп и реализующий интерфейс Iterable;
// до 26 февр., 15:00 +05:00 UTC


package Lesson_3;

import java.util.Iterator;
import java.util.List;

public class Flow implements Iterable<StudentGroup>  {

    // Flow flow;

    String flowname;

    List<StudentGroup> studentGroupsList;

    public Flow(List<StudentGroup> studentGroupsList) {
        this.studentGroupsList = studentGroupsList;
    }

    public void add(StudentGroup studentGroup) {
        studentGroupsList.add(studentGroup);
    }

    @Override
    public Iterator<StudentGroup> iterator() {
        return new FlowGroupIterator(studentGroupsList);

    
    }


    public 
   
}




   
    

