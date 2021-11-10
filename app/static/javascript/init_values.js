// initial values
N = 13680470; // current population, int

Rh = 5;
Bt_s = 0.67;
Bt_a = 0.74;
Ps = 0.1; // % wearing masks, float
Xi = 0.5; // % infected fall because of masks, float
La_s = 0.1; // % for symptomatic people to get healthy, float
La_a = 0.1; // % for asymptomatic people to get healthy, float
La_q = 0.05; // % for people in quarantine people to get healthy, float
Al_s = 0.2; // % of symptomatic people isolating, float
Al_a = 0.2; // % of asymptomatic people isolating, float
De_s = 0.015; // fatafatality rate for symptomatic people, float
De_q = 0.015; // fatality rate for people in quarantine, float
Mu = 0.000036529; // ovrall fatality rate, float

I_s = parseInt(0.04 * N); // current amount of infected people with symptoms, int
I_a = parseInt(0.01 * N); // current amount of infected people without symptoms, int
S = N - I_s - I_a; // amount of not infected people, int
Q = 0; // amount of people in quarantine, int
R = 0; // amount of prople with immunity, int
D = 0; // amount of deaths, int


// setting initial values
setInputInitials(
    inputName = 'mask-rate',
    value = Ps
);

setInputInitials(
    inputName = 'mask-fall-rate',
    value = Xi,
);


// set the initial values of chosen input
// the last argument is optional and allows setting the same value to correlated inputs (defaults to 2, slider with number type input)
function setInputInitials(inputName, value, min=0, max=1, step=0.01, inputsCount=2) {
    let el = document.getElementsByName(inputName)[0];
    let elements = [];

    for (_ = 0; _ < inputsCount; _++) {
        el.min = min;
        el.max = max;
        el.step = step;
        el.value = value;

        elements.push(el);
        el = el.nextElementSibling;
    }

    for (e of elements) {
        e.addEventListener('input', function() {onInput2(e, elements)}, true);
    }
}
// much to change here
function onInput2(e, elements) {
    console.log(elements)
    for (ee of elements) {
        if (e != ee) {
            ee.value = e.value;
        }
    }
}
