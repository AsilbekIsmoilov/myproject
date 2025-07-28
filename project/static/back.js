let currentBackground = 0;

function loadBackgroundFromStorage() {
    const savedIndex = localStorage.getItem('backgroundIndex');
    if (savedIndex !== null && !isNaN(savedIndex)) {
        currentBackground = parseInt(savedIndex);
        setBackground(currentBackground);
    } else {
        setBackground(0);
    }
}

function setBackground(index) {
    if (backgrounds.length === 0) return;

    const bg = backgrounds[index % backgrounds.length];
    document.body.style.backgroundImage = `url('${bg}')`;
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundPosition = "center center";
    document.body.style.backgroundAttachment = "fixed";
    document.body.style.backgroundSize = "cover";
    document.body.style.transition = "background-image 0.5s ease";
}


function changeBackground() {
    currentBackground = (currentBackground + 1) % backgrounds.length;
    setBackground(currentBackground);
    localStorage.setItem('backgroundIndex', currentBackground);
}

document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("logo");
    if (logo) {
        logo.addEventListener("click", changeBackground);
        loadBackgroundFromStorage();
    }
});
