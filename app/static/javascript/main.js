// set properties of inputs
for (el of document.querySelectorAll('.row_input')) {
    let children = []
    for (child of el.children)
        if (child instanceof HTMLInputElement)
            children.push(child)

    connectFollowingInput(children[0]);
    setChartGenerationProperty(children);
}

function setChartGenerationProperty(els) {
    for (el of els)
        el.addEventListener('input', function() { generateChart('chart_1', getChartData()) });
}

// connect selected input to its following input
function connectFollowingInput(el) {
    el.addEventListener('input', function () { this.nextElementSibling.value = this.value }, true);
    el.nextElementSibling.addEventListener('input', function () { this.previousElementSibling.value = this.value }, true);
}