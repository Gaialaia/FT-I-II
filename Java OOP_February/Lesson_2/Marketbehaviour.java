package Lesson_2;

import java.util.List;

public interface Marketbehaviour {
    
    void acceptToMarket (Actor actor);

    void releaseFromMarket (List<Actor> actors);

    void update();



    
}
