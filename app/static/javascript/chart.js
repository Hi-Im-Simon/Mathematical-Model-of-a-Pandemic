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

function getChartData() {
    // reads all data from the HTML form
    let form_data = new FormData(document.querySelector('#input_form'));

    // creates a list of values from 0 to t
    let x_values = Array.from(Array(+(form_data.get('time')) + 1).keys());
    let y_values_all = calc(form_data);

    return [x_values, y_values_all];
}

function generateChart(chart_name = 'chart_1', action = 'update', data = getChartData()) {
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

var charts = {};
generateChart(chart_name='chart_1', action='create');
generateChart(chart_name='chart_2', action='create');