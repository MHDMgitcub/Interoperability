let timer;
let isRunning = false;
let elapsedTime = localStorage.getItem("elapsedTime") || 0;
let startTime;
let savedTimes = JSON.parse(localStorage.getItem("savedTimes")) || [];

const progressCircle = document.querySelector(".progress-ring-circle");
const totalLength = 2 * Math.PI * 70; // Circumference of the circle
progressCircle.style.strokeDasharray = totalLength;

document.addEventListener("DOMContentLoaded", function () {
    updateDisplay();
    loadSavedTimes();
    updateProgressRing();
});

function startStopwatch() {
    if (!isRunning) {
        startTime = Date.now() - elapsedTime;
        timer = setInterval(updateTime, 100);
        isRunning = true;
        localStorage.setItem("isRunning", "true");
    }
}

function stopStopwatch() {
    if (isRunning) {
        clearInterval(timer);
        isRunning = false;
        localStorage.setItem("isRunning", "false");
    }
}

function resetStopwatch() {
    clearInterval(timer);
    isRunning = false;
    elapsedTime = 0;
    updateDisplay();
    updateProgressRing();
    localStorage.setItem("elapsedTime", 0);
    localStorage.setItem("isRunning", "false");
}

function updateTime() {
    elapsedTime = Date.now() - startTime;
    updateDisplay();
    updateProgressRing();
    localStorage.setItem("elapsedTime", elapsedTime);
}

function updateDisplay() {
    let time = new Date(elapsedTime);
    let minutes = String(time.getUTCMinutes()).padStart(2, "0");
    let seconds = String(time.getUTCSeconds()).padStart(2, "0");
    let milliseconds = String(Math.floor(time.getUTCMilliseconds() / 100)).padStart(1, "0");
    document.getElementById("display").textContent = `${minutes}:${seconds}:${milliseconds}`;
}

function updateProgressRing() {
    let timeInSeconds = elapsedTime / 1000;
    let progress = (timeInSeconds % 60) / 60; // Resets every 60 seconds
    progressCircle.style.strokeDashoffset = totalLength * (1 - progress);
}

function saveTime() {
    savedTimes.push(document.getElementById("display").textContent);
    localStorage.setItem("savedTimes", JSON.stringify(savedTimes));
    loadSavedTimes();
}

function loadSavedTimes() {
    let list = document.getElementById("savedTimes");
    list.innerHTML = "";
    savedTimes.forEach(time => {
        let li = document.createElement("li");
        li.textContent = time;
        list.appendChild(li);
    });
}