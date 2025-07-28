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

if (typeof PDF_URL !== 'undefined') {
  pdfjsLib.getDocument(PDF_URL).promise.then(pdf => {
    pdfDoc = pdf;
    renderAllPages(pdf);
  }).catch(error => {
    console.error("Ошибка при загрузке PDF:", error);
  });
}
