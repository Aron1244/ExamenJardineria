function toggleTheme() {
  const content = document.getElementById("contenido");
  const footer = document.getElementById("footer");
  const navbar = document.getElementById("navbar");
  if (content.classList.contains("dark-mode")) {
    setLightMode(content, footer, navbar);
    localStorage.setItem("theme", "light");
  } else {
    setDarkMode(content, footer, navbar);
    localStorage.setItem("theme", "dark");
  }
}

function setLightMode(content, footer, navbar) {
  content.classList.remove("dark-mode");
  content.classList.add("light-mode");

  footer.classList.remove("dark-mode-footer");
  footer.classList.add("light-mode-footer");

  navbar.classList.remove("dark-mode-footer");
  navbar.classList.add("light-mode-footer");
  navbar.classList.add("navbar-dark");
}

function setDarkMode(content, footer, navbar) {
  content.classList.remove("light-mode");
  content.classList.add("dark-mode");

  footer.classList.remove("light-mode-footer");
  footer.classList.add("dark-mode-footer");

  navbar.classList.remove("light-mode-footer");
  navbar.classList.add("dark-mode-footer");
  navbar.classList.add("navbar-dark");
}

function applySavedTheme() {
  const savedTheme = localStorage.getItem("theme");
  const content = document.getElementById("contenido");
  const footer = document.getElementById("footer");
  const navbar = document.getElementById("navbar");

  if (savedTheme === "dark") {
    setDarkMode(content, footer, navbar);
  } else {
    setLightMode(content, footer, navbar);
  }
}

document.addEventListener("DOMContentLoaded", applySavedTheme);
