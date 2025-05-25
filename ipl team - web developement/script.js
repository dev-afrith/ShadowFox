// Fan Poll Logic
document.getElementById("pollForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    const selectedPlayer = document.getElementById("player").value;
    let resultMessage = "Thank you for voting!";

    // Simple logic to show a personalized message based on the selected player
    switch(selectedPlayer) {
        case "dhoni":
            resultMessage = "You voted for MS Dhoni! The Captain Cool!";
            break;
        case "jadeja":
            resultMessage = "You voted for Ravindra Jadeja! The Super All-Rounder!";
            break;
        case "ruturaj":
            resultMessage = "You voted for Ruturaj Gaikwad! Rising Star!";
            break;
        case "moeen":
            resultMessage = "You voted for Moeen Ali! The Dynamic All-Rounder!";
            break;
        case "chahar":
            resultMessage = "You voted for Deepak Chahar! The Pace Maestro!";
            break;
        default:
            resultMessage = "Please select a player!";
    }

    // Display the result of the poll
    document.getElementById("pollResult").textContent = resultMessage;
});
