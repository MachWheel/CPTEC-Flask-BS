$(document).ready(function () {
    addClassToTableColumn("weather-results", ["h4"], 1);
    addClassToTableColumn("weather-results", ["text-danger", "fw-bold"], 2);
    addClassToTableColumn("weather-results", ["text-primary", "fw-bold"], 3);
});

function addClassToTableColumn(tableId, classList, columnIndex) {
    var table = document.getElementById(tableId);
    for (var i = 1, row; row = table.rows[i]; i++) {
        for (var j=0; j < classList.length; j++) {
            row.cells[columnIndex].classList.add(classList[j]);
        }
    }
}
