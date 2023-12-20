const chatbotContainer = document.querySelector(".chatbot-container");
const chatbotHeaderClose = document.querySelector(".chatbot-header-close");
const chatbotInput = document.querySelector("#chatbot-input");
const chatbotSend = document.querySelector("#chatbot-send");
const chatbotBodyContentWrapper = document.querySelector(".chatbot-body-content-wrapper");

chatbotHeaderClose.addEventListener("click", () => {
    chatbotContainer.classList.toggle("active");
});

chatbotInput.addEventListener("keyup", (event) => {
    if (event.keyCode === 13) {
        chatbotSend.click();
    }
});

function addMessage(message) {
    let html = `
        <div class="chatbot-body-content-wrapper-message">
            <div class="chatbot-body-content-wrapper-message-text">
                <p>${message}</p>
            </div>
        </div>
    `;
    chatbotBodyContentWrapper.innerHTML += html;
    chatbotBodyContentWrapper.scrollTop = chatbotBodyContentWrapper.scrollHeight;
}

chatbotSend.addEventListener("click", () => {
    let message = chatbotInput.value;
    if (message) {
        chatbotInput.value = "";
        addMessage(message);
        fetch(`/api/get_reply?message=${message}`)
            .then((response) => response.json())
            .then((data) => {
                addMessage(data["message"]);
            });
    }
});

