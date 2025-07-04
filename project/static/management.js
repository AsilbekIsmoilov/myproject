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

if (typeof PDF_URL !== 'undefined') {
  pdfjsLib.getDocument(PDF_URL).promise.then(pdf => {
    pdfDoc = pdf;
    renderAllPages(pdf);
  }).catch(error => {
    console.error("Ошибка при загрузке PDF:", error);
  });
}
  function showPdf(url, button) {
  document.querySelectorAll('.pdf-button').forEach(btn => btn.classList.remove('active'));
  button.classList.add('active');

  const container = document.getElementById("pdf-container");
  container.innerHTML = '';

  const loadingTask = pdfjsLib.getDocument(url);
  loadingTask.promise.then(pdf => {
    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      pdf.getPage(pageNum).then(page => {
        const canvas = document.createElement("canvas");
        container.appendChild(canvas);

        const viewport = page.getViewport({ scale: 1.5 });
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        page.render({ canvasContext: canvas.getContext("2d"), viewport });
      });
    }
  });
}

if (DEFAULT_PDF_URL) {
  showPdf(DEFAULT_PDF_URL, document.querySelector('.pdf-button'));
}
