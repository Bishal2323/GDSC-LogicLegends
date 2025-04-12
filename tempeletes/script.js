const navigateBtn = document.querySelector('#navigateBtn');
        
async function calculateRoute() {
    // const start = document.getElementById('current-location').value;
    // const end = document.getElementById('destination').value;
    // const directionsDiv = document.getElementById('directions');

    // // Reset directions container
    // directionsDiv.classList.remove('error-message', 'success-message');
    
    // if (!start || !end) {
    //     directionsDiv.innerHTML = "Please select both current location and destination!";
    //     directionsDiv.classList.add('error-message');
    //     directionsDiv.style.display = 'block';
    //     return;
    // }

    // if (start === end) {
    //     directionsDiv.innerHTML = "🎉 You're already at your destination!";
    //     directionsDiv.classList.add('success-message');
    //     directionsDiv.style.display = 'block';
    //     return;
    // }

        const response = await fetch('http://localhost:5000/navigate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start: "start",
                end: "end"
            })
        });

        const data = await response.json();
        console.log(data);
        // if (data.error) {
        //     directionsDiv.innerHTML = `❌ Error: ${data.error}`;
        //     directionsDiv.classList.add('error-message');
        // } else {
        //     directionsDiv.innerHTML = `
        //         <h3>Route from ${start} to ${end}:</h3>
        //         <p>${data.directions}</p>
        //         <p class="estimated-time">⏱ Estimated time: ${data.estimated_time}</p>
        //     `;
        //     directionsDiv.classList.add('success-message');
        // }
        // directionsDiv.style.display = 'block';

    
    // catch (error) {
    //     directionsDiv.innerHTML = "⚠️ Failed to connect to navigation service";
    //     directionsDiv.classList.add('error-message');
    //     directionsDiv.style.display = 'block';
    // }
}

navigateBtn.addEventListener('click', calculateRoute);