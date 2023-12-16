/*video ka js */
var myVideo = document.getElementById("trim");
myVideo.playbackRate = 2.5;

const phrases = ["Vruksha Vista", "वृक्ष विस्टा"];
let currentPhraseIndex = 0;
let currentCharIndex = 0;
const typingContainer = document.getElementById("typeing");

function type() {
  if (typingContainer) {
    if (currentCharIndex < phrases[currentPhraseIndex].length) {
      typingContainer.textContent +=
        phrases[currentPhraseIndex].charAt(currentCharIndex);
      currentCharIndex++;
      setTimeout(type, 200); // Adjust typing speed (milliseconds)
    } else {
      setTimeout(erase, 1500); // Wait before starting to erase
    }
  }
}

function erase() {
  if (typingContainer) {
    if (currentCharIndex > 0) {
      typingContainer.textContent = phrases[currentPhraseIndex].substring(
        0,
        currentCharIndex - 1
      );
      currentCharIndex--;
      setTimeout(erase, 200); // Adjust erasing speed (milliseconds)
    } else {
      currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
      setTimeout(type, 500); // Wait before typing the next phrase
    }
  }
}

setTimeout(type, 500);

document.getElementById("explore").addEventListener("click", () => {
  document.getElementById("login").style.display = "block";
  document.getElementById("text-explore").style.display = "none";
});

document.getElementById("close-button").addEventListener("click", () => {
  document.getElementById("login").style.display = "none";
  document.getElementById("text-explore").style.display = "block";
});
