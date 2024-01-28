using UnityEngine;
using UnityEngine.UI; // Namespace for working with UI

public class ScoreCount : MonoBehaviour
{
    public Text countText; // Assign this in the inspector by dragging the Text object into this field
    public GameObject[] objectsToCheck; // Array of objects to check. Assign these in the inspector or find them dynamically during runtime if needed

    void Update()
    {
        int count = 0;

        // Iterate through each object and check its z-position
        foreach (GameObject obj in objectsToCheck)
        {
            if (obj.transform.position.y < -20)
            {
                count++;
            }
        }
        count = 30 + count*70/6;
        // Update the text object with the count
        countText.text = "Score: " + count.ToString();
    }
}
