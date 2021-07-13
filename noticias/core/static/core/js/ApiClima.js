$(document).ready(function(){
    $("#msj").hide();
        navigator.geolocation.getCurrentPosition(function(lugarx){
        
        var url = `https://fcc-weather-api.glitch.me/api/current?lat=${lugarx.coords.latitude}&lon=${lugarx.coords.longitude}`;
        traerDatos(url);

        // function traerDatos(url){
        //     $.get(url,function(data){
        //         $("#msj").append(`<div>
        //                         <td>${data.name}</td>
        //                         <td>${data.name}</td>
        //                         <td><img src='${data.weather[0].icon}'></td>   
        //                         </div>`);
        //         $("#msj").show();
        //     })
        // }  

        function traerDatos(url){
            $.get(url,function(data){
                $("#msj").append(`<div>
                                        <td>${data.name}</td>
                                        <td>${(data.main.feels_like)}°C </td>
                                        <img src='${data.weather[0].icon}'>
                                    </div>`)
                                 $("#msj").show()
            })
        }



    })
})