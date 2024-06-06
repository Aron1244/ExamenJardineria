function loadCart() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const cartItemsContainer = document.getElementById("cart-items");
  cartItemsContainer.innerHTML = "";

  let subtotal = 0;

  cart.forEach((item) => {
    const totalItemPrice = item.price * item.quantity;
    subtotal += totalItemPrice;

    const itemElement = document.createElement("div");
    itemElement.classList.add("row", "align-items-start");
    itemElement.innerHTML = `
        <div class="col-md-8 col-lg-3" style="text-align: left">
          <img src="${item.image}" style="width: 10vh" alt="" />
        </div>
        <div class="col-md-2" style="text-align: center">
          <div class="row" style="text-align: center">${item.title}</div>
          <div class="row" style="text-align: center">${item.author}</div>
          <div class="row" style="text-align: center">
            <button class="btn btn-danger" onclick="removeItem('${item.isbn}')">Eliminar</button>
          </div>
        </div>
        <div class="col-md-2 col-lg-2" style="margin-left: 100px">
          <div class="row justify-content-center align-items-center">
            <button class="btn btn-secondary" style="width: 30px;" onclick="decrementQuantity('${item.isbn}')">-</button>
            <div>${item.quantity}</div>
            <button class="btn btn-secondary" style="width: 30px;" onclick="incrementQuantity('${item.isbn}')">+</button>
          </div>
        </div>
        <div class="col-md-2 col-lg-3">${formatCurrency(item.price)}</div>
        <div class="col">${formatCurrency(totalItemPrice)}</div>
      `;
    cartItemsContainer.appendChild(itemElement);
  });

  // Update subtotal
  document.getElementById("subtotal").textContent = formatCurrency(subtotal);
  // Calculate shipping
  const shippingCost = calculateShipping(subtotal);
  document.getElementById("envio").textContent = formatCurrency(shippingCost);
  // Update total
  const total = subtotal + shippingCost;
  document.getElementById("total").textContent = formatCurrency(total);
}

function formatCurrency(value) {
  return `$${value.toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`;
}

function calculateShipping(subtotal) {
  return 0; // Aquí puedes agregar tu lógica para calcular el envío si es necesario
}

function removeItem(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart = cart.filter((item) => item.isbn !== itemId);
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();
}

function decrementQuantity(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const updatedCart = cart.map((item) => {
    if (item.isbn === itemId && item.quantity > 1) {
      item.quantity -= 1;
    }
    return item;
  });
  localStorage.setItem("cart", JSON.stringify(updatedCart));
  loadCart();
}

function incrementQuantity(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const updatedCart = cart.map((item) => {
    if (item.isbn === itemId) {
      item.quantity += 1;
    }
    return item;
  });
  localStorage.setItem("cart", JSON.stringify(updatedCart));
  loadCart();
}

window.onload = function () {
  loadCart();
};

function pagar() {
  localStorage.removeItem("cart");
  location.reload();
}

function applyCoupon() {
  const cuponInput = document.getElementById("cuponInput").value;
  let total = parseFloat(document.getElementById("total").textContent.replace(/[$.]/g, '').replace(',', '.'));

  switch (cuponInput) {
    case "Primera-Compra":
      total *= 0.8; // Aplica un descuento del 20%
      break;
    case "50-descuento":
      total *= 0.5; // Aplica un descuento del 50%
      break;
    default:
      alert("Cupón no válido");
      return;
  }

  // Actualiza el total en el carrito
  document.getElementById("total").textContent = formatCurrency(total);
  alert(`Cupón "${cuponInput}" aplicado correctamente`);
}
