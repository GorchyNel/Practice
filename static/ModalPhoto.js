var images = document.getElementsByClassName('ModalImage');
var modal = document.getElementById('Modal');
var modalImg = document.getElementById('img01');
var captionText = document.getElementById('caption');


//Вешаем обработчик нажатия на каждую фотку
for(let i=0; i<images.length; i++)
{
    images[i].onclick = function (){
    console.log("Зашел");
    modal.style.display = 'block';
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
    }
}


var span = document.getElementsByClassName('close')[0];

span.onclick = function () {
    modal.style.display = "none";
}