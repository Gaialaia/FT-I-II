package Lesson_3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// Создать класс ПотокСервис, добавив в него метод сортировки списка потоков, используя созданный

public class FlowService {

    Flow flow;

    public FlowService (Flow flow) {
        this.flow = flow;
    }

    public List <StudentGroup> getSortedFlows () {
        List <StudentGroup> studentGroupsFlow = new ArrayList<>(flow.studentGroupsList);
        Collections.sort(studentGroupsFlow);
    }


    public List <StudentGroup> getSortedFlows () {
        List <StudentGroup> studentGroupsFlow = new ArrayList<>(flow.studentGroupsList);
        Collections.sort(studentGroupsFlow);
    }

    



}


