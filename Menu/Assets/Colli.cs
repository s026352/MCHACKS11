using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Colli : MonoBehaviour
{
    public GameObject objt;

    void Start(){
        objt.SetActive(false);
    }
    private void OnCollisionEnter(Collision collision)
    {
        objt.SetActive(true);

    }

    private void OnCollisionStay(Collision collision)
    {
        objt.SetActive(true);
    }

    private void OnCollisionExit(Collision collision)
    {
        objt.SetActive(false);
    }
}
