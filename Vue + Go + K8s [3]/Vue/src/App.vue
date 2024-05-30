<script setup>
import { ref } from 'vue';
import GetButton from './components/GetButton.vue';
import HotelTable from './components/HotelTable.vue';
import RoomTable from './components/RoomTable.vue';

const hotels = ref([]);
const rooms = ref([]);

function updateResults(type, data) {
  if (type === 'Hotel') {
    console.log(data);
    hotels.value = data;
  } else if (type === 'Room') {
    console.log(data);
    rooms.value = data;
  }
}
</script>

<template>
  <div>
    <h2>Hotel List</h2>
    <GetButton type="Hotel" @hotel-retrieved="updateResults"></GetButton>
    <HotelTable :data="hotels" v-if="hotels.length"></HotelTable>
  </div>

  <br>

  <div>
    <h2>Room List</h2>
    <GetButton type="Room" @room-retrieved="updateResults"></GetButton>
    <RoomTable :data="rooms" v-if="rooms.length"></RoomTable>
  </div>

</template>

<style>
</style>
