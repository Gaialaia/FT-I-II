package Lesson_2;

import java.util.ArrayList;
import java.util.List;


public class Market implements Marketbehaviour, QueueBehavioor {


    private List<Actor> actorsList = new ArrayList();


    @Override
    public void takeInQueue(Actor actor) {
        System.out.println(actor.getName() + "in queue");
        actorsList.add(actor);
    }

    @Override
    public void takeOrders() {
        for (Actor actor : actorsList) {
            if(!actor.isMakeOrder()) {
                actor.setMakeOrder(true);
                System.out.println(actor.getName() + "has made an order");  
            }
        }
    }

    @Override
    public void giveOrders() {
        for (Actor actor : actorsList) {
            if(!actor.isMakeOrder()) {
                actor.setTakeOrder(true);
                System.out.println(actor.getName() + "has taken his order");  
            }
        }
        
    }

    @Override
    public void releaseFromQueue() {
        List<Actor> releasedActors = new ArrayList<>();
        for(Actor actor : actorsList) {
            if(actor.isTakeOrder()) {
                releasedActors.add(actor);
                System.out.println(actor.getName() + "left the queue");
            }
        }

        releaseFromMarket(releasedActors);
    }

    @Override
    public void acceptToMarket(Actor actor) {
        System.out.println(actor.getName() + "entered the store");
        takeInQueue(actor);
    }

    @Override
    public void releaseFromMarket(List<Actor> actors) {
       for (Actor actor: actors) {
        System.out.println(actor.getName()  + "left the store");
        actorsList.remove(actor);
       }
    }

    @Override
    public void update() {
       takeOrders();
       giveOrders();
       releaseFromQueue();
    }
    
   

    
    }

