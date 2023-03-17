using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb2d;
    public float speed = 200.0f;

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
        Vector2 delta = new Vector2(deltaX, deltaY);

        //Debug.Log("dX: " + deltaX + " dY: " + deltaY);

        //make it FPS invariant
        delta *= Time.deltaTime;

        //set velocity to that change
        rb2d.velocity = delta;
    }
}
