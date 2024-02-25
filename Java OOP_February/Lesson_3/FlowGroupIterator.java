package Lesson_3;

import java.util.Iterator;
import java.util.List;

public class FlowGroupIterator implements Iterator <StudentGroup> {

    List<StudentGroup> studentGroupsList;

    int counter = 0;

    public FlowGroupIterator(List<StudentGroup> studentGroupsList) {
        this.studentGroupsList = studentGroupsList;
    }

    @Override
    public boolean hasNext() {
        return counter < studentGroupsList.size();
    }

    @Override
    public StudentGroup next() {
        if (!hasNext())
        return null;

        return studentGroupsList.get((counter ++));
        
        
    }

    @Override
    public void remove() {
        if(hasNext())
        studentGroupsList.remove(--counter);
    }

    


    
}
