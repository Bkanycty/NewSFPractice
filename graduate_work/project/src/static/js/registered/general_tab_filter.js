function general_filter() {
    var machine_model = document.getElementById('general-filter-machine-model');
    var machine_factory_number = document.getElementById('general-filter-machine-factory-number');
    var engine_model = document.getElementById('general-filter-engine-model');
    var transmission_model = document.getElementById('general-filter-transmission-model');
    var drive_axle_model = document.getElementById('general-filter-drive-axle-model');
    var steering_axle_model = document.getElementById('general-filter-steering-axle-model');
    var filters = [];
    
    function show_all() {
        var rows_to_show = document.getElementById('general-tab-table-data').children;
        for (var i = 0; i < rows_to_show.length; i+=1) {
            var row = rows_to_show[i];
            row.style.display = '';
        };
    };
    show_all();

    machine_model.value != '' ? filters.push(machine_model.value) : false;
    machine_factory_number.value != '' ? filters.push(machine_factory_number.value) : false;
    engine_model.value != '' ? filters.push(engine_model.value) : false;
    transmission_model.value != '' ? filters.push(transmission_model.value) : false;
    drive_axle_model.value != '' ? filters.push(drive_axle_model.value) : false;
    steering_axle_model.value != '' ? filters.push(steering_axle_model.value) : false;

    if (filters.length != 0) {
        var rows = document.getElementById('general-tab-table-data').children;
        for (var i = 0; i < rows.length; i+=1) {
            var row = rows[i]; // Определяем строки для фильтрации
            var data_to_filter = []; // Список значений в ячейках строки

            for (var j = 0; j < row.children.length; j+=1) {
                var td = row.children[j].textContent;
                data_to_filter.push(td); // Закидываем содержимое ячеек в список
                };
            var check_list = []; // Список true/false значений
            for (let k = 0; k < filters.length; k+=1) {
                check_list.push(data_to_filter.includes(filters[k]));
            };
            let check = check_list.every(function(elem) { // функция проверки, все ли фильтры находятся в строке
                if (elem == true) {
                    return true;
                } else {
                    return false;
                };
            });
            if (check == false) { // если не все фильтры в строке, она скрывается
                let row_to_hide = document.getElementById(row.id);
                row_to_hide.style.display = 'none';
            };
        };
    }
    else { // ничего не делаем, если все фильтры сброшены
        ;
        };
};