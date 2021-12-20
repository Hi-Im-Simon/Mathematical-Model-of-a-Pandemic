function generateChart() {
    // read all data from the HTML form
    let form_data = new FormData(document.querySelector('form'));
    let y_values_all = calc(form_data);
    
    // creates a list of values from 0 to t
    let x_values = Array.from(Array(+(form_data.get('_time')) + 1).keys());
    console.log(form_data.keys())

    var datasets_predef = [];
    for (let y_values of y_values_all) {
        datasets_predef.push({ data: y_values, borderColor: "rgba(0,0,0,0.1)",})
    }

    new Chart("chart_1", {
        type: "line",
        data: {
            labels: x_values,
            datasets: datasets_predef,
        },
        options: {
            animation: {
                duration: 0,
            }
        }
    });
}

function getDataNames() {
    // it will return names of data lines that will lable them in the chart
}

generateChart();