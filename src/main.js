fetch('src/components/BillNoteSheet.html')
  .then(response => response.text())
  .then(html => document.getElementById('app').innerHTML = html);