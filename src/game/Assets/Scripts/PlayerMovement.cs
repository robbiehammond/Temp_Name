using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb2d;
    public float speed = 0.5f;

    // Start is called before the first frame update
    void Start()
    {
        rb2d = GetComponent<Rigidbody2D> ();
        rb2d.freezeRotation = true;

    }

    // Update is called once per frame
    void Update()
    {
        float deltaX = Input.GetAxisRaw("Horizontal") * speed;
        float deltaY = Input.GetAxisRaw("Vertical") * speed;

        Vector2 delta = new Vector2(deltaX, deltaY);
        delta *= Time.deltaTime;

        Debug.Log(deltaY);

        rb2d.velocity = delta;


        

        
    }
}
