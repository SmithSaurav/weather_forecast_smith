function showPosition(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const locationInput = document.getElementById("location_input");
            locationInput.value = latitude + "," + longitude;
            locationInput.style.display = "block";
            const locationDropdown = document.getElementById("location");
            locationDropdown.selectedIndex = 0;
        }

        const locationDropdown = document.getElementById("location");
        const locationInput = document.getElementById("location_input");
        locationDropdown.addEventListener("change", function() {
            const latitude = this.options[this.selectedIndex].getAttribute("data-latitude");
            const longitude = this.options[this.selectedIndex].getAttribute("data-longitude");
            if (latitude && longitude) {
                locationInput.value = latitude + "," + longitude;
                locationInput.style.display = "block";
            } else {
                locationInput.value = "";
                locationInput.style.display = "none";
            }
        });