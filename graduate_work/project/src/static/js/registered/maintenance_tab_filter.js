function maintenance_filter() {
    var machine_factory_number = document.getElementById('maintenance-filter-machine-factory-number');
    var maintenance_type = document.getElementById('maintenance-filter-maintenance-type');
    var service_company = document.getElementById('maintenance-filter-service-company');
    var filters = [];
    
    function show_all() {
        var rows_to_show = document.getElementById('maintenance-tab-table-data').children;
        for (var i = 0; i < rows_to_show.length; i+=1) {
            var row = rows_to_show[i];
            row.style.display = '';
        };
    };
    show_all();

    machine_factory_number.value != '' ? filters.push(machine_factory_number.value) : false;
    maintenance_type.value != '' ? filters.push(maintenance_type.value) : false;
    service_company.value != '' ? filters.push(service_company.value) : false;

    if (filters.length != 0) {
        var rows = document.getElementById('maintenance-tab-table-data').children;
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