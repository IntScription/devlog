document.addEventListener('DOMContentLoaded', function() {
  var el = document.getElementById('typed-welcome');
  if (!el) return;
  var text = "Welcome to my public developer log. I document my progress, projects, learning experiences, and reflections as I build and improve my skills in software engineering, AI, and development tools.";
  var i = 0;
  var speed = 32; // ms per character
  el.textContent = '';
  function type() {
    if (i < text.length) {
      el.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  type();
}); 