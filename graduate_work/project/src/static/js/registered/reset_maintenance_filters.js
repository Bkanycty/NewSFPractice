function reset_maintenance_filters() {
    var machine_factory_number = document.getElementById('maintenance-filter-machine-factory-number');
    var maintenance_type = document.getElementById('maintenance-filter-maintenance-type');
    var service_company = document.getElementById('maintenance-filter-service-company');

    machine_factory_number.value = '';
    maintenance_type.value = '';
    service_company.value = '';

    function show_all() {
        var rows_to_show = document.getElementById('maintenance-tab-table-data').children;
        for (var i = 0; i < rows_to_show.length; i+=1) {
            var row = rows_to_show[i];
            row.style.display = '';
        };
    };
    show_all();
};