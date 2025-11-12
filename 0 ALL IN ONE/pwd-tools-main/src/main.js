<<<<<<< HEAD
fetch('src/components/BillNoteSheet.html')
  .then(response => response.text())
=======
fetch('src/components/BillNoteSheet.html')
  .then(response => response.text())
>>>>>>> 888881a (Your commit message here)
  .then(html => document.getElementById('app').innerHTML = html);