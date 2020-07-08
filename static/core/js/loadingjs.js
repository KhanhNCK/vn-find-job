$(window).on('load',function (event) {
    $('body').removeClass('preloading');
    $('#preload').delay(1000).fadeOut('fast');
});
