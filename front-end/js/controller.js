console.log(12);
setInterval(() => {
    $.getJSON("https://io.adafruit.com/Jackson25092002/feeds/bbc-temp", function (data) {
        console.log(data.last_value);
        document.getElementById("temp").innerHTML = data.last_value + "℃";
    });
    $.getJSON("	https://io.adafruit.com/Jackson25092002/feeds/bbc-water", function (data) {
        console.log(data.last_value);
        if (data.last_value == "OPEN")
            document.getElementById("water").checked = true;
        else document.getElementById("water").checked = false;
    });
    $.getJSON("https://io.adafruit.com/api/v2/hjilklong/feeds/bbc-led", function (data) {
        console.log(data.last_value);
        if (data.last_value == "ON")
            document.getElementById("light").checked = true;
        else document.getElementById("light").checked = false;
    });
}, 5000);

function Led() {
    if (document.getElementById('led').checked) {
        $.ajax({
            url: "https://io.adafruit.com/Jackson25092002/feeds/bbc-led/data",
            dataType: "json",
            type: "post",
            headers: {
                'Content-Type': 'application/json',
                'Content-Type': 'application/json',
                'X-AIO-Key': 'aio_zcpq66VhoobW2X57E1LqDxJ00fLn'
            },
            data: JSON.stringify({"value": "ON"}),
            processData: false,
            success: function (data, textStatus, jQxhr) {
                //alert('ONN');
            },
            error: function (jQxhr, textStatus, errorThrown) {
                console.log(errorThrown);
            },
        })
    } else {
        $.ajax({
            url: "https://io.adafruit.com/api/v2/hjilklong/feeds/bbc-led/data",
            dataType: "json",
            type: "post",
            headers: {
                'Content-Type': 'application/json',
                'Content-Type': 'application/json',
                'X-AIO-Key': 'aio_zcpq66VhoobW2X57E1LqDxJ00fLn'
            },
            data: JSON.stringify({ "value": "OFF" }),
            processData: false,
            success: function (data, textStatus, jQxhr) {
                //alert('ONN');
            },
            error: function (jQxhr, textStatus, errorThrown) {
                console.log(errorThrown);
            },
        })

    }
}

function Water() {
    if (document.getElementById('water').checked) {
        $.ajax({
            url: "https://io.adafruit.com/Jackson25092002/feeds/bbc-water/data",
            dataType: "json",
            type: "post",
            headers: {
                'Content-Type': 'application/json',
                'Content-Type': 'application/json',
                'X-AIO-Key': 'aio_zcpq66VhoobW2X57E1LqDxJ00fLn'
            },
            data: JSON.stringify({"value": "ON"}),
            processData: false,
            success: function (data, textStatus, jQxhr) {
                //alert('ONN');
            },
            error: function (jQxhr, textStatus, errorThrown) {
                console.log(errorThrown);
            },
        })
    } else {
        $.ajax({
            url: "https://io.adafruit.com/Jackson25092002/feeds/bbc-water/data",
            dataType: "json",
            type: "post",
            headers: {
                'Content-Type': 'application/json',
                'Content-Type': 'application/json',
                'X-AIO-Key': 'aio_zcpq66VhoobW2X57E1LqDxJ00fLn'
            },
            data: JSON.stringify({ "value": "OFF" }),
            processData: false,
            success: function (data, textStatus, jQxhr) {
                //alert('ONN');
            },
            error: function (jQxhr, textStatus, errorThrown) {
                console.log(errorThrown);
            },
        })

    }
}
