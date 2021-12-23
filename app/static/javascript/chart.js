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

function getDataNames() {
    return {
        'S': 'people susceptible to infection',
        'I': 'infected people',
        'R': 'recovered people who obtained temporary immunity',
        'D': 'deaths due to disease',
        'V': 'vaccinated people',
        'N': 'alive population'
    };
}

function getChartData() {
    // reads all data from the HTML form
    let form_data = new FormData(document.querySelector('form'));

    // creates a list of values from 0 to t
    let x_values = Array.from(Array(+(form_data.get('_time')) + 1).keys());
    let y_values_all = calc(form_data);

    return [x_values, y_values_all];
}

function generateChart(action='update') {
    let t = getChartData();
    x_values = t[0];
    y_values_all = t[1];

    if (action == 'create') {
        let labels = getDataNames();

        chart = new Chart("chart_1", {
            type: "line",
            options: {
                animation: {
                    duration: 0,
                },
            },
        });

        for (let i = 0; i < lines.length; i++)
            chart.data.datasets.push({ data: y_values_all[lines[i]], borderColor: line_colors[lines[i]], label: labels[lines[i]], });
    }
    else {
        for (let i = 0; i < lines.length; i++)
            chart.data.datasets[i].data = y_values_all[lines[i]];
    }
    chart.data.labels = x_values;
    chart.update();
}

var chart;
generateChart(action='create');