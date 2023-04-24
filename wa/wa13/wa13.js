// check function
function check() {
    console.log('test');
}

// submit function
function submit() {
    alert('Woaahhh ur volume is now ' + output.textContent + '! Great job?');
}

// reset function
function reset() {
    outputInt = 0;
    output.textContent = outputInt;
}

// minus function
function minus() {
    if (outputInt > 0) {
    outputInt -=1;
    output.textContent = outputInt; 
    }
}

// plus function
function plus() {
    if (outputInt < 100) {
    outputInt +=1;
    output.textContent = outputInt;
    }
}

// random function 0-100
function random() {
    outputInt = randomNumber(0, 100);
    output.textContent = outputInt;
}

// random function custom
function randomNumber(min, max) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    return num;
  }

// // output
// const output = document.querySelector('.output');
// let outputInt = parseInt(output.textContent);
// console.log(outputInt);

//count instantiation
let clicks = 0;

// mash function
function mash() {
    console.log("mash");
    if(clicks == 0) {
        setTimeout(ending, 5000);
    }
    clicks++;
}

// ending function
function ending() {
    console.log("ending");
    clickCount.textContent = clicks.toString();
    clicks = 0;
}


// buttons
// const minusButton = document.querySelector('.minus-button').addEventListener('click', minus);
// const plusButton = document.querySelector('.plus-button').addEventListener('click', plus);
// const resetButton = document.querySelector('.reset-button').addEventListener('click', reset);
// const randomButton = document.querySelector('.random-button').addEventListener('click', random);
// const submitButton = document.querySelector('.submit-button').addEventListener('click', submit);
const mashButton = document.querySelector('.mash-button').addEventListener('click', mash);