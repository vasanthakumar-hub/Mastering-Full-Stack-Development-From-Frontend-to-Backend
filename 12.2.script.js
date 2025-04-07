/* document.addEventListener('DOMContentLoaded',()=>{ */ /* It is Not Needed In External Javascript */
function createParagraph(){
    const para = document.createElement('p');
    para.textContent = 'You Clicked to Create Paragraph!';
    document.body.appendChild(para);
}
const buttons = document.querySelectorAll('button')

for(const button of buttons){
    button.addEventListener('click',createParagraph)
}
/* }) */