let img = document.getElementById('gallery');
let id;
id=setInterval(slide,4995);
function slide(){
    if(img.src.slice(24)=="/static/checklist.png"){
        img.src="/static/woman_with_list.png";
    }
    else{
    if(img.src.slice(24)=="/static/woman_with_list.png"){
        img.src="/static/man_with_list.png";
    }
    else{
        img.src="/static/checklist.png"
    }
}
}
