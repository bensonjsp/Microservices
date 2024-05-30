<template>
  <table v-if="data.length" style="border: 1px solid black">
    <thead>
      <tr>
          <th style="font-weight: bold">Hotel Name</th>
          <th style="font-weight: bold">Room Number</th>
          <th style="font-weight: bold">Room Size</th>
          <th style="font-weight: bold">Vacancy</th>
      </tr>
    </thead>
    <tbody class="center">
      <tr v-for="room in data">
          <td>{{ room.hotel_name }}</td>
          <td>{{ room.room_number }}</td>
          <td>{{ room.room_size }}</td>
          <td>{{ room.room_vacancy }}</td>
      </tr>
    </tbody>
  </table>
</template>
  
<script>
export default {
    props: {
      data: {
        type: Array,
        required: true
      }
    }
};
</script>

<style>
.center{
  text-align: center;
}
</style>