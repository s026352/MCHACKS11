using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;

public class ScriptToLoad : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
/*
    public void LoadGame()
    {
        UnityEngine.Debug.Log("Load Game Button pressed");

        string unityExecutablePath = @"C:\Program Files\Unity\Hub\Editor\2022.3.18f1\Editor\Unity.exe";

        // Close the current instance of Unity
        Process.GetCurrentProcess().Kill();

        // Start a new instance of Unity
        Process.Start(unityExecutablePath);

        //UnityEngine.SceneManagement.SceneManager.LoadScene("Scenes/SampleScene");
    }*/



    public void LoadGame()
    {
        UnityEngine.Debug.Log("Load Game Button pressed");

        UnityEngine.SceneManagement.SceneManager.LoadScene("Scenes/SampleScene");
    }

    public void RunScript()
    {
        UnityEngine.Debug.Log("Run Script Button pressed");

        string pythonScriptPath = @"C:\Users\johnp\Documents\JP\McGill\MeshyAPI.py"; // Set the correct path
        string pythonInterpreterPath = "C:\\Program Files\\Python311\\python.exe"; // Set the correct path

        // Create a new process to run the Python script
        Process process = new Process();
        process.StartInfo.FileName = pythonInterpreterPath;
        process.StartInfo.Arguments = pythonScriptPath;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.RedirectStandardError = true;
        process.StartInfo.CreateNoWindow = true;

        // Start the process
        process.Start();

        // Optionally, you can read the output and error streams if needed
        string output = process.StandardOutput.ReadToEnd();
        string error = process.StandardError.ReadToEnd();

        // Wait for the process to finish
        process.WaitForExit();

        // Close the process
        process.Close();

        // Print output and error if needed
        UnityEngine.Debug.Log("Output: " + output);




        // the bottom line is commented out to avoid an error logging into unity
        // UnityEngine.Debug.Log("Error: " + error);
    }
}
