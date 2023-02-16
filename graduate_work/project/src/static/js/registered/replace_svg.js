function replace_svg() {
    function getCoords(elem) {
    let box = elem.getBoundingClientRect();

        return {
            top: box.top + window.pageYOffset,
            right: box.right + window.pageXOffset,
            bottom: box.bottom + window.pageYOffset,
            left: box.left + window.pageXOffset
        };
    };

    document.getElementById('general-svg').style.top = getCoords(document.getElementById('general')).top
    document.getElementById('general-svg').style.left = getCoords(document.getElementById('general')).left
    document.getElementById('maintenances-svg').style.top = getCoords(document.getElementById('maintenances')).top
    document.getElementById('maintenances-svg').style.left = getCoords(document.getElementById('maintenances')).left
    document.getElementById('reclamations-svg').style.top = getCoords(document.getElementById('reclamations')).top
    document.getElementById('reclamations-svg').style.left = getCoords(document.getElementById('reclamations')).left
};
document.addEventListener("DOMContentLoaded", replace_svg);
window.addEventListener('resize', replace_svg);