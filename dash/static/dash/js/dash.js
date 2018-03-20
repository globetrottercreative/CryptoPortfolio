var main = function() {
    var endpoint = '/api/data/chart/';

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data) {
            var ctx = document.getElementById("myChartEth").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.nz_eth_dates,
                    datasets: [{
                            label: '60 Day (NZD)',
                            data: data.nz_eth_data,
                            borderColor: '#483D8B',
                            borderWidth: 1,
                            lineTension: 0
                        },
                        {
                            label: '60 Day (USD)',
                            data: data.us_eth_data,
                            borderColor: '#6610f2',
                            borderWidth: 1,
                            lineTension: 0
                        }
                    ]
                },
                options: {}
            });

            var ctx = document.getElementById("myChartBtc").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.nz_btc_dates,
                    datasets: [{
                            label: '60 Day (NZD)',
                            data: data.nz_btc_data,
                            borderColor: '#483D8B',
                            borderWidth: 1,
                            lineTension: 0
                        },
                        {
                            label: '60 Day (USD)',
                            data: data.us_btc_data,
                            borderColor: '#6610f2',
                            borderWidth: 1,
                            lineTension: 0
                        }
                    ]
                },
                options: {}
            });

            var ctx = document.getElementById("myChartBch").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.nz_bch_dates,
                    datasets: [{
                            label: '60 Day (NZD)',
                            data: data.nz_bch_data,
                            borderColor: '#483D8B',
                            borderWidth: 1,
                            lineTension: 0
                        },
                        {
                            label: '60 Day (USD)',
                            data: data.us_bch_data,
                            borderColor: '#6610f2',
                            borderWidth: 1,
                            lineTension: 0
                        }
                    ]
                },
                options: {}
            });
        },
        error: function(error_data) {

        }
    })
};

$(window).on('load', main);