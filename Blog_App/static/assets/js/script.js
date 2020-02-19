let sidebarItems= document.querySelectorAll('.sidebar-wrapper ul li')


sidebarItems.forEach(item => {
    console.log(item);
    item.addEventListener('click',function(){
        sidebarItems.forEach(item=>{
            item.classList.remove('active')
        })
        item.classList.add('active')
        
        
    })
})