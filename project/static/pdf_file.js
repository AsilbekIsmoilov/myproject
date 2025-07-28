let pdfDoc = null;
let pageNum = 1;
let scale = 1.5;
const container = document.getElementById('pdf-container');

// Очистка и отрисовка одной страницы
function renderPage(num) {
  container.innerHTML = "";

  pdfDoc.getPage(num).then(page => {
    const viewport = page.getViewport({ scale });
    const canvas = document.createElement('canvas');
    canvas.id = `page-${num}`;
    canvas.classList.add('pdf-page');
    canvas.height = viewport.height;
    canvas.width = viewport.width;
    canvas.style.margin = "10px auto";
    canvas.style.display = "block";

    const context = canvas.getContext('2d');
    const renderContext = {
      canvasContext: context,
      viewport: viewport
    };

    // Добавляем в DOM и рендерим
    container.appendChild(canvas);
    page.render(renderContext).promise.then(() => {
      updatePageCounter();
    });

    // Обработчик двойного клика — выделение canvas (имитация строки)
    canvas.ondblclick = function () {
      document.querySelectorAll('.pdf-page').forEach(el => {
        el.classList.remove('highlighted');
      });
      canvas.classList.add('highlighted');
    };
  });
}

// Загрузка PDF-файла
function loadPDF(url) {
  pdfjsLib.getDocument(url).promise.then(pdf => {
    pdfDoc = pdf;
    pageNum = 1;
    renderPage(pageNum);
  }).catch(error => {
    console.error("Ошибка при загрузке PDF:", error);
    container.innerHTML = "<p style='text-align:center; color:gray;'>Ошибка загрузки PDF</p>";
  });
}

// Обновление счётчика
function updatePageCounter() {
  let infoBlock = document.getElementById('pdf-page-info');
  if (!infoBlock) {
    infoBlock = document.createElement('div');
    infoBlock.id = 'pdf-page-info';
    infoBlock.style.textAlign = 'center';
    infoBlock.style.margin = '5px';
    container.parentNode.insertBefore(infoBlock, container);
  }
  infoBlock.innerHTML = `Страница ${pageNum} из ${pdfDoc.numPages}`;
}

// Кнопки управления
function nextPage() {
  if (pageNum < pdfDoc.numPages) {
    pageNum++;
    renderPage(pageNum);
  }
}

function prevPage() {
  if (pageNum > 1) {
    pageNum--;
    renderPage(pageNum);
  }
}

function zoomIn() {
  scale += 0.2;
  renderPage(pageNum);
}

function zoomOut() {
  if (scale > 0.6) {
    scale -= 0.2;
    renderPage(pageNum);
  }
}

// Обработчик при загрузке
function showPdf(code, clickedBtn = null) {
  const url = pdfFiles[code];
  if (url) {
    loadPDF(url);
  } else {
    container.innerHTML = "<p style='text-align:center; color:gray;'>PDF файл не найден</p>";
  }

  document.querySelectorAll('.pdf-button').forEach(btn => {
    btn.classList.remove('active');
  });

  if (clickedBtn) {
    clickedBtn.classList.add('active');
  }
}

window.addEventListener('load', () => {
  const defaultBtn = document.querySelector('.pdf-button');
  if (defaultBtn) {
    defaultBtn.click();
  }
});
