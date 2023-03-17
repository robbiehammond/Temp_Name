using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT
}


//Singleton so the same information is seen everywhere
public sealed class PlayerInfo {
    public static PlayerInfo instance = null;
    private static readonly object threadLock = new object();
    private Direction mostRecentDirection;


    private PlayerInfo() {
        mostRecentDirection = Direction.DOWN;
    }
    public static PlayerInfo Instance {
        get {
            lock (threadLock) {
                if (instance == null)
                    instance = new PlayerInfo();
                return instance;
            }
        }
    }
    public void setLastDirection(float prevDX, float prevDY, float dX, float dY) {
        //if you start moving horizontally
        if (dX != 0 && dX != prevDX) {
            if (dX > 0)
                mostRecentDirection = Direction.RIGHT;
            else if (dX < 0)
                mostRecentDirection = Direction.LEFT;
        }

        //if you start moving vertically
        if (dY != 0 && dY != prevDY) {
            if (dY > 0)
                mostRecentDirection = Direction.UP;
            else if (dY < 0)
                mostRecentDirection = Direction.DOWN;
        }

        //if you let go of a horizontal keypress
        if (dX == 0 && dY != 0) {
            if (dY > 0)
                mostRecentDirection = Direction.UP;
            else if (dY < 0)
                mostRecentDirection = Direction.DOWN;
        }

        //if you let go of a vertical keypress
        if (dY == 0 && dX != 0) {
            if (dX > 0)
                mostRecentDirection = Direction.RIGHT;
            else if (dX < 0)
                mostRecentDirection = Direction.LEFT;
        }
    }

    public Direction getLastDirection() {
        return mostRecentDirection;
    }

}