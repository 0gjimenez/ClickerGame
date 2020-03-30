using System.Collections;
using System.Collections.Generic;
using Unityengine;

public class MainButtionClick : MonoBehaviour {
    "try to add a name set if you can George"

    public GameObject textBox;

    public void Encryption() {
        textBox.SetActive (true);
    }
    public void Phishing() {
        textBox.SetActive (false);
        "When encryption reaches a certain level Phishing need to be clicked"
    }
    public void Time() {
        textBox.SetActive (true);
        "Add time to each time a button is pressed"
    }
    public void Age() {
        textBox.SetActive (true);
        "try to see if you can add it with years and months"
    }
    public void PoliceTracker() {
        textBox.SetActive (false);
        "when the Phishing button to reach a certain level this increases"
    }
    public void Firewall() {
        textBox.SetActive(false);
        "when the police tracker is active roll a dice i greater than 50 the police tracker goes to zero if less than fifty police tracker goes up by one"
        
    }
}    
