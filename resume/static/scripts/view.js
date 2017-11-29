'use strict';

const resumeView = {};

resumeView.initPage = function() {
  resumeView.handleNav();

  $('.main-nav, .toggle-menu').removeAttr('style');

  function closeNav() {
    if ($('.toggle-menu').hasClass('icon-cross')) {
      $('.main-nav').removeClass('show');
      $('.toggle-menu').removeClass('icon-cross');
    }
  }
  
  var buffer = false;
  $(window).on('resize scroll', function() {
    if (buffer !== false) {
      clearTimeout(buffer);
    }
    buffer = setTimeout(function(){
      closeNav();
    }, 100);
  });

  $('.toggle-menu').on('click', function() {
    if ($(this).hasClass('icon-cross')) {
      closeNav();
    } else {
      $('.main-nav').addClass('show');
      $('.toggle-menu').addClass('icon-cross');
    }
  });

  $(window).scroll(function() {
    if ($(this).scrollTop() > 0) {
      $('body').addClass('sticky');
    }
    else {
      $('body').removeClass('sticky');
      $('nav .tab').removeClass('current');
    }
  });
};

resumeView.handleNav = function() {
  $('.main-nav a').on('click', function(e) {
    e.preventDefault();
    let scroller;
    let route = $(this).attr('href');
    if (route === '/') {
      scroller = 0;
    } else {
      route = route.substring(1);
      if (($(`${route}`).length > 0)) {
        scroller = $(`${route}`).offset().top;
      } else {
        scroller = 0;
      }
    }
    $('html, body').animate({
      scrollTop: scroller
    }, 800);
  });
}
