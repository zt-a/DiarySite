


function clearField(fieldId) {
    document.getElementById(fieldId).value = '';
};


var count = 0;
function displayDateTime() {
    var currentDate = new Date();

    var date = currentDate.toDateString();
    var time = currentDate.toLocaleTimeString();
    count = count + 1;

    var dateElement = document.getElementById("date");
    var timeElement = document.getElementById("time");
    var networkElement = document.getElementById("in_network");

    dateElement.textContent = "Дата: " + date;
    timeElement.textContent = "Время: " + time;
    networkElement.textContent = "В сети: " + count + "сек.";
};



