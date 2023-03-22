const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const images = ['berserk1.jpg', 'Guts.jpg', 'berserk2.jpg', 'Jungle.jpg', 'mobangry.jpg'];

/* Declaring the alternative text for each image file */
//Declare a const object listing the alternative text for each image
const altText = {
    '100.jpg': 'A picture of a red flower',
    'Guts.jpg': 'A picture of a blue flower',
    'Donkey.jpg': 'A picture of a yellow flower',
    'Jungle.jpg': 'A picture of a purple flower',
    'mob.jpg': 'A picture of a green flower'
};
/* Looping through images */
//Loop through the array of filenames, and for each one, insert an <img> element inside the thumb-bar <div> that embeds that image in the page along with its alternative text
for (let i = 0; i < images.length; i++) {
    const newImage = document.createElement('img');
    newImage.setAttribute('src', 'images/' + images[i]);
    newImage.setAttribute('alt', altText[images[i]]);
    thumbBar.appendChild(newImage);
    newImage.addEventListener('click', e => {
        displayedImage.src = e.target.src;
        displayedImage.alt = e.target.alt;
    });
}

/* Wiring up the Darken/Lighten button */
//Darken lighten button
btn.addEventListener('click', () => {
    const btnClass = btn.getAttribute('class');
    if (btnClass === 'dark') {
        btn.setAttribute('class', 'light');
        btn.textContent = 'Lighten';
        overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
    } 
    else {    
        btn.setAttribute('class', 'dark');
        btn.textContent = 'Darken';
        overlay.style.backgroundColor = 'rgba(0,0,0,0)';
    }
});

const newImage = document.createElement('img');
newImage.setAttribute('src', xxx);
newImage.setAttribute('alt', xxx);
thumbBar.appendChild(newImage);