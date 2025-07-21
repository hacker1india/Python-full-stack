// let tasks = [];

// const input = document.getElementById("task-input");
// const list = document.getElementById("task-list");

// const rest = () => {
//   list.innerHTML = "";
//   tasks.forEach((task, i) => {
//     const li = document.createElement("li");

//     const text = document.createElement("span");
//     text.textContent = task.text;
//     if (task.done) text.classList.add("completed");
//     text.onclick = () => {
//       task.done = !task.done;
//       rest();
//     };

//     const del = document.createElement("button");
//     del.textContent = "✖️";
//     del.onclick = () => {
//       tasks.splice(i, 1);
//       rest();
//     };

//     li.append(text, del);
//     list.appendChild(li);
//   });
// };

// const addTask = () => {
//   if (input.value.trim()) {
//     tasks.push({ text: input.value.trim(), done: false });
//     input.value = "";
//     rest();
//   }
// };


function Addtask(){
  const btn = document.querySelector("#task-input")
  const addtext = btn.value.trim();

  if(addtext === "") return;
  const li = document.createElement("li")
  li.textContent=addtext;
  const delbtn=document.createElement("button")
  delbtn.textContent = addtext;
  delbtn.onclick = () => li.remove();

  li.appendChild(delbtn);
  document.querySelector("#task-list").appendChild(li)
  btn.value=""
}
