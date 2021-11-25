<template>
  <div class="row">
        <div class="rv-hd">
          <!-- <div class="div">
            <h3>Related Movies To</h3>
          <h2>Skyfall: Quantum of Spectre</h2>
          </div> -->
          <div style="display: flex; flex-direction: row-reverse; margin-bottom: 1em;">
            <a @click.prevent="$router.push({ name: 'ReviewForm', params:{title: movie.title, id: movie.id }})" href="#" class="redbtn">Write Review</a>
            <!-- <router-link :to="{ name: 'ReviewForm', params: { title: `${movie.title}`, movieId: `${movie.id}` }}" class="redbtn">Write Reivew</router-link> -->
          </div>
        </div>
        <div class="topbar-filter">
    <p>Found <span>56 reviews</span> in total</p>
    <label>Filter by:</label>
    <select>
      <option value="popularity">Popularity Descending</option>
      <option value="popularity">Popularity Ascending</option>
      <option value="rating">Rating Descending</option>
      <option value="rating">Rating Ascending</option>
      <option value="date">Release date Descending</option>
      <option value="date">Release date Ascending</option>
    </select>
  </div>
  <div class="mv-user-review-item">
    <div class="user-infor">
      <!-- <img src="images/uploads/userava1.jpg" alt=""> -->
      <div>
        <h3>Best Marvel movie in my opinion</h3>
        <!-- <div class="no-star" style="margin-top: 20px;">
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star"></i>
          <i class="ion-android-star last"></i>
        </div> -->
        <p class="time" style="display: flex; margin-top: 10px; width: 95%;">
          <a href="#" style="margin-left:20px"> <h6> user     </h6> </a>
           <span style="margin-left: 50px;"> | 2016-11-20 </span>
        </p>
      </div>
    </div> 
    
    <p style="width: 95%;">This is by far one of my favorite movies from the MCU. The introduction of new Characters both good and bad also makes the movie more exciting. giving the characters more of a back story can also help audiences relate more to different characters better, and it connects a bond between the audience and actors or characters. Having seen the movie three times does not bother me here as it is as thrilling and exciting every time I am watching it. In other words, the movie is by far better than previous movies (and I do love everything Marvel), the plotting is splendid (they really do out do themselves in each film, there are no problems watching it more than once.</p>
    <hr>
  </div>
  

      </div>
</template>

<script>
// import axios from 'axios'

// const api = 'http://127.0.0.1:8000/api/v1/community/'
// const id = this.$route.params.id

export default {
  name: 'MovieReview',
  data () {
    return {
      review: null,
    }
  },
  props: {
    movie: Object
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

  } 
}
</script>

<style>

</style>