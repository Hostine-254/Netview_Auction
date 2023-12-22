function copyMenu(){
    var dpCategory = document.querySelector('.dpt-cat');
    var dptPlace = document.querySelector('.departments');
    dptPlace.innerHTML = dpCategory.innerHTML;

    //copy inside nav to nav
    var mainNav = document.querySelector('.header-nav nav');
    var navPlace = document.querySelector('.off-canvas nav');
    navPlace.innerHTML = mainNav.innerHTML;

    //copy .header-top .wrapper to .thetop-nav
    var topNav = document.querySelector('.header-top .wrapper');
    var topPlace = document.querySelector('.off-canvas .thetop-nav');
    topPlace.innerHTML = topNav.innerHTML;
}
copyMenu();

//show mobile menu
const menuButton = document.querySelector('.trigger'),
      closeButton = document.querySelector('.t-close'),
      addclass = document.querySelector('.site');
menuButton.addEventListener('click', function(){
    addclass.classList.toggle('showmenu')
})
closeButton.addEventListener('click', function(){
    addclass.classList.remove('showmenu')
})


//Show submenu on mobile
const submenu = document.querySelectorAll('.has-child .icon-small');
submenu.forEach((menu) => menu.addEventListener('click',toggle));

function toggle(e){
    e.preventDefault();
    submenu.forEach((item) => item != this ? item.closest('.has-child').classList.remove('expand') : null);
    if (this.closest('.has-child').classList != 'expand');
    this.closest('.has-child').classList.toggle('expand');
}

//slider
const swiper = new Swiper('.swiper', {
    loop: true,
    autoplay:{
        delay:4020,
        disableOnInteraction:false,
    },
    //if pagination is required
    pagination: {
        el: '.swiper-pagination'
    }
  });

//show dpt menu

const dptButton = document.querySelector('.dpt-cat .dpt-trigger'),
      dptClass = document.querySelector('.site');
dptButton.addEventListener('click', function(){
    dptClass.classList.toggle('showdpt')
});

//show search

const searchButton = document.querySelector('.t-search'),
      tClose = document.querySelector('.search-close'),
      showClass = document.querySelector('.search-bottom');
searchButton.addEventListener('click', function(){
    showClass.classList.toggle('showsearch');

    if(showClass.classList.contains('showsearch')){
        console.log("contains search")
        showClass.classList.add('showsearch');
        tClose.addEventListener('click', function(){
            showClass.classList.remove('showsearch');
        })
    }
    else{
        console.log("does not contain that")
        showClass.classList.remove('showsearch');
    }
    
});

const realImageBtn = document.querySelector('#img-pt')
const customBtn = document.querySelector('.custom-btn')
const customtxt = document.querySelector('.custom-text')

realImageBtn.addEventListener("change", function(){
    if (realImageBtn.value){
      customtxt.innerHTML = realImageBtn.value; 
    }
    else {
        customtxt.innerHTML = "No image choosen..";
    }
})

const realImageBtn1 = document.querySelector('#img-pt1')
const customtxt1 = document.querySelector('.cust-txt1')

realImageBtn1.addEventListener("change", function(){
    if (realImageBtn1.value){
      customtxt1.innerHTML = realImageBtn1.value; 
    }
    else {
        customtxt1.innerHTML = "No image choosen..";
    }
})

const realImageBtn2 = document.querySelector('#img-pt2')
const customtxt2 = document.querySelector('.cust-txt2')

realImageBtn2.addEventListener("change", function(){
    if (realImageBtn2.value){
      customtxt2.innerHTML = realImageBtn2.value; 
    }
    else {
        customtxt2.innerHTML = "No image choosen..";
    }
})

const realImageBtn3 = document.querySelector('#img-pt3')
const customtxt3 = document.querySelector('.cust-txt3')

realImageBtn3.addEventListener("change", function(){
    if (realImageBtn3.value){
      customtxt3.innerHTML = realImageBtn3.value; 
    }
    else {
        customtxt3.innerHTML = "No image choosen..";
    }
})

const realImageBtn4 = document.querySelector('#img-pt4')
const customtxt4 = document.querySelector('.cust-txt4')

realImageBtn4.addEventListener("change", function(){
    if (realImageBtn4.value){
      customtxt4.innerHTML = realImageBtn4.value; 
    }
    else {
        customtxt4.innerHTML = "No image choosen..";
    }
})


