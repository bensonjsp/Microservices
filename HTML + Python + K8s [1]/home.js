// Function to retrieve the list of hotels
function getHotels() {
    const response =
    fetch('http://localhost:5001/gethotel', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {
            // console.log(response);
            if (data.code === 404) {
                console.log('No hotels found')
            } else {
                console.log(data);
                console.log(data.data.hotels);
                const hotels = data.data.hotels;
                // Populate the hotel table with data
                const hotelTableBody = document.getElementById('hotel-table-body');
                hotelTableBody.innerHTML = ''; // Clear existing data
                for (index in hotels) {
                    const hotel_row = document.createElement('tr');
                    hotel_row.innerHTML = `<td>${hotels[index].hotel_name}</td><td>${hotels[index].hotel_location}</td>`; // Add more columns as needed
                    hotelTableBody.appendChild(hotel_row);
                }

            }
        })
        .catch(error => {
            console.error('Error retrieving hotels:', error);
        });
}

// Function to retrieve the list of rooms
function getRooms() {
    fetch('http://localhost:5002/getroom', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        // console.log(response);
        if (data.code === 404) {
            console.log('No rooms found')
        } else {
            console.log(data);
            console.log(data.data.rooms);
            const rooms = data.data.rooms;
            // Populate the hotel table with data
            const roomTableBody = document.getElementById('room-table-body');
            roomTableBody.innerHTML = ''; // Clear existing data
            for (index in rooms) {
                const room_row = document.createElement('tr');
                room_row.innerHTML = `<td>${rooms[index].hotel_name}</td><td>${rooms[index].room_number}</td>
                                <td>${rooms[index].room_size}</td><td>${rooms[index].room_vacancy}</td>`; // Add more columns as needed
                roomTableBody.appendChild(room_row);
            }

        }
    })
    .catch(error => {
        console.error('Error retrieving rooms:', error);
    });
}