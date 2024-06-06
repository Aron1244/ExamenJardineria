function iniciarSesion(event) {
  event.preventDefault();

  const usuario = document.getElementById("inputUsuario").value;
  const contra = document.getElementById("inputContra").value;

  const superUsuario = "admin";
  const superContra = "admin123";

  if (usuario === superUsuario && contra === superContra) {
    alert("Inicio de sesión exitoso!");
    setTimeout(function () {
      window.location.href = "admin.html";
    }, 500);
  } else {
    alert("Usuario o contraseña incorrectos. Inténtelo de nuevo.");
  }

  return false;
}
