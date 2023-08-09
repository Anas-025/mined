const input = document.querySelector("#genre");
const list = document.querySelector("#genre-list");
const genreValue = document.querySelector("#genre-value");
const clear = document.querySelector(".clear");

console.log('static requestJS.js');
input.addEventListener("focus", () => {
  list.style.display = "block";
  clear.style.display = "block";
});

document.addEventListener("click", (e) => {
  if (e.target !== input && e.target !== list && e.target !== clear) {
    list.style.display = "none";
    clear.style.display = "none";
  }
});

clear.addEventListener("click", ()=>{
  input.value="";
  genreValue.setAttribute("data-value", "");
})

const listItems = Array.from(list.children[0].children);

listItems.map((item) => {
  console.log(item);
  item.addEventListener("click", () => {
    input.value = item.innerText;
    list.style.display = "none";
    const datavalue = item.getAttribute("data-value");
    genreValue.value = datavalue;
  });
});
