function getBotResponse(input) {
  const chatbotResUrl = "https://free-frindly-chat-bot.vercel.app/ask";
  $.ajax({
      type: "POST",
      url: chatbotResUrl,
      contentType: "application/json",
      data: JSON.stringify({ message: input }),
      success: function (data) {
          let botHtml = '<p class="botText"><span>' + data.response + '</span></p>';
          $("#chatbox").append(botHtml);
          console.log(data.response);

          // Re-attach event listener for newly added elements
          attachClickListener();
      },
      error: function (data) {
          console.log(data);
      },
  });
}

function attachClickListener() {
  let botTextElements = document.querySelectorAll('.botText');

  // Loop through each element and attach a click event listener
  botTextElements.forEach(function (element) {
      element.removeEventListener('click', copyTextToClipboard);
      element.addEventListener('click', copyTextToClipboard);
  });
}

function copyTextToClipboard(event) {
  // Get the text content of the clicked p tag
  let text = this.querySelector('span').textContent;
  // Copy the text to clipboard
  navigator.clipboard.writeText(text)
      .then(function() {
          // Alert the user that the text has been copied
          alert("Copied to clipboard: " + text);
      })
      .catch(function(error) {
          console.error('Failed to copy text: ', error);
      });
}

// Initial call to attach event listeners
attachClickListener();
