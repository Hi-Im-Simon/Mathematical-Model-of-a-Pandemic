function generateChart() {
    // read the simulation time
    let x_len = document.getElementsByName('_time')[0].value;
    // create a list from 0 to `x_len`
    let x_values = Array.from(Array(+(x_len) + 1).keys());
    let y_values = [7];

    new Chart("chart_1", {
        type: "line",
        data: {
            labels: x_values,
            datasets: [{
                backgroundColor: "rgba(0,0,0,1.0)",
                borderColor: "rgba(0,0,0,0.1)",
                data: y_values,
            }]
        },
        options: {}
    });
}