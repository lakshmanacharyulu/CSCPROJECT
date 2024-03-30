const shortBtn=document.getElementById('short-btn') ;
const reloadBtn= document.getElementById('reload-btn') ;

shortBtn. addEventListener('click' ,() =>{
const longUrl = document. getElementById('longUrl').value;
const apiUrl=`https://tinyurl.com/api-create.php?url=${encodeURIComponent(longUrl)}`;
const shortUrlTextarea=document.getElementById("shortUrl");

fetch(apiUrl)
.then(response =>response.text())
.then(data=>shortUrlTextarea.value=data)
.catch(error =>shortUrlTextarea.value="Error:Unable to shorten Url");

});

reloadBtn.addEventListener("click",() =>location.reload());