// set properties of inputs
for (el of document.querySelectorAll('.row-input')) {
    let children = []
    for (child of el.querySelectorAll('*'))
        if (child instanceof HTMLInputElement)
            children.push(child)

    connectFollowingInput(children[0]);
    setChartGenerationProperty(children);
    setPropertiess(children);
}

function setChartGenerationProperty(els) {
    for (el of els)
        el.addEventListener('input', function() { generateChart('chart-1', getChartData()) });
}

function setPropertiess(els) {
    for (el of els) {
        if (el.type == 'number') {
            prev_el = el.previousElementSibling;
            step = prev_el.step; min = prev_el.min; max = prev_el.max; value = prev_el.value;
            el.step = step < 1 ? step / 100 : 1;
            el.min = min; el.max = max; el.value = value;
            el.placeholder = prev_el.min + ' — ' + prev_el.max;
        }
    }
}

// connect selected input to its following input
function connectFollowingInput(el) {
    el.addEventListener('input', function () { this.nextElementSibling.value = this.value }, true);
    el.nextElementSibling.addEventListener('input', function () { this.previousElementSibling.value = this.value }, true);
}