const url = '/devices';
const sensor = (
    () => {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                values = JSON.parse(data)[0].fields
                console.log(JSON.stringify(values));
                document.getElementById("data").innerHTML = JSON.stringify(values);
                if(values.sensor_1 == "ligado")
                    document.getElementById("image").src = "/static/sensors_connected.png"
            
                else document.getElementById("image").src = "/static/sensors_disconnected.png"
            })
            .catch(error => console.error('There was a problem with the fetch operation:', error));
    }
);
setInterval(() => {
    sensor();
}, 500);