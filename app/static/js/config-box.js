const set_view_text = (text) => {
    $("#switch-view-btn").text(text)
}

$("#switch-view-btn").click(function () {

    let alternate_view = $("#switch-view-btn").attr("href")
    window.location.href = alternate_view;
});

export {set_view_text};