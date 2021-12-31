$(document).ready(function () {
    $('.file-upload').hide()
    $('.button').click(function () {
        $(this).hide();
        $('.file-upload').show()
    })

    $("#nav").click(function () {
        $('.super-container').toggleClass('super')
        $('.menu-container').toggle()
    });
    $('#btn-of-upload').click(function () {
        $(this).add('h1')
    })

    $('.copy-content').click(function () {
        copy('.copycontent')
    })

    $('.content-mcq').hide()
    $('.form-btn').hide()
    $('.normal-container').click(function () {
        $('#content').toggle()
        $('.category').toggle()
        $('#files').toggle()
        $('.content-mcq').show()
        $('.form-btn').show()
    })
});