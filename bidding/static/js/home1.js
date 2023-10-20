const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const dropDownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick = function (){
    dropDownMenu.classList.toggle('open')
    const isOpen = dropDownMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen
    ? 'fa-solid fa-xmark'
    : 'fa-solid fa-bars'
}

var lastScrollTop = 0;
    navbar = document.getElementById("header");

window.onscroll = function(){
    if(window.pageYOffset >= navbar.offsetTop){
        navbar.classList.add("sticky");
    }
    else{
        navbar.classList.remove("sticky");
    }
}

const divlist = document.querySelectorAll('#product2 .pro-container');
const nxtbtn = document.querySelectorAll('#next-slide');
const prevbtn = document.querySelectorAll('#prev-slide');

divlist.forEach((item, i) => {
    let containerDim = item.getBoundingClientRect();
    let containerWid = containerDim.width;

    nxtbtn[i].addEventListener('click', () => {
        console.log(item)
        item.scrollLeft += containerWid;
    })

    prevbtn[i].addEventListener('click', () => {
        console.log("clicked")
        item.scrollLeft -= containerWid;
    })
})
