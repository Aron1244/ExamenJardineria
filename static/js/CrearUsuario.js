$(document).ready(function () {
  $("#Sign_Usuario").submit(function (event) {
    event.preventDefault();

    var nombre = $("#inputNombre").val();
    var apellido = $("#inputApellido").val();
    //var fecha = $("#inputNac").val();
    var direccion = $("#inputDireccion").val();
    var usuario = $("#inputUsuario").val();
    var email = $("#exampleInputEmail1").val();
    var contraseña = $("#exampleInputPassword1").val();
    var check = $("#exampleCheck1").is(":checked");
    var fecha = $("#inputNac").val();

    if (nombre.length < 3 || nombre.length > 15) {
      alert("El nombre deben tener entre 3 y un máximo de 15 caracteres.");
      return;
    }
    if (apellido.length < 3 || apellido.length > 20) {
      alert("El Apellido deben tener entre 3 y un máximo 20 caracteres.");
      return;
    }

    if (fecha === "") {
      alert("Por favor, ingresa una fecha.");
      return;
    }

    if (usuario.length < 5 || usuario.length > 15) {
      alert("Nombre de Usuario Invalido ");
      return;
    }
    if (direccion.length < 10 || direccion.length > 20) {
      alert("debe escribir la Dirección Completa");
      return;
    }

    if (email.length < 2 || email.length > 15) {
      alert("Correo invalido");
      return;
    }

    if (contraseña.length == "" || contraseña.length < 5) {
      alert("Tamaño de contraseña muy corta ");
      return;
    }
    if (!check) {
      alert("Debe aceptar los termino y condiciones: ");
      return;
    }

    alert("¡Usuario Creado!");
    window.location.href = "index.html";
  });
});
