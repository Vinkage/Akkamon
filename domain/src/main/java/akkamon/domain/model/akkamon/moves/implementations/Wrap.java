package akkamon.domain.model.akkamon.moves.implementations;

import akkamon.domain.model.akkamon.Mon;
import akkamon.domain.model.akkamon.Stat;
import akkamon.domain.model.akkamon.moves.MoveCategory;

public class Wrap extends Mon.Move {

    public Wrap(String name, Mon.Type type, MoveCategory category, Stat PP, int power, double accuracy) {
        super(name, type, category, PP, power, accuracy);
    }

    @Override
    public void startTurn() {

    }

    @Override
    public void fight() {

    }

    @Override
    public void getAttacked() {

    }

    @Override
    public void useItem() {

    }

    @Override
    public void switchOut() {

    }

    @Override
    public void endTurn() {

    }
}
