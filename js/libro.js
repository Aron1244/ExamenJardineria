function addToCart(book) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  let existingBook = cart.find((item) => item.isbn === book.isbn);
  if (existingBook) {
    existingBook.quantity += 1;
  } else {
    book.quantity = 1;
    cart.push(book);
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  window.location.href = "catalogo.html";
}
