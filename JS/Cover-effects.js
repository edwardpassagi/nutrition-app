var first_click = false;
var second_click = false; 
var clicks = 0

$(document).ready(function() {
    
    $(window).ready(function() {
        document_initiation();
        button_click_setting();
        var num = $('.inner h3').width();
        // console.log(num);
        set_header3_position();
    });

    $(window).resize(function() {
        // document_resized();
        console.log('\n');
        set_header3_position();
        var header1_font_size = $('.inner h1').css('font-size');
        console.log("header 1 font size: " + header1_font_size);
        var header2_font_size = $('.inner h2').css('font-size');
        console.log("header 2 font size: " + header2_font_size);
        var header3_font_size = $('.inner h3').css('font-size');
        console.log("header 3 font size: " + header3_font_size);
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

function set_header3_position() {
    var window_width = $('body').width();
    var header3_width = $('.inner h3').width();
    
    console.log("header 3 width: " + header3_width);
    console.log("window width: " + window_width);
    $('.inner h3').css('left', window_width/2 - header3_width/2);
}