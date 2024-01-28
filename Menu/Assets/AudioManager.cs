using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioManager : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        GameObject audioManager = GameObject.Find("Music");

        if (audioManager != null)
        {
            // Get the AudioSource component from AudioManager
            AudioSource audioSource = audioManager.GetComponent<AudioSource>();

            // Start playing the audio
            if (audioSource != null && !audioSource.isPlaying)
            {
                audioSource.Play();
            }
        }
        else
        {
            Debug.LogWarning("AudioManager not found in the scene.");
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
