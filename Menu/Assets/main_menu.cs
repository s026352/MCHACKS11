using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System;
using System.Threading;

public class main_menu : MonoBehaviour
{
    public void Punch_9prof (){
        SceneManager.LoadScene("s2/SampleScene");
    }

    public void Punch_Boris (){
        SceneManager.LoadScene("s2/SampleSceneBoris");
    }

    public void Punch_Alberini (){
        SceneManager.LoadScene("s2/SampleSceneAlberini");
    }

    public void Punch_Campbell (){
        SceneManager.LoadScene("s2/SampleSceneCampbell");
    }

    public void Punch_Custom (){
        Thread.Sleep(150000);
        SceneManager.LoadScene("s2/SampleSceneCustom");
    }

    public void Punch_Erring (){
        SceneManager.LoadScene("s2/SampleSceneErrington");
    }

    public void Punch_Kanaan (){
        SceneManager.LoadScene("s2/SampleSceneKanaan");
    }

    public void Punch_Mahes (){
        SceneManager.LoadScene("s2/SampleSceneMahes");
    }

    public void Punch_McGill (){
        SceneManager.LoadScene("s2/SampleSceneMcGill");
    }

    public void Punch_Vetta (){
        SceneManager.LoadScene("s2/SampleSceneVetta");
    }
    

    public void Punch_cust (){
        SceneManager.LoadScene(2);
    }

    public void Quit(){
        Debug.Log("Quit");
        Application.Quit();
    }
}
