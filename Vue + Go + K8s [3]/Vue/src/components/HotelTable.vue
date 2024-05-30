<template>
  <table v-if="data.length" style="border: 1px solid black">
    <thead>
      <tr>
          <th style="font-weight: bold">Hotel Name</th>
          <th style="font-weight: bold">Location</th>
      </tr>
    </thead>
    <tbody class="center">
      <tr v-for="hotel in data">
          <td>{{ hotel.hotel_name }}</td>
          <td>{{ hotel.hotel_location }}</td>
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
<!-- data.data.hotels returns this:
[
    {
        "hotel_id": 1,
        "hotel_location": "USA",
        "hotel_name": "Grand Plaza"
    },
    {
        "hotel_id": 2,
        "hotel_location": "Singapore",
        "hotel_name": "Marina Bay Sands"
    },
] -->