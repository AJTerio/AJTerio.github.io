const button = document.querySelector('#js-new-quote');
button.addEventListener('click', getQuote);

//const answerButton = document.querySelector('#js-tweet');
//answerButton.addEventListener('click', showAnswer);

const endpoint = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random';
//const endpoint = 'https://trivia.cyberwisp.com/getrandomchristmasquestion';


async function getQuote() {
    //console.log("it works");
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw Error(response.statusText);
        }
        const json = await response.json();
        //console.log(json.message);
        displayQuote(json.message);
    }
    catch (err) {
        console.log(err);
        alert("Sorry, there was a problem getting a quote. Please try again later.");
    }
}

function displayQuote(quote) {
    const quoteText = document.querySelector('#js-quote-text');
    quoteText.textContent = quote;
}

//function showAnswer(quote) {
    //const answerText = document.querySelector('#js-answer-text');
    //answerText.textContent = quote;
//}

getQuote();