$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
         theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        // open or close navbar
        $('#sidebar').toggleClass('active');
        // close dropdowns
        $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

function initMap() {
    var locationInput = document.getElementById('autocomplete-input');

    var autocomplete_one = new google.maps.places.Autocomplete(locationInput);

    // var objLocation;
    // google.maps.event.addListener(autocomplete_one, 'place_changed', function () {
    //     objLocation = autocomplete_one.getPlace();
    // });

    // autocomplete_one.addListener('place_changed', e => {
    //     // addPeople();
    // })

    // function addPeople() {
    //     if (objLocation) {cord = {
    //         lat: objLocation.geometry.location.lat(),
    //         lng: objLocation.geometry.location.lng(),
    //     }}
    //
    //     var obj = {
    //         cord: cord,
    //         name: objLocation.formatted_address
    //     };
    //     // locationInput.value = "";
    // }
}

// list animation
function listAnimation() {
    var i = 0;
    var delay_duration = 0.1;
    var animations = ["fadeInRight","fadeInUp","flipInX","lightSpeedIn","zoomInDown"]; //,"rotateInDownRight","rotateInUpLeft"
    var animation = "animated " + animations[Math.floor(Math.random() * animations.length)];
    $(".list-group li").each(function(){
        $(this).css("animation-delay",(delay_duration * i++)+"s");
        $(this).css("animation-duration","0.8s");
        $(this).addClass(animation);
    });
    setTimeout(function(){
         $(".list-group li").each(function(){
            $(this).removeClass(animation);
        });
    },(++i * delay_duration * 1000));
}
