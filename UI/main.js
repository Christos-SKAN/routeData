document.getElementById('request-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const from = document.getElementById('from').value;
    const to = document.getElementById('to').value;
    if (from && to) {
        const data = {origin: from, destination: to}
        try {
            fetch('http://' + location.host + '/routeData', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify(data)
            })
            .then(response => {return response.json()})
            .then(data => {
                document.querySelector('.infoL').textContent = "duration: " + data.duration + " distance: " + data.distance + " tolls: " + data.tolls + " ferry: " + data.ferry
                
            })
          } catch (error) {
            console.log('error', error);
          }
    };
  });