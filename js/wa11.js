const button = document.querySelector('#js-new-quote');
button.addEventListener('click', getImage);

const endpoint = 'https://api.catboys.com/img';

async function getImage() {
    console.log("it works");
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw Error(response.statusText);
        }
        const json = await response.json();
        //console.log(json.message);
        displayImage(json.url);
    }
    catch (err) {
        console.log(err);
        alert("Sorry, there was a problem generating a cat. Please try again later.");
    }
}

function displayImage(image) {
    //const quoteText = document.querySelector('#js-quote-text');
    //quoteText.textContent = quote;
    console.log(image);

    var img = document.createElement('img');
    img.src = image;
    document.getElementById('body').appendChild(img);
}
