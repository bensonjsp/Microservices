<template>
    <button v-on:click="getInfo()">Get {{ type }}</button>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            required: true
        }
    },
    methods: {
        getInfo() {
            if (this.type == 'Hotel') {
                console.log('Retrieving hotel info');
                this.retrieveHotelInfo('Hotel');
            }
            else if (this.type == 'Room') {
                console.log('Retrieving room info');
                this.retrieveRoomInfo('Room');
            }
        },
        retrieveHotelInfo(hotel) {
            const response =
            fetch('http://localhost:5001/gethotel', {
                method: 'GET',
            })
                .then(response => response.json())
                .then(data => {
                    // console.log(response);
                    if (data.code === 404) {
                        console.log('No hotels found');
                    } else {
                        // console.log('Hotels found');
                        // console.log(data.data.hotels);
                        this.$emit('hotel-retrieved', hotel, data.data.hotels);
                    }
                })
                .catch(error => {
                    console.error('Error retrieving hotels:', error);
                });
        },
        retrieveRoomInfo(room) {
            fetch('http://localhost:5002/getroom', {
                method: 'GET',
            })
            .then(response => response.json())
            .then(data => {
                // console.log(response);
                if (data.code === 404) {
                    console.log('No rooms found')
                } else {
                    // console.log('Rooms found')
                    this.$emit('room-retrieved', room, data.data.rooms);
                }
            })
            .catch(error => {
                console.error('Error retrieving rooms:', error);
            });
        }
    },

}
</script>