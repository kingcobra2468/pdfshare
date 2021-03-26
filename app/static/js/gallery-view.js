import {set_view_text} from './config-box.js';

$(document).ready(function () {

    $("#switch-view-btn").attr("href", "/library/list-view");
    set_view_text('List View');
});