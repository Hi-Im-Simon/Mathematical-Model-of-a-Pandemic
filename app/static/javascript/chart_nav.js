function switch_chart(dest) {
    if (dest == 'left' && data_set_i > 0) {
        data_set_i -= 1;
    }
    else if (dest == 'right' && data_set_i < db['id'].length - 1) {
        data_set_i += 1;
    }
    else return;
    
    let data_set = new Map();
    for (entry in db)
        data_set.set(entry, db[entry][data_set_i]);
    let x_values = Array.from(Array(+(data_set.get('time')) + 1).keys());
    generateChart(chart_name='chart_2', action='update', data=[x_values, calc(data_set)]);
    document.getElementById('chart_id').innerHTML = data_set_i + 1;
}

var data_set_i = db['id'].length - 1;
document.getElementById('chart_id').innerHTML = db['id'].length;