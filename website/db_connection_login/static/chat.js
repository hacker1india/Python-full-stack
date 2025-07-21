function sendMessage() {
    const inputField = document.getElementById("user-input");
    const message = inputField.value.trim();
    if (message === "") return;
  
    // Add user message to chat
    addMessage("user", message);
  
    // Get bot response
    const response = getBotResponse(message);
    setTimeout(() => addMessage("bot", response), 500); // Delay for realism
  
    inputField.value = "";
  }
  
  function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const messageEl = document.createElement("div");
    messageEl.className = sender === "user" ? "user-message" : "bot-message";
    messageEl.textContent = text;
    chatBox.appendChild(messageEl);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
  }
  
  function getBotResponse(message) {
    message = message.toLowerCase();
  
    if (message.includes("hello") || message.includes("hi")) {
      return "Hi there! 👋";
    } else if (message.includes("your name")) {
      return "I'm ChatBuddy, your simple web chatbot 🤖";
    } else if (message.includes("services")) {
      return "We offer web development, AI and design services.";
    } else if (message.includes("bye")) {
      return "Goodbye! Have a great day 😊";
    } else if (message.includes("how")) {
        return "I'm good, Thank You. What about you? 😊";
    } else {
      return "Sorry, I didn't understand that. Try asking something else!";
    }
  }
  