$(document).ready(function () {
  $("#Forma_contacto").submit(function (event) {
    event.preventDefault();

    var nombre = $("#inputNombre").val();
    var apellido = $("#inputApellido").val();
    var email = $("#exampleInputEmail1").val();
    let rut = $("#inputRut").val();
    let telefono = $("#inputTelefono").val();
    let Empresa_Fono = $("#inputEmpresa").val();
    let Validacion_numerica = /^\d+$/.test(Empresa_Fono);
    let onlyNumber = /^\d+$/.test(telefono);

    if (email.length < 2 || email.length > 15) {
      alert("Correo invalido");
      return;
    }

    if (rut.length < 5 || rut.length > 12) {
      alert("rut invalido");
      return;
    }

    if (nombre.length < 3 || nombre.length > 15) {
      alert("El nombre deben tener entre 3 y un máximo de 15 caracteres.");
      return;
    }

    if (apellido.length < 3 || apellido.length > 20) {
      alert("El Apellido deben tener entre 3 y un máximo 20 caracteres.");
      return;
    }

    if (telefono.length < 9 || telefono.length > 13) {
      alert("teléfono invalido");
      return;
    } else if (!onlyNumber) {
      alert("El teléfono solo debe contener valores numéricos");
    }

    if (Empresa_Fono.length < 9 || Empresa_Fono.length > 13) {
      alert("telefono Debe tener al menos 9 números");
      return;
    } else if (!Validacion_numerica) {
      alert("El teléfono solo debe contener números.");
      return;
    }

    alert("Formulario Enviado Con Éxito");
    window.location.href = "index.html";
    //  location.reload();
  });
});
