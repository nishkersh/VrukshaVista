const map = new google.maps.Map(document.getElementById('google-earth'), {
    center: { lat: 23.226670906906943, lng: 77.32310944557776 },
    zoom: 17,
    mapTypeId: google.maps.MapTypeId.SATELLITE,
    styles: [
        {
            featureType: "all",
            elementType: "labels",
            stylers: [{ visibility: "on" }]
        }
    ]
});

function initMap() {
    console.log('Map Loaded');
}

var button = document.querySelector('button');
button.addEventListener('click', function () {
    var lat = map.getCenter().lat();
    var lng = map.getCenter().lng();
    var zoom = map.getZoom();

    fetch('/map', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ lat: lat, lng: lng, zoom: zoom })
    }).then(function (response) {
        alert(response.json());
    }).then(function (data) {
        alert(data);
    });

});