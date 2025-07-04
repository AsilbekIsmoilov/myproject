let pdfDoc = null;
let scale = 2;
const container = document.getElementById('pdf-container');

function renderAllPages(pdf) {
  for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
    pdf.getPage(pageNum).then(page => {
      const viewport = page.getViewport({ scale });

      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      canvas.height = viewport.height;
      canvas.width = viewport.width;
      canvas.style.marginBottom = "20px";

      container.appendChild(canvas);

      const renderContext = {
        canvasContext: context,
        viewport: viewport
      };
      page.render(renderContext);
    });
  }
}

function reloadPages() {
  container.innerHTML = "";
  renderAllPages(pdfDoc);
}

function loadPDF(url) {
  container.innerHTML = "";
  pdfjsLib.getDocument(url).promise.then(pdf => {
    pdfDoc = pdf;
    renderAllPages(pdf);
  }).catch(error => {
    console.error("Ошибка при загрузке PDF:", error);
    container.innerHTML = "<p style='text-align:center; color:gray;'>Ошибка загрузки PDF</p>";
  });
}

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
