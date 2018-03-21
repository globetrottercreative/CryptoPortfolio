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
                    }]
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
                    }]
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
                    }]
                },
                options: {}
            });
        },
        error: function(error_data) {

        }
    })
};

$(window).on('load', main);

var updateSpots = function() {

    var endpoint = '/api/data/spot/'

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data) {

            var ethirhigh = document.getElementById("ETHIR").getElementsByClassName("spothigh")[0];
            var cur = Number(ethirhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_ir.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethirhigh.className = "spothigh red";
            } else if (cur < nw) {
                ethirhigh.className = "spothigh green";
            } else {
                ethirhigh.className = "spothigh black";
            }
            ethirhigh.innerText = '$' + data.eth_ir.high;

            var ethirprice = document.getElementById("ETHIR").getElementsByClassName("spotprice")[0];
            var cur = Number(ethirprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_ir.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethirprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                ethirprice.className = "display-4 spotprice green";
            } else {
                ethirprice.className = "display-4 spotprice black";
            }
            ethirprice.innerText = '$' + data.eth_ir.price;

            var ethirlow = document.getElementById("ETHIR").getElementsByClassName("spotlow")[0];
            var cur = Number(ethirlow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_ir.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethirlow.className = "spotlow red";
            } else if (cur < nw) {
                ethirlow.className = "spotlow green";
            } else {
                ethirlow.className = "spotlow black";
            }
            ethirlow.innerText = '$' + data.eth_ir.low;

            var btcirhigh = document.getElementById("BTCIR").getElementsByClassName("spothigh")[0];
            var cur = Number(btcirhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_ir.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcirhigh.className = "spothigh red";
            } else if (cur < nw) {
                btcirhigh.className = "spothigh green";
            } else {
                btcirhigh.className = "spothigh black";
            }
            btcirhigh.innerText = '$' + data.btc_ir.high;

            var btcirprice = document.getElementById("BTCIR").getElementsByClassName("spotprice")[0];
            var cur = Number(btcirprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_ir.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcirprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                btcirprice.className = "display-4 spotprice green";
            } else {
                btcirprice.className = "display-4 spotprice black";
            }
            btcirprice.innerText = '$' + data.btc_ir.price;

            var btcirlow = document.getElementById("BTCIR").getElementsByClassName("spotlow")[0];
            var cur = Number(btcirlow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_ir.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcirlow.className = "spotlow red";
            } else if (cur < nw) {
                btcirlow.className = "spotlow green";
            } else {
                btcirlow.className = "spotlow black";
            }
            btcirlow.innerText = '$' + data.btc_ir.low;

            var bchirhigh = document.getElementById("BCHIR").getElementsByClassName("spothigh")[0];
            var cur = Number(bchirhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_ir.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchirhigh.className = "spothigh red";
            } else if (cur < nw) {
                bchirhigh.className = "spothigh green";
            } else {
                bchirhigh.className = "spothigh black";
            }
            bchirhigh.innerText = '$' + data.bch_ir.high;

            var bchirprice = document.getElementById("BCHIR").getElementsByClassName("spotprice")[0];
            var cur = Number(bchirprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_ir.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchirprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                bchirprice.className = "display-4 spotprice green";
            } else {
                bchirprice.className = "display-4 spotprice black";
            }
            bchirprice.innerText = '$' + data.bch_ir.price;

            var bchirlow = document.getElementById("BCHIR").getElementsByClassName("spotlow")[0];
            var cur = Number(bchirlow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_ir.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchirlow.className = "spotlow red";
            } else if (cur < nw) {
                bchirlow.className = "spotlow green";
            } else {
                bchirlow.className = "spotlow black";
            }
            bchirlow.innerText = '$' + data.bch_ir.low;

            var ethcryhigh = document.getElementById("ETHCRY").getElementsByClassName("spothigh")[0];
            var cur = Number(ethcryhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_cry.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethcryhigh.className = "spothigh red";
            } else if (cur < nw) {
                ethcryhigh.className = "spothigh green";
            } else {
                ethcryhigh.className = "spothigh black";
            }
            ethcryhigh.innerText = '$' + data.eth_cry.high;

            var ethcryprice = document.getElementById("ETHCRY").getElementsByClassName("spotprice")[0];
            var cur = Number(ethcryprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_cry.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethcryprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                ethcryprice.className = "display-4 spotprice green";
            } else {
                ethcryprice.className = "display-4 spotprice black";
            }
            ethcryprice.innerText = '$' + data.eth_cry.price;

            var ethcrylow = document.getElementById("ETHCRY").getElementsByClassName("spotlow")[0];
            var cur = Number(ethcrylow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.eth_cry.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethcrylow.className = "spotlow red";
            } else if (cur < nw) {
                ethcrylow.className = "spotlow green";
            } else {
                ethcrylow.className = "spotlow black";
            }
            ethcrylow.innerText = '$' + data.eth_cry.low;

            var btccryhigh = document.getElementById("BTCCRY").getElementsByClassName("spothigh")[0];
            var cur = Number(btccryhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_cry.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btccryhigh.className = "spothigh red";
            } else if (cur < nw) {
                btccryhigh.className = "spothigh green";
            } else {
                btccryhigh.className = "spothigh black";
            }
            btccryhigh.innerText = '$' + data.btc_cry.high;

            var btccryprice = document.getElementById("BTCCRY").getElementsByClassName("spotprice")[0];
            var cur = Number(btccryprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_cry.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btccryprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                btccryprice.className = "display-4 spotprice green";
            } else {
                btccryprice.className = "display-4 spotprice black";
            }
            btccryprice.innerText = '$' + data.btc_cry.price;

            var btccrylow = document.getElementById("BTCCRY").getElementsByClassName("spotlow")[0];
            var cur = Number(btccrylow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.btc_cry.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btccrylow.className = "spotlow red";
            } else if (cur < nw) {
                btccrylow.className = "spotlow green";
            } else {
                btccrylow.className = "spotlow black";
            }
            btccrylow.innerText = '$' + data.btc_cry.low;

            var bchcryhigh = document.getElementById("BCHCRY").getElementsByClassName("spothigh")[0];
            var cur = Number(bchcryhigh.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_cry.high.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchcryhigh.className = "spothigh red";
            } else if (cur < nw) {
                bchcryhigh.className = "spothigh green";
            } else {
                bchcryhigh.className = "spothigh black";
            }
            bchcryhigh.innerText = '$' + data.bch_cry.high;

            var bchcryprice = document.getElementById("BCHCRY").getElementsByClassName("spotprice")[0];
            var cur = Number(bchcryprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_cry.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchcryprice.className = "display-4 spotprice red";
            } else if (cur < nw) {
                bchcryprice.className = "display-4 spotprice green";
            } else {
                bchcryprice.className = "display-4 spotprice black";
            }
            bchcryprice.innerText = '$' + data.bch_cry.price;

            var bchcrylow = document.getElementById("BCHCRY").getElementsByClassName("spotlow")[0];
            var cur = Number(bchcrylow.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.bch_cry.low.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchcrylow.className = "spotlow red";
            } else if (cur < nw) {
                bchcrylow.className = "spotlow green";
            } else {
                bchcrylow.className = "spotlow black";
            }
            bchcrylow.innerText = '$' + data.bch_cry.low;
        },
        error: function(error_data) {

        }
    });
};

setInterval(updateSpots, 60 * 1000);

var updateCMC = function() {
    var endpoint = '/api/data/cmc/'

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data) {
            //ETH
            var ethmarketcap = document.getElementById("CMCETH").getElementsByClassName("marketcap")[0];
            var cur = Number(ethmarketcap.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_eth.marketcap.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethmarketcap.className = "marketcap red";
            } else if (cur < nw) {
                ethmarketcap.className = "marketcap green";
            } else {
                ethmarketcap.className = "marketcap black";
            }
            ethmarketcap.innerText = '$' + data.cmc_eth.marketcap;

            var ethprice = document.getElementById("CMCETH").getElementsByClassName("price")[0];
            var cur = Number(ethprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_eth.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethprice.className = "price red";
            } else if (cur < nw) {
                ethprice.className = "price green";
            } else {
                ethprice.className = "price black";
            }
            ethprice.innerText = '$' + data.cmc_eth.price;

            var ethchang24 = document.getElementById("CMCETH").getElementsByClassName("chg24")[0];
            var cur = Number(ethchang24.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_eth.change24.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethchang24.className = "chg24 red";
            } else if (cur < nw) {
                ethchang24.className = "chg24 green";
            } else {
                ethchang24.className = "chg24 black";
            }
            ethchang24.innerText = data.cmc_eth.change24 + '%';

            var ethchang7 = document.getElementById("CMCETH").getElementsByClassName("chg7")[0];
            var cur = Number(ethchang7.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_eth.change7.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethchang7.className = "chg7 red";
            } else if (cur < nw) {
                ethchang7.className = "chg7 green";
            } else {
                ethchang7.className = "chg7 black";
            }
            ethchang7.innerText = data.cmc_eth.change7 + '%';

            var ethsupply = document.getElementById("CMCETH").getElementsByClassName("supply")[0];
            var cur = Number(ethsupply.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_eth.supply.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                ethsupply.className = "supply red";
            } else if (cur < nw) {
                ethsupply.className = "supply green";
            } else {
                ethsupply.className = "supply black";
            }
            ethsupply.innerText = data.cmc_eth.supply;

            //BTC
            var btcmarketcap = document.getElementById("CMCBTC").getElementsByClassName("marketcap")[0];
            var cur = Number(btcmarketcap.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_btc.marketcap.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcmarketcap.className = "marketcap red";
            } else if (cur < nw) {
                btcmarketcap.className = "marketcap green";
            } else {
                btcmarketcap.className = "marketcap black";
            }
            btcmarketcap.innerText = '$' + data.cmc_btc.marketcap;

            var btcprice = document.getElementById("CMCBTC").getElementsByClassName("price")[0];
            var cur = Number(btcprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_btc.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcprice.className = "price red";
            } else if (cur < nw) {
                btcprice.className = "price green";
            } else {
                btcprice.className = "price black";
            }
            btcprice.innerText = '$' + data.cmc_btc.price;

            var btcchang24 = document.getElementById("CMCBTC").getElementsByClassName("chg24")[0];
            var cur = Number(btcchang24.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_btc.change24.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcchang24.className = "chg24 red";
            } else if (cur < nw) {
                btcchang24.className = "chg24 green";
            } else {
                btcchang24.className = "chg24 black";
            }
            btcchang24.innerText = data.cmc_btc.change24 + '%';

            var btcchang7 = document.getElementById("CMCBTC").getElementsByClassName("chg7")[0];
            var cur = Number(btcchang7.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_btc.change7.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcchang7.className = "chg7 red";
            } else if (cur < nw) {
                btcchang7.className = "chg7 green";
            } else {
                btcchang7.className = "chg7 black";
            }
            btcchang7.innerText = data.cmc_btc.change7 + '%';

            var btcsupply = document.getElementById("CMCBTC").getElementsByClassName("supply")[0];
            var cur = Number(btcsupply.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_btc.supply.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                btcsupply.className = "supply red";
            } else if (cur < nw) {
                btcsupply.className = "supply green";
            } else {
                btcsupply.className = "supply black";
            }
            btcsupply.innerText = data.cmc_btc.supply;

            //BCH
            var bchmarketcap = document.getElementById("CMCBCH").getElementsByClassName("marketcap")[0];
            var cur = Number(bchmarketcap.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_bch.marketcap.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchmarketcap.className = "marketcap red";
            } else if (cur < nw) {
                bchmarketcap.className = "marketcap green";
            } else {
                bchmarketcap.className = "marketcap black";
            }
            bchmarketcap.innerText = '$' + data.cmc_bch.marketcap;

            var bchprice = document.getElementById("CMCBCH").getElementsByClassName("price")[0];
            var cur = Number(bchprice.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_bch.price.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchprice.className = "price red";
            } else if (cur < nw) {
                bchprice.className = "price green";
            } else {
                bchprice.className = "price black";
            }
            bchprice.innerText = '$' + data.cmc_bch.price;

            var bchchang24 = document.getElementById("CMCBCH").getElementsByClassName("chg24")[0];
            var cur = Number(bchchang24.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_bch.change24.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchchang24.className = "chg24 red";
            } else if (cur < nw) {
                bchchang24.className = "chg24 green";
            } else {
                bchchang24.className = "chg24 black";
            }
            bchchang24.innerText = data.cmc_bch.change24 + '%';

            var bchchang7 = document.getElementById("CMCBCH").getElementsByClassName("chg7")[0];
            var cur = Number(bchchang7.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_bch.change7.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchchang7.className = "chg7 red";
            } else if (cur < nw) {
                bchchang7.className = "chg7 green";
            } else {
                bchchang7.className = "chg7 black";
            }
            bchchang7.innerText = data.cmc_bch.change7 + '%';

            var bchsupply = document.getElementById("CMCBCH").getElementsByClassName("supply")[0];
            var cur = Number(bchsupply.innerText.replace(/[^0-9\.-]+/g, ""));
            var nw = Number(data.cmc_bch.supply.replace(/[^0-9\.-]+/g, ""));
            if (cur > nw) {
                bchsupply.className = "supply red";
            } else if (cur < nw) {
                bchsupply.className = "supply green";
            } else {
                bchsupply.className = "supply black";
            }
            bchsupply.innerText = data.cmc_bch.supply;

        },
        error: function(error_data) {

        }
    });
};

setInterval(updateCMC, 60 * 1000);