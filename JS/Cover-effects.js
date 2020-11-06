var first_click = false;
var second_click = false; 
var clicks = 0
var lower_height = 0;
$(document).ready(function() {
    
    $(window).ready(function() {
        document_initiation();
        button_click_setting();
        set_coming_soon_position();
        setTimeout(function() {
            lower_height = $('.lower-inner').height();
        }, 900);
        // lower_side_setup(lower_height);
    });

    $(window).resize(function() {
        // document_resized();
        set_coming_soon_position();
        // lower_side_setup(lower_height);
    });

    $(document).scroll(function() {
        // documnet_scrolled();
    });
});

function document_initiation() {
    hide_elements();

    setTimeout(function() {
        $('.lower-inner h1').fadeIn(1000);
    }, 900);

    setTimeout(function() {
        $('.lower-inner h2').fadeIn(1000);
    }, 1600);

    setTimeout(function() {
        $('.lower-inner button').fadeIn(500);
    }, 1600);

    setTimeout(function() {
        $('.lower-inner h3').fadeIn(1000);
    }, 2000);
}

function hide_elements() {
    $('.lower-inner h1').hide();
    $('.lower-inner h2').hide();
    $('.lower-inner button').hide();
    $('.lower-inner h3').hide();
}

function button_click_setting() {
    $('.inner button').click(function() {
        if (clicks == 0) {
            clicks = 1;
            $('.inner button').css('color', 'white');
        } else {
            $('.inner a').attr('href', '/Main/main.html');
        }
    });
}

function set_coming_soon_position() {
    var window_width = $('body').width();
    setTimeout(function() {
        var header3_width = $('.inner h3').width();
        $('.inner h3').css('left', window_width/2 - header3_width/2);
    }, 2100);
}

function lower_side_setup(lower_height) {
    var current_lower = $('.lower').height();
    if(current_lower < 140) {
        $('.inner h3').css('position', 'relative');
        console.log('we are here');
    }
}