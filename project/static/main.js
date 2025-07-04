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


// Персональный рост / спад
new Chart(document.getElementById("growthChart"), {
  type: "line",
  data: {
    labels: ["Янв", "Фев", "Мар"],
    datasets: [
      {
        data: [87.5, 74, 81.5],
        fill: true,
        tension: 0.4,
        borderColor: "#3b82f6",
        backgroundColor: "rgba(59,130,246,0.15)",
        pointBackgroundColor: "#fff",
        pointBorderColor: "#3b82f6",
        pointRadius: 5,
        pointHoverRadius: 7,
        pointStyle: "circle"
      }
    ]
  },
  options: {
    plugins: {
      legend: { display: false },
      tooltip: {
        enabled: true,
        backgroundColor: "rgba(0,0,0,0.7)",
        titleColor: "#ff3b3b",
        bodyColor: "#93c5fd",
        padding: 10,
        borderWidth: 1,
        borderColor: "#3b82f6"
      }
    },
    scales: {
      y: {
        min: 50,
        max: 95,
        ticks: {
          color: "#cbd5e1"
        },
        grid: {
          color: "rgba(255,255,255,0.05)",
          drawTicks: false
        }
      },
      x: {
        ticks: {
          color: "#e2e8f0"
        },
        grid: {
          display: false
        }
      }
    }
  }
});

// Круговая диаграмма "Соотношение критериев"
new Chart(document.getElementById("ratioChart"), {
  type: "doughnut",
  data: {
    labels: ["Консультация", "Остальные"],
    datasets: [
      {
        data: [35, 65],
        backgroundColor: ["#6366f1", "#1e293b"],
        cutout: "70%"
      }
    ]
  },
  options: {
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#1f2937",
        bodyColor: "#ff3b3b",
        titleColor: "#93c5fd",
        borderColor: "#6366f1",
        borderWidth: 1
      }
    }
  }
});

// Генерация донатов по критериям
const donutConfig = [
  { title: "Приветствие / Прощание", data: [1, 1, 1] },
  { title: "Внимательное слушание", data: [1, 3, 1] },
  { title: "Исп. уточняющих вопросов", data: [0, 0, 0] },
  { title: "Заинтересованность в проблеме", data: [0, 1, 1] },
  { title: "Консультация / Понятное пред. инф.", data: [1, 0, 1] },
  { title: "Доброжелательность, Вежливость", data: [0, 0, 0] },
  { title: "Грамотная речь", data: [0, 0, 1] },
  { title: "Оформление и обработка заявок", data: [0, 0, 0] },
  { title: "Предупреждение об ожидании", data: [0, 1, 0] },
  { title: "Эмоц. окраска голоса / Темп диалога", data: [1, 0, 2] },
  { title: "Быстрое решение вопроса", data: [0, 0, 1] }
];

const topGrid = document.getElementById("donutTop");
const bottomGrid = document.getElementById("donutBottom");

donutConfig.forEach((cfg, i) => {
  const total = cfg.data.reduce((a, b) => a + b, 0);
  const wrap = document.createElement("div");
  wrap.className = "indicator";
  wrap.innerHTML = `
    <h3>${cfg.title}</h3>
    <div style="position:relative; display:inline-block;">
      <canvas id="d${i}"></canvas>
      <div style="
        position:absolute;
        top:50%;
        left:50%;
        transform:translate(-50%,-50%);
        font-size:1.2rem;
        font-weight:bold;
        color:#f43f5e;">${total}</div>
    </div>
    <div class="months">
      <span data-count="${cfg.data[0]}">Янв</span>
      <span data-count="${cfg.data[1]}">Фев</span>
      <span data-count="${cfg.data[2]}">Мар</span>
    </div>
  `;

  // Разделим: первые 5 наверх, остальные вниз
  if (i < 5) topGrid.appendChild(wrap);
  else bottomGrid.appendChild(wrap);

  new Chart(document.getElementById(`d${i}`), {
    type: "doughnut",
    data: {
      labels: ["Янв", "Фев", "Мар"],
      datasets: [{
        data: cfg.data,
        backgroundColor: ["#3b82f6", "#f43f5e", "#9333ea"],
        cutout: "70%"
      }]
    },
    options: {
      plugins: { legend: { display: false }, tooltip: { enabled: false } },
      rotation: -0.5 * Math.PI
    }
  });
});

// Комментарии
const comments = `
  <p><strong>Код звонка:</strong> 665392861<br>Грубая ошибка (–25): Тишина...</p>
  <p><strong>Код звонка:</strong> 666304561<br>Грубая ошибка (–25): Неверная информация...</p>
  <p><strong>Код звонка:</strong> 661668011<br>Ошибка (–10): Оператор не нашёл предыдущее обращение…</p>
  <p><strong>Код звонка:</strong> 671100001<br>Недочёт (–2): Неверно заполнены данные…</p>
`;
document.getElementById("commentsBox").innerHTML = comments;

// Обработка фамилии
document.getElementById("nameSearch").addEventListener("input", function () {
  const name = this.value;
  console.log("Выбрана фамилия:", name);
  // Здесь можно обновить другие части панели под выбранного пользователя
});

// Обработка квартала
document.getElementById("quarterSelect").addEventListener("change", function () {
  const quarter = this.value;
  console.log("Выбран квартал:", quarter);
  // Здесь можно переключать данные по кварталам
});

document.getElementById("groupSelect").addEventListener("change", function () {
  const group = this.value;
  console.log("Выбрана группа:", group);
});


<!--    let currentIndex = -1;-->

<!--function filterDropdown() {-->
<!--    const input = document.getElementById("operator-name");-->
<!--    const filter = input.value.toLowerCase();-->
<!--    const dropdown = document.getElementById("dropdown");-->
<!--    const items = dropdown.getElementsByClassName("dropdown-item");-->

<!--    if (filter.length === 0) {-->
<!--        dropdown.style.display = "none";-->
<!--        return;-->
<!--    }-->

<!--    let anyVisible = false;-->
<!--    currentIndex = -1;-->

<!--    for (let i = 0; i < items.length; i++) {-->
<!--        const item = items[i];-->
<!--        const name = item.getAttribute("data-name").toLowerCase();-->

<!--        if (name.includes(filter) || name.startsWith(filter)) {-->
<!--            item.style.display = "block";-->
<!--            anyVisible = true;-->
<!--        } else {-->
<!--            item.style.display = "none";-->
<!--        }-->

<!--        item.style.backgroundColor = "";-->
<!--    }-->

<!--    dropdown.style.display = anyVisible ? "block" : "none";-->
<!--}-->

<!--function highlightItem(items) {-->
<!--    for (let i = 0; i < items.length; i++) {-->
<!--        const item = items[i];-->
<!--        if (i === currentIndex) {-->
<!--            item.style.backgroundColor = "#ddd";-->
<!--            item.scrollIntoView({ block: "nearest", behavior: "smooth" });-->
<!--        } else {-->
<!--            item.style.backgroundColor = "";-->
<!--        }-->
<!--    }-->
<!--}-->

<!--function handleKeyDown(event) {-->
<!--    const dropdown = document.getElementById("dropdown");-->
<!--    const items = Array.from(dropdown.getElementsByClassName("dropdown-item"))-->
<!--        .filter(item => item.style.display !== "none");-->

<!--    if (items.length === 0) return;-->

<!--    if (event.key === "ArrowDown") {-->
<!--        event.preventDefault();-->
<!--        if (currentIndex < items.length - 1) {-->
<!--            currentIndex++;-->
<!--            highlightItem(items);-->
<!--        }-->
<!--    } else if (event.key === "ArrowUp") {-->
<!--        event.preventDefault();-->
<!--        if (currentIndex > 0) {-->
<!--            currentIndex&#45;&#45;;-->
<!--            highlightItem(items);-->
<!--        }-->
<!--    } else if (event.key === "Enter") {-->
<!--        event.preventDefault();-->
<!--        if (currentIndex >= 0 && items[currentIndex]) {-->
<!--            const selectedName = items[currentIndex].getAttribute("data-name");-->
<!--            document.getElementById("operator-name").value = selectedName;-->
<!--            dropdown.style.display = "none";-->
<!--        }-->
<!--        document.getElementById("operator-form").submit(); // если форма должна отправляться-->
<!--    }-->
<!--}-->

<!--document.getElementById("operator-name").addEventListener("keydown", handleKeyDown);-->

<!--document.addEventListener("click", function(event) {-->
<!--    const input = document.getElementById("operator-name");-->
<!--    const dropdown = document.getElementById("dropdown");-->
<!--    if (!input.contains(event.target) && !dropdown.contains(event.target)) {-->
<!--        dropdown.style.display = "none";-->
<!--    }-->
<!--});-->

<!--document.querySelectorAll(".dropdown-item").forEach(item => {-->
<!--    item.addEventListener("click", function() {-->
<!--        const name = this.getAttribute("data-name");-->
<!--        document.getElementById("operator-name").value = name;-->
<!--        document.getElementById("dropdown").style.display = "none";-->
<!--        document.getElementById("operator-form").submit();-->
<!--    });-->
<!--});-->
const backgrounds = [
    "url('/static/img/ttt.jpg')",
    "url('/static/img/background.jpg')",
];

let bgIndex = 0;
let isCooldown = false;

window.addEventListener('load', () => {
    const savedBg = localStorage.getItem('backgroundImage');

    // Если ранее сохранённого фона нет — установить дефолтный (первый из списка)
    if (!savedBg) {
        const defaultBg = backgrounds[0];
        document.body.style.backgroundImage = defaultBg;
        localStorage.setItem('backgroundImage', defaultBg);
    } else {
        document.body.style.backgroundImage = savedBg;
    }

    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundPosition = "center";
});

document.getElementById('logo-img').addEventListener('click', () => {
    if (isCooldown) return;

    const newBg = backgrounds[bgIndex];
    document.body.style.backgroundImage = newBg;
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundPosition = "center";
    document.body.style.transition = "background-image 0.5s ease-in-out";

    localStorage.setItem('backgroundImage', newBg);
    bgIndex = (bgIndex + 1) % backgrounds.length;
});
    const ctx = document.getElementById('scoreChart').getContext('2d');
const score = parseFloat("{{ chart_score|default:0 }}");

let scoreColor = '';
if (score < 80) {
    scoreColor = '#ED2100';
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
            data: [score, 100 - score],
            backgroundColor: [scoreColor, '#1e293b'],
            borderColor: ['#ffffff', '#ffffff'],
            borderWidth: 1,
            spacing: 3
        }]
    },
    options: {
        cutout: '75%',
        responsive: false,
        plugins: {
            legend: { display: false },
            tooltip: { enabled: false }
        }
    }
});

  const monthLabels = {{ month_names|safe }};
  const donutConfig = {{ criteria_data|safe }};
  const monthlyData = {{ monthly_marks|safe }};

  function renderGrowthChart() {
    const ctx = document.getElementById("growthChart").getContext("2d");

    // Вычисляем среднее значение
    const sum = monthlyData.reduce((acc, val) => acc + val, 0);
    const avg = monthlyData.length ? sum / monthlyData.length : 0;

    new Chart(ctx, {
      type: "line",
      data: {
        labels: monthLabels,
        datasets: [
          {
            label: "Оценка",
            data: monthlyData,
            fill: true,
            tension: 0.4,
            borderColor: "#3b82f6",
            backgroundColor: "rgba(59,130,246,0.15)",
            pointBackgroundColor: "#fff",
            pointBorderColor: "#3b82f6",
            pointRadius: 5,
            pointHoverRadius: 7,
            pointStyle: "circle"
          },
          {
            label: "Средняя линия",
            data: Array(monthlyData.length).fill(avg),
            borderDash: [5, 5],
            borderColor: "#10b981", // зелёная линия
            pointRadius: 0,
            borderWidth: 1,
            fill: false
          }
        ]
      },
      options: {
        plugins: {
          legend: {
            display: true,
            labels: { color: "#ccc" }
          },
          tooltip: {
            enabled: true,
            backgroundColor: "rgba(0,0,0,0.7)",
            titleColor: "#ff3b3b",
            bodyColor: "#93c5fd",
            padding: 10,
            borderWidth: 1,
            borderColor: "#3b82f6"
          }
        },
        scales: {
          y: {
            min: 50,
            max: 95,
            ticks: { color: "#cbd5e1" },
            grid: { color: "rgba(255,255,255,0.05)", drawTicks: false }
          },
          x: {
            ticks: { color: "#e2e8f0" },
            grid: { display: false }
          }
        },
        animation: {
          onComplete: () => {
            // Добавим стрелку вручную на конец линии
            const chart = Chart.getChart("growthChart");
            const ctx = chart.ctx;
            const meta = chart.getDatasetMeta(0); // основная линия
            const lastPoint = meta.data[meta.data.length - 1];
            const prevPoint = meta.data[meta.data.length - 2];

            if (lastPoint && prevPoint) {
              ctx.save();
              ctx.fillStyle = lastPoint.y < prevPoint.y ? "limegreen" : "red";
              ctx.font = "bold 16px Arial";
              ctx.textAlign = "center";
              ctx.fillText(
                lastPoint.y < prevPoint.y ? "⬆" : "⬇",
                lastPoint.x,
                lastPoint.y - 10
              );
              ctx.restore();
            }
          }
        }
      }
    });
  }

  document.addEventListener('DOMContentLoaded', renderGrowthChart);

  // === Соотношение критериев ===
document.addEventListener('DOMContentLoaded', function () {
    const data = {{ quarter_penalties|safe }};
    const hasData = Array.isArray(data) && data.some(num => num > 0);

    const canvas = document.getElementById("ratioChart");
    const message = document.getElementById("noDataMessage");

    if (hasData) {
        new Chart(canvas, {
            type: 'pie',
            data: {
                labels: ['1-квартал', '2-квартал', '3-квартал', '4-квартал'],
                datasets: [{
                    label: 'Кол-во ошибок',
                    data: data,
                    backgroundColor: ['#00bcd4', '#2196f3', '#ff9800', '#8bc34a'],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'right',
                        labels: {
                            color: '#ffffff',
                            font: {
                                size: 12,
                                family: 'Arial'
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: Кол-во ошибок: ${context.raw}`;
                            }
                        }
                    }
                }
            }
        });
    } else {
        canvas.style.display = 'none';
        message.style.display = 'block';
    }
});


  // === Донаты по критериям ===
  const topGrid = document.getElementById("donutTop");
  const bottomGrid = document.getElementById("donutBottom");

  donutConfig.forEach((cfg, i) => {
    const total = cfg.data.reduce((a, b) => a + b, 0);
    const isAllZero = cfg.data.every(val => val === 0);

    const wrap = document.createElement("div");
    wrap.className = "indicator";
    wrap.innerHTML = `
      <h3>${cfg.title}</h3>
      <div style="position:relative; display:inline-block;">
        <canvas id="d${i}"></canvas>
        <div style="
          position:absolute;
          top:50%;
          left:50%;
          transform:translate(-50%,-50%);
          font-size:1.2rem;
          font-weight:bold;
          color:#f43f5e;">${total}</div>
      </div>
      <div class="months">
        <span data-count="${cfg.data[0]}">${monthLabels[0]}</span>
        <span data-count="${cfg.data[1]}">${monthLabels[1]}</span>
        <span data-count="${cfg.data[2]}">${monthLabels[2]}</span>
      </div>
    `;

    (i < 5 ? topGrid : bottomGrid).appendChild(wrap);

    new Chart(document.getElementById(`d${i}`), {
      type: "doughnut",
      data: {
        labels: monthLabels,
        datasets: [{
          data: isAllZero ? [1] : cfg.data,
          backgroundColor: isAllZero
            ? ["transparent"] //
            : ['#00bcd4',
        '#2196f3',
        '#ff9800',],
          cutout: "70%"
        }]
      },
      options: {
        plugins: { legend: { display: false }, tooltip: { enabled: false } },
        rotation: -0.5 * Math.PI
      }
    });
  });
  const comments = JSON.parse('{{ quarter_comments|escapejs }}');
  const commentsHtml = comments.map((c, i) => `
    <p><strong>${i + 1}) Месяц "${c.month_name}":</strong><hr> ${c.text}</p><br>
  `).join("");
  document.getElementById("commentsBox").innerHTML = commentsHtml;

  const mises = JSON.parse('{{ quarter_mises|escapejs }}');

  const counts = { severe: 0, major: 0, minor: 0 };

  mises.forEach(m => {
    if (counts[m.type] !== undefined) {
      counts[m.type]++;
    }
  });

  const legendItems = document.querySelectorAll(".legend-item");

  legendItems.forEach(item => {
    const label = item.querySelector(".label span.dot");
    if (label.classList.contains("severe")) {
      item.querySelector(".count").innerText = counts.severe;
    } else if (label.classList.contains("major")) {
      item.querySelector(".count").innerText = counts.major;
    } else if (label.classList.contains("minor")) {
      item.querySelector(".count").innerText = counts.minor;
    }
  });

      console.log("MONTH LABELS:", monthLabels);
      console.log("MONTHLY DATA:", monthlyData);
