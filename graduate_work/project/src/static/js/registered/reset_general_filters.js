function reset_general_filters() {
    var machine_model = document.getElementById('general-filter-machine-model');
    var machine_factory_number = document.getElementById('general-filter-machine-factory-number');
    var engine_model = document.getElementById('general-filter-engine-model');
    var transmission_model = document.getElementById('general-filter-transmission-model');
    var drive_axle_model = document.getElementById('general-filter-drive-axle-model');
    var steering_axle_model = document.getElementById('general-filter-steering-axle-model');

    machine_model.value = '';
    machine_factory_number.value = '';
    engine_model.value = '';
    transmission_model.value = '';
    drive_axle_model.value = '';
    steering_axle_model.value = '';

    function show_all() {
        var rows_to_show = document.getElementById('general-tab-table-data').children;
        for (var i = 0; i < rows_to_show.length; i+=1) {
            var row = rows_to_show[i];
            row.style.display = '';
        };
    };
    show_all();
};