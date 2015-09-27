var ledscontrol = (function($){

    function sendCommand($element, active){
        var data = 'ref='+$element.data('ref')+'&active='+active;

        $.ajax({
            url: '/leds/update',
            method: 'POST',
            data: data
        }).done(function(response){
            console.log(response)
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    return {
        init: function(){
            this.initCSRF();
            this.bindLeds();
        },


        initCSRF: function(){
            var csrftoken = getCookie('csrftoken');
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
        },

        bindLeds: function(){
            var self = this;
            $('.label-led').on('click', function () {
                sendCommand.call(self, $(this), !$(this).hasClass('active'))
            })
        }
    };


})(jQuery)


$( document ).ready(function() {
  ledscontrol.init();
});