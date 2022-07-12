$(document).ready(function () {
    var dt_table = $('#productionTable').dataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        order: [[0, "desc"]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {
                orderable: true,
                searchable: true,
                className: "center",
                targets: [0, 1]
            },
            {
                data: 'line',
                targets: [0]
            },
            {
                data: 'model',
                targets: [1]
            },
            {
                data: 'color',
                targets: [2]
            },
            {
                data: 'start_date',
                targets: [3]
            },
            {
                data: 'end_date',
                targets: [4]
            },
            {
                data: 'finished',
                targets: [5]
            },

        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL
    });
});