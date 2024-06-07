document.addEventListener("DOMContentLoaded", () => {
  const searchBar = document.getElementById("searchBar");
  const books = document.querySelectorAll(".card");

  searchBar.addEventListener("keyup", (e) => {
    const searchString = e.target.value.toLowerCase();

    books.forEach((book) => {
      const title = book.querySelector(".card-title").textContent.toLowerCase();
      if (title.includes(searchString)) {
        book.style.display = "block";
      } else {
        book.style.display = "none";
      }
    });
  });
});
