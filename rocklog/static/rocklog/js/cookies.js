if(localStorage.getItem('cookieSeen') != 'shown'){
  $(".cookie-banner").delay(2000).fadeIn();
}

$('.close').click(function(e) {
  localStorage.setItem('cookieSeen','shown')
  $('.cookie-banner').fadeOut();
});
