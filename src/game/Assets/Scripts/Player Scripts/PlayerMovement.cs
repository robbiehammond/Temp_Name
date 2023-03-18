using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb2d;
    public float speed = 100.0f;
    private PlayerInfo playerInformation = PlayerInfo.Instance;
    public Animator animator;
    
    //to see which direction is the most "recent" press
    private float prevDeltaX = 0.0f;
    private float prevDeltaY = 0.0f;

    void Start()
    {
        rb2d = GetComponent<Rigidbody2D> ();
        rb2d.freezeRotation = true;
    }

    void Update()
    {
        //get change in X and Y
        float deltaX = Input.GetAxisRaw("Horizontal") * speed;
        float deltaY = Input.GetAxisRaw("Vertical") * speed;
        Direction lastDir = playerInformation.getLastDirection();
        playerInformation.setLastDirection(prevDeltaX, prevDeltaY, deltaX, deltaY);

        //only indicate to animator when the direction is actually changed.
        //sending a message each time causes the animation to reset each frame, which is obviously bad.
        if (lastDir != playerInformation.getLastDirection())
            triggerAnimator(playerInformation.getLastDirection());


        Vector2 delta = new Vector2(deltaX, deltaY);

        //Debug.Log(playerInformation.getLastDirection());

        //make it FPS invariant
        delta *= Time.deltaTime;

        //set velocity to that change
        rb2d.velocity = delta;


        prevDeltaX = deltaX;
        prevDeltaY = deltaY;
    }


    private void triggerAnimator(Direction d) {
        animator.SetTrigger(d.ToString());
    }
}
