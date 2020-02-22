const replybtns=document.querySelectorAll('.replybtn')
const forms=document.querySelectorAll('.replyform')
forms.forEach(form=>{
    form.style.display='none'
    
})

replybtns.forEach(btn =>{

    btn.addEventListener('click',function(e)
    {
        e.preventDefault();
        let form=btn.parentElement.querySelector(".replyform");
         
        form.classList.toggle("myactive")
        if (form.style.display=='block')
            form.style.display='none'
        else
            form.style.display='block'  
    })
    // console.log(btn.parentElement);
   
    // console.log(form);

})
// console.log(replybtn,replyform)
