function reset_reclamation_filters() {
    var broken_node = document.getElementById('reclamation-filter-broken-node');
    var recovery_method = document.getElementById('reclamation-filter-recovery-method');
    var service_company = document.getElementById('reclamation-filter-service-company');

    broken_node.value = '';
    recovery_method.value = '';
    service_company.value = '';

    function show_all() {
        var rows_to_show = document.getElementById('reclamation-tab-table-data').children;
        for (var i = 0; i < rows_to_show.length; i+=1) {
            var row = rows_to_show[i];
            row.style.display = '';
        };
    };
    show_all();
};