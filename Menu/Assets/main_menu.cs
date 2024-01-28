using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class main_menu : MonoBehaviour
{
    public void Punch_9prof (){
        SceneManager.LoadScene(1);
    }

    public void Punch_cust (){
        SceneManager.LoadScene(2);
    }

    public void Quit(){
        Debug.Log("Quit");
        Application.Quit();
    }
}
