$(document).ready(function () {

    $('#submitWeather').click(function () {

        var city = $('#city').val();
        var out='';

        if(city != ''){

            $.ajax({

                url:'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric' +
                    '&APPID=bf92102ecd82d3994af53c403681fbd1',
                type: 'GET',
                dataType: 'jsonp',
                success: function(data){
                    let out='';
                        // out +='Погода: <b>'+data.weather[0].main+'</b><br>';
                        out +='<p"><img src="https://openweathermap.org/img/w/' + data.weather[0].icon + '.png"></p>';
                        out +='Температура: <b>' + Math.round(data.main.temp)+'&#176;C</b><br>';
                        out +='Влажность: <b>' + data.main.humidity + '%</b><br>';
                        out +='Давление: <b>'+ Math.round(data.main.pressure*0.00750063755419211*100)+'мм.рт.ст</b><br>';
                        out +='Видимость: <b>' + (data.visibility/1000)+'км</b><br>';
                        console.log(data.main);
                        $('#show').html(out);
                }

                });
            }else{
                $('#error').html('Fiend cannot be empty');
            }

                });

});

