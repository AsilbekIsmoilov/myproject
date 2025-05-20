document.addEventListener("DOMContentLoaded", function () {
    let dateSpan = document.getElementById("date");
    let today = new Date();
    let options = {
        month: 'long',
        year: 'numeric'
    };
    let formattedDate = today.toLocaleDateString('ru-RU', options);

    formattedDate = formattedDate.charAt(0).toUpperCase() + formattedDate.slice(1);

    dateSpan.textContent = formattedDate;
    });
const scoreElement = document.querySelector("#score-value");


const ctx = document.getElementById('scoreChart').getContext('2d');
const score = parseInt("{{ selected_operator.mark|default:0 }}");

let scoreColor = '';
if (score < 80) {
    scoreColor = '#FF0000';
} else if (score <= 82) {
    scoreColor = '#ffeb3b';
} else {
    scoreColor = '#00ff00';
}

new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Баллы', 'Остаток'],
        datasets: [{
            label: 'Оценка',
            data: [score, 100 - score],
            backgroundColor: [scoreColor, 'transparent'],
            borderColor: ['#ffffff', '#ffffff'],
            borderWidth: 01,
            borderRadius: 01,
            spacing: 5
        }]
    },
    options: {
        cutout: '70%',
        responsive: false,
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            }
        }
    }
});
function filterDropdown() {
    const input = document.getElementById("operator-name");
    const filter = input.value.toLowerCase();
    const dropdown = document.getElementById("dropdown");
    const items = dropdown.getElementsByClassName("dropdown-item");

    if (filter.length === 0) {
        dropdown.style.display = "none";
        return;
    }

    let anyVisible = false;
    for (let item of items) {
        const name = item.getAttribute("data-name").toLowerCase();

        if (name.includes(filter) || name.startsWith(filter)) {
            item.style.display = "block";
            anyVisible = true;
        } else {
            item.style.display = "none";
        }
    }

    dropdown.style.display = anyVisible ? "block" : "none";
}

document.querySelectorAll(".dropdown-item").forEach(item => {
    item.addEventListener("click", function() {
        const name = this.getAttribute("data-name");
        document.getElementById("operator-name").value = name;
        document.getElementById("dropdown").style.display = "none";
        document.getElementById("operator-form").submit(); // 👉 Отправка формы
    });
});

document.addEventListener("click", function(event) {
    const input = document.getElementById("operator-name");
    const dropdown = document.getElementById("dropdown");
    if (!input.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.style.display = "none";
    }
});

