// connect inputs
for (el of document.querySelectorAll('.connect_following_input')) {
    connectInputs(el);
}

// connect selected input to its following input
function connectInputs(el) {
    el.addEventListener('input', function () { this.nextElementSibling.value = this.value }, true);
    el.nextElementSibling.addEventListener('input', function () { this.previousElementSibling.value = this.value }, true);
}