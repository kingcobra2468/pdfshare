'use strict';

// sets the text on gallery/list config box btn
const set_view_text = (text) => {
    $('#switch-view-btn').text(text)
}

// sets the text on the theme button
const set_mode_text = (text) => {
    $('#dark-mode-btn').text(text)
}

// toggle between light and dark theme
const toggle_mode = () => {

    let mode = localStorage.getItem('theme');
    
    if (mode == null) { // is no theme is cached, default to light theme
        localStorage.setItem('theme', 'light');
        mode = 'light'
    }

    if (mode == 'dark') {
        $(document.documentElement).attr('theme', 'light');
        localStorage.setItem('theme', 'light');
        set_mode_text('Dark Theme');
    }
    else {
        $(document.documentElement).attr('theme', 'dark');
        localStorage.setItem('theme', 'dark');
        set_mode_text('Light Theme');
    }
}

// set the correct mode when loading page
const set_mode = () => {
    let mode = localStorage.getItem('theme');
    
    if (mode == null) { // is no theme is cached, default to light theme
        localStorage.setItem('theme', 'light');
        mode = 'light'
    }

    if (mode == 'light') {
        $(document.documentElement).attr('theme', 'light');
        set_mode_text('Dark Theme');
    }
    else {
        $(document.documentElement).attr('theme', 'dark');
        set_mode_text('Light Theme');
    }
}

// event to listen when list/gallery btn was clicked
$('#switch-view-btn').click(function () {

    let alternate_view = $('#switch-view-btn').attr('href');
    window.location.href = alternate_view;
});

// event to listen when theme button was clicked
$('#dark-mode-btn').click(function () {
    toggle_mode();
});

// on page load event
$(document).ready(function () {

    set_mode();
});

export {set_view_text};