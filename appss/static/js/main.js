/*===== GOOGLE FONTS =====*/
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

/*===== VARIABLES CSS =====*/
:root {
  --header-height: 3rem;

  /*========== Colors ==========*/
  --first-color: #DA2535;
  --first-color-alt: #C42130;
  --first-color-send: #DE3B49;
  --title-color: #161212;
  --text-color: #5B5757;
  --text-color-light: #8F8A8A;
  --body-color: #FEFBFB;
  --container-color: #FFF;

  /*========== Font and typography ==========*/
  --body-font: 'Poppins', sans-serif;
  --biggest-font-size: 2rem;
  --h2-font-size: 1.25rem;
  --h3-font-size: 1.125rem;
  --normal-font-size: .938rem;
  --small-font-size: .813rem;

  /*========== Font weight ==========*/
  --font-semi-bold: 600;
  --font-bold: 700;

  /*========== Margenes ==========*/
  --mb-1: .5rem;
  --mb-2: 1rem;
  --mb-3: 1.5rem;
  --mb-4: 2rem;
  --mb-5: 2.5rem;
  --mb-6: 3rem;
  /*========== z index ==========*/

  --z-tooltip: 10;
  --z-fixed: 100;
}

@media screen and (min-width: 968px){
  :root{
    --biggest-font-size: 3rem;
    --h2-font-size: 1.75rem;
    --h3-font-size: 1.25rem;
    --normal-font-size: 1rem;
    --small-font-size: .875rem;
  }
}

/*========== BASE ==========*/
*,::before,::after{
  box-sizing: border-box;
}

html{
  scroll-behavior: smooth;
}
/*========== Variables Dark theme ==========*/
body.dark-theme{
  --first-color-send: #161212;
  --title-color: #F3F1F1;
  --text-color: #D1C7C8;
  --body-color: #251D1E;
  --container-color: #302728;
}

/*========== Button Dark/Light ==========*/
.change-theme{
  position: absolute;
  right: 1.5rem;
  top: 2.2rem;
  display: flex;
  color: var(--title-color);
  font-size: 2rem;
  cursor: pointer;
}

body{
  margin: var(--header-height) 0 0 0;
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
  background-color: var(--body-color);
  color: var(--text-color);
  line-height: 1.6;
}

h1,h2,h3,ul,p{
  margin: 0;
}

h1,h2,h3{
  font-weight: var(--font-semi-bold);
  color: var(--title-color);
}

ul{
  padding: 0;
  list-style: none;
}

a{
  text-decoration: none;
}

img{
  max-width: 100%;
  height: auto;
}

/*========== CLASS CSS ==========*/
.section{
  padding: 4rem 0 2rem;
}

.section-title, .section-title-center{
  font-size: var(--h2-font-size);
  color: var(--title-color);
  text-align: center;
  margin-bottom: var(--mb-3);
}

/*========== LAYOUT ==========*/
.l-main{
  overflow: hidden;
}

.bd-container{
  max-width: 968px;
  width: calc(100% - 3rem);
  margin-left: var(--mb-3);
  margin-right: var(--mb-3);
}

.bd-grid{
  display: grid;
  gap: 1.5rem;
}

.l-header{
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: var(--z-fixed);
  background-color: var(--body-color);
}

/*========== NAV ==========*/
.nav{
  height: var(--header-height);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media screen and (max-width: 768px){
  .nav__menu{
    position: fixed;
    top: -100%;
    left: 0;
    right: 0;
    width: 90%;
    margin: 0 auto;
    padding: 2.5rem 0 0;
    text-align: center;
    background-color: var(--body-color);
    transition: .4s;
    box-shadow: 0 0 4px rgba(0,0,0,.1);
    border-radius: 2rem;
    z-index: var(--z-fixed);
  }
}

.nav__item{
  margin-bottom: var(--mb-3);
}

.nav__link, .nav__logo, .nav__toggle{
  color: var(--title-color);
  font-weight: var(--font-semi-bold);
}

.nav__logo:hover{
  color: var(--first-color);
}

.nav__link{
  transition: .3s;
}

.nav__link:hover{
  color: var(--first-color);
}

.nav__toggle{
  font-size: 1.3rem;
  cursor: pointer;
}

/* Show menu */
.show-menu{
  top: calc(var(--header-height) + 1rem);
}

/* Active menu link */
.active-link{
  position: relative;
}

.active-link::before{
  content: '';
  position: absolute;
  bottom: -.75rem;
  left: 45%;
  width: 5px;
  height: 5px;
  background-color: var(--title-color);
  border-radius: 50%;
}

/* Change background header */
.scroll-header{
  box-shadow: 0 1px 4px rgba(0,0,0,.1);
}

/* Scroll top */
.scrolltop{
  position: fixed;
  right: 1rem;
  bottom: -20%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: .3rem;
  background: rgba(218,37,53,.5);
  border-radius: .4rem;
  z-index: var(--z-tooltip);
  transition: .4s;
  visibility: hidden;
}

.scrolltop:hover{
  background-color: var(--first-color);
}

.scrolltop__icon{
  font-size: 1.5rem;
  color: var(--body-color);
}

.show-scroll{
  visibility: visible;
  bottom: 1.5rem;
}

/*========== HOME ==========*/
.home__container{
  row-gap: .5rem;
}

.home__img{
  width: 280px;
  justify-self: center;
}

.home__title{
  font-size: var(--biggest-font-size);
  font-weight: var(--font-bold);
  margin-bottom: var(--mb-2);
}

.home__description{
  margin-bottom: var(--mb-3);
}

/*========== BUTTONS ==========*/
.button{
  display: inline-block;
  background-color: var(--first-color);
  color: #fff;
  padding: 1rem 1.5rem;
  border-radius: .5rem;
  font-weight: var(--font-semi-bold);
  transition: .3s;
}

.button:hover{
  background-color: var(--first-color-alt);
}

.button-link{
  background: none;
  padding: 0;
  color: var(--first-color);
}

.button-link:hover{
  background-color: transparent;
  color: var(--first-color-alt);
}

/*========== SHARE ==========*/
.share__data{
  text-align: center;
}

.share__description{
  margin-bottom: var(--mb-2);
}

.share__img{
  width: 280px;
  justify-self: center;
}

/*========== DECORATION ==========*/
.decoration__container{
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.decoration__data{
  text-align: center;
  padding: 1rem 1rem 2rem;
  background-color: var(--container-color);
  box-shadow: 0 2px 6px rgba(65,11,16,.15);
  border-radius: 1rem;
}

.decoration__data:hover{
  box-shadow: 0 3px 12px rgba(65,11,16,.15);
}

.decoration__img{
  width: 180px;
}

.decoration__title{
  font-size: var(--h3-font-size);
  margin-bottom: var(--mb-1);
}

/*========== ACCESSORIES ==========*/
.accessory__container{
  grid-template-columns: repeat(2,1fr);
  padding-bottom: 2rem;
}

.accessory__content{
  position: relative;
  display: grid;
  padding: .25rem .75rem .75rem;
  background-color: var(--container-color);
  box-shadow: 0 2px 6px rgba(65,11,16,.15);
  border-radius: 1rem;
}

.accessory__content:hover{
  box-shadow: 0 3px 12px rgba(65,11,16,.15);
}

.accessory__img{
  width: 110px;
  justify-self: center;
  margin-bottom: .25rem;
}

.accessory__title, .accessory__category{
  text-align: center;
}

.accessory__title{
  font-size: var(--normal-font-size);
}

.accessory__category{
  font-size: var(--small-font-size);
  margin-bottom: var(--mb-1);
  color: var(--text-color-light);
}

.accessory__preci{
  font-weight: var(--font-semi-bold);
  color: var(--title-color);
}

.accessory__button{
  position: absolute;
  bottom: 0;
  right: 0;
  display: flex;
  font-size: 1.25rem;
  padding: .5rem .625rem;
  border-radius: 1rem 0 1rem 0;
}

/*========== SEND GIFT ==========*/
.send{
  background-color: var(--first-color-send);
}

.send__title, .send__description{
  color: #fff;
}

.send__description{
  text-align: center;
  margin-bottom: var(--mb-4);
}

.send__direction{
  display: flex;
  justify-content: space-between;
  background-color: #fff;
  padding: .5rem;
  border-radius: .5rem;
}

.send__input{
  width: 70%;
  outline: none;
  border: none;
  font-size: var(--normal-font-size);
  font-family: var(--body-font);
}

.send__input::placeholder{
  font-family: var(--body-font);
}

.send__img{
  width: 280px;
  justify-self: center;
}

/*FAQ*/.wrapper {
  margin: 20px;
  font-family: var(--body-font);
}

.wrapper .faq {
  margin-bottom: 10px;
}

.wrapper .faq .accordion {
  border-radius: .5rem;
  background-color: #f1f1f1;
  color: #333;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  transition: background-color 0.4s, max-height 0.3s ease-out; /* Added smooth transition for max-height */
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
}

.wrapper .faq .accordion:hover {
  background-color: #ddd;
}

.wrapper .faq .accordion.active {
  background-color: #ccc;
}

.wrapper .faq .accordion i {
  float: right;
}

.wrapper .faq .pannel {
  border-radius: .5rem;
  padding: 0 18px;
  display: none;
  background-color: white;
  color:#333;
  overflow: hidden;
  max-height: 0;
  transition: max-height 0.3s ease-out; /* Added smooth transition for max-height */
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
}

.wrapper .faq .pannel p {
  margin: 10px 0;
}

.wrapper .faq.active .pannel {
  display: block;
  max-height: 500px;
}
/*========== FOOTER ==========*/
.footer__container{
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.footer__logo{
  color: var(--title-color);
}

.footer__title{
  margin-bottom: var(--mb-2);
}

.footer__logo, .footer__title{
  font-size: var(--h3-font-size);
}

.footer__link{
  display: inline-block;
  margin-bottom: .75rem;
  color: var(--text-color);
}

.footer__link:hover{
  color: var(--first-color);
}

.footer__social{
  font-size: 1.5rem;
  color: var(--title-color);
  margin-right: var(--mb-3);
}

.footer__social:hover{
  color: var(--first-color);
}

.footer__copy{
  text-align: center;
  font-size: var(--small-font-size);
  color: var(--text-color-light);
  margin-top: 4rem;
}

/*========== MEDIA QUERIES ==========*/

/* For full-screen images on small screens */
@media screen and (max-width: 359px){
  .home__img,
  .share__img,
  .send__img{
    width: 100%;
  }
}

@media screen and (min-width: 576px){
  .home__container,
  .share__container,
  .send__container{
    grid-template-columns: repeat(2,1fr);
    align-items: center;
  }

  .home__container{
    padding: 5rem 0 0;
  }

  .home__img{
    order: 1;
  }

  .section-title-center,
  .share__data,
  .send__description{
    text-align: initial;
  }

  .home__img,
  .share__img,
  .send__img{
    width: 100%;
  }
  
  .share__img{
    order: -1;
  }
}

@media screen and (min-width: 768px){
  body{
    margin: 0;
  }

  .section{
    padding-top: 7rem;
  }

  .nav{
    height: calc(var(--header-height) + 1.5rem);
  }

  .nav__list{
    display: flex;
    align-items: center;
  }

  .nav__item{
    margin-left: var(--mb-5);
    margin-bottom: 0;
  }

  .nav__toggle{
    display: none;
  }

  .change-theme{
    position: initial;
    margin-left: var(--mb-4);
  }

  .home__container{
    padding: 7rem 2rem 0;
  }

  .share__container{
    padding: 0 2rem;
  }

  .accessory__container{
    grid-template-columns: repeat(3,224px);
    justify-content: center;
  }

  .accessory__content{
    padding: .5rem 1.5rem 1.5rem;
  }

  .accessory__img{
    width: 120px;
    margin-bottom: var(--mb-1);
  }

  .accessory__title, .accessory__category{
    text-align: initial;
  }

  .accessory__button{
    padding: .75rem;
  }

  .send{
    background: none;
  }

  .send__container{
    background-color: var(--first-color-send);
    padding: 2rem;
    border-radius: 1.5rem;
  }
}

@media screen and (min-width: 968px){
  .bd-container{
    margin-left: auto;
    margin-right: auto;
  }

  .home__img,
  .share__img,
  .send__img{
    width: 469px;
  }

  .home__container,
  .share__container,
  .send__container{
    column-gap: 5rem;
  }
}
