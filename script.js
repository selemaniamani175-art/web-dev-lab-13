// Get elements
const scoreInput = document.getElementById("scoreInput");
const calcBtn = document.getElementById("calcBtn");
const results = document.getElementById("results");

// Button click event
calcBtn.addEventListener("click", calculateGrade);

function calculateGrade() {

    let score = Number(scoreInput.value);

    // Validation
    if (
        isNaN(score) ||
        scoreInput.value === "" ||
        score < 0 ||
        score > 100
    ) {

        results.innerHTML =
            "<p style='color:red;'>Please enter a valid score between 0 and 100.</p>";

        return;
    }

    let grade = "";

    // Grade calculation
    if(score >= 70){
        grade = "A";
    }
    else if(score >= 60){
        grade = "B";
    }
    else if(score >= 50){
        grade = "C";
    }
    else if(score >= 40){
        grade = "D";
    }
    else{
        grade = "F";
    }

    // Display result
    results.innerHTML = `
        <h3>Result</h3>
        <p>Score: ${score}</p>
        <p>Grade: ${grade}</p>
    `;

    // Reset input
    scoreInput.value = "";
}