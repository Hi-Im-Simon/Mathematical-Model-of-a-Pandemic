// change the order in which labels should be displayed
var lines = ['S', 'I', 'R', 'D', 'V', 'N'];

// change chart lines colors
var line_colors = {
    'S': 'yellow',
    'I': 'red',
    'R': 'green',
    'D': 'black',
    'V': 'blue',
    'N': 'gray'
};

// retrieves chart data from inputs
function getChartData() {
    // reads all data from the HTML form
    let form_data = new FormData(document.querySelector('#input_form'));

    // creates a list of values from 0 to t
    let x_values = Array.from(Array(+(form_data.get('time')) + 1).keys());
    let y_values_all = calc(form_data);

    return [x_values, y_values_all];
}

// Generate a chart
// An HTML element with a `chart_name` id must exist
// To use the data from currently filled form, pass `getChartData()` to the `data` parameter, otherwise it must be passed
// a map of all elements from the chosen row from the database   
// To generate a chart for the first time, `action` parameter must be specified to `create`, then the parameter does not need to be specified
function generateChart(chart_name, data, action = 'update') {
    x_values = data[0];
    y_values_all = data[1];

    if (action == 'create') {
        let labels = getTranslations();

        charts[chart_name] = new Chart(chart_name, {
            type: "line",
            options: {
                animation: {
                    duration: 0,
                },
            },
        });

        for (let i = 0; i < lines.length; i++)
            charts[chart_name].data.datasets.push({ data: y_values_all[lines[i]], borderColor: line_colors[lines[i]], label: labels[lines[i]][chosen_language], });
    }
    else {
        for (let i = 0; i < lines.length; i++)
            charts[chart_name].data.datasets[i].data = y_values_all[lines[i]];
    }
    charts[chart_name].data.labels = x_values;
    charts[chart_name].update();
}

// switches the comparison chart left or right
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
    generateChart(chart_name = 'chart_2', action = 'update', data = [x_values, calc(data_set)]);
    document.getElementById('chart_id').innerHTML = data_set_i + 1;
}

var data_set_i = db['id'].length - 1;
document.getElementById('chart_id').innerHTML = db['id'].length;

var charts = {};
generateChart(chart_name='chart_1', data=getChartData(), action='create');
generateChart(chart_name='chart_2', data=getChartData(), action='create');