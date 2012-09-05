(function($) {
    $(document).ready(function() {

        $("#desktop article.list section.task h1").click(function(){
            $(this).parent().parent().toggleClass("task-open");
        });

        scrollbars();

    })
})(jQuery);

function scrollbars() {
    $('.scrollable').jScrollPane({autoReinitialise: true});

    var api = $(".scrollable").data("jsp");
    $(window).bind('resize', function(){
        if ($.browser.msie) {
            // IE fires multiple resize events while you are dragging the browser window which
            // causes it to crash if you try to update the scrollpane on every one. So we need
            // to throttle it to fire a maximum of once every 50 milliseconds...
            if (!throttleTimeout) {
                throttleTimeout = setTimeout(function(){
                    api.reinitialise();
                    throttleTimeout = null;
                }, 50);
            }
        } else {
            console.log(api);
            api.reinitialise();
        }
    });

}
