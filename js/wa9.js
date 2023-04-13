const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array){
const random = Math.floor(Math.random()*array.length);
return array[random];
}

//Store the first, big long, string of text inside a variable called storyText
let storyText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.';
//Store the first set of three strings inside an array called insertX
let insertX = ['Chip Oatlay', 'Steve the tree', 'Richard Enbals'];
//Store the second set of three strings inside an array called insertY
let insertY = ['bovas', 'DK Summmit', 'Axels room'];
//Store the third set of three strings inside an array called insertZ
let insertZ = ['played the mountain', 'talked to drunk Navan', 'turned into a bee and crawled into my head'];


randomize.addEventListener('click', result);

    function result() {
      var newStory = storyText;
      var xItem = randomValueFromArray(insertX);
      var yItem = randomValueFromArray(insertY);
      var zItem = randomValueFromArray(insertZ);

      var newStory = newStory.replaceAll(':insertx:', xItem);
      var newStory = newStory.replaceAll(':inserty:', yItem);
      var newStory = newStory.replaceAll(':insertz:', zItem);
    
      if(customName.value !== '') {
        const name = customName.value;
        newStory = newStory.replaceAll('Bob', name);
      }
    
      if(document.getElementById("uk").checked) {
        const weight = Math.round(300/14) + ' stone';
        const temperature =  Math.round((94-32)*(5/9)) + ' centrigrade';
        newStory = newStory.replaceAll('94 fahrenheit', temperature);
        newStory = newStory.replaceAll('300 pounds', weight);
      }
    
      story.textContent = newStory;
      story.style.visibility = 'visible';
    }