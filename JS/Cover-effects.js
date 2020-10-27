var first_click = false;
var second_click = false; 
var clicks = 0

$(document).ready(function() {
    
    $(window).ready(function() {
        document_initiation();
        button_click_setting();
    });

    $(window).resize(function() {
        // document_resized();
    });

    $(document).scroll(function() {
        // documnet_scrolled();
    });
});

function document_initiation() {
    hide_elements();

    setTimeout(function() {
        $('.inner h1').fadeIn(1000);
    }, 900);

    setTimeout(function() {
        $('.inner h2').fadeIn(1000);
    }, 1600);

    setTimeout(function() {
        $('.inner button').fadeIn(500);
    }, 1600);

    setTimeout(function() {
        $('.inner h3').fadeIn(1000);
    }, 2000);
}

function hide_elements() {
    $('.inner h1').hide();
    $('.inner h2').hide();
    $('.inner button').hide();
    $('.inner h3').hide();
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