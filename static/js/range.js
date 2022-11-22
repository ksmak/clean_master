rangeElement = document.getElementById('room_size');
rangeValueElement = document.getElementById('room_size_value');

function updateRangeValue() {
    rangeValueElement.textContent = rangeElement.value;
}

rangeElement.addEventListener("input", function(e) {
    updateRangeValue();
}, false);

rangeElement.addEventListener("change", function(e) {
    updateRangeValue();
}, false);