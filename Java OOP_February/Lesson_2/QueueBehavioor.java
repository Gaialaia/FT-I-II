package Lesson_2;

public interface QueueBehavioor {
    
    void takeInQueue (Actor actor);

    void takeOrders();

    void giveOrders();

    void releaseFromQueue();
 
}
