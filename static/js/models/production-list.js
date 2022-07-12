$(document).ready(function () {
    var dt_table = $('#productionTable').DataTable({
        language: {
            url: LANG
        },

        dom: 'r<t>lp',
  
        order: [[3, "desc"]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {
                orderable: true,
                searchable: true,
                targets: [0, 1, 2, 3, 4, 5]
            },
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: JSON_URL
    });

    

    $('#buscarProducciones').on( 'keyup', function () {
        dt_table.search( this.value ).draw();
    } );

}
);

