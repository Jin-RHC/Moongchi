<template>
  <div class="row">
        <div class="rv-hd">
          <!-- <div class="div">
            <h3>Related Movies To</h3>
          <h2>Skyfall: Quantum of Spectre</h2>
          </div> -->
          <div v-show="isLogin" style="display: flex; flex-direction: row-reverse; margin-bottom: 1em;">
            <a @click.prevent="$router.push({ name: 'ReviewForm', params:{movieTitle: movie.title, movieId: movie.id }})" href="#" class="redbtn">Write Review</a>
            <!-- <router-link :to="{ name: 'ReviewForm', params: { title: `${movie.title}`, movieId: `${movie.id}` }}" class="redbtn">Write Reivew</router-link> -->
          </div>
        </div>
  <p v-if="!isLogin">
    <span class="time" style="font-size: 20px;">로그인이 필요한 페이지입니다.</span>
  </p>
  <div v-else class="topbar-filter">
    <p>Found <span>{{ reviews.length }} reviews</span> in total</p>
    <label>Filter by:</label>
    <select disabled>
      <option value="popularity">Popularity Descending</option>
      <option value="popularity">Popularity Ascending</option>
      <option value="rating">Rating Descending</option>
      <option value="rating">Rating Ascending</option>
      <option value="date">Release date Descending</option>
      <option value="date">Release date Ascending</option>
    </select>
  </div>
  <div class="mv-user-review-item" v-for="review in reviews" :key="review.id">
    <div class="" style="">
      <!-- <img src="images/uploads/userava1.jpg" alt=""> -->
      <div>
      <div>
        <div class="no-star" style="margin-top: 20px;">
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
        </div>
      </div>
      <div style="margin: 10px; 100px;">

        <a @click.prevent="$router.push({ name: 'ReviewDetail', params: { reviewId: review.id }})" href=""><h3>{{ review.title }}</h3></a>
      </div>
      </div>
    </div > 
      <div style="display: flex; margin-top: 20px;">

        <p class="time" style="display: flex; margin-top: 10px;">          
          <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: review.user.username }})" href="#" style="margin-left:20px"> <h6> {{ review.user.username }} </h6> </a>
          <span style="margin-left: 50px;"> {{ review.updated_at.slice(0, 10)}} {{ review.updated_at.slice(11, 16)}} </span>
        </p>
    
      </div>
    <!-- <p style="width: 95%;">This is by far one of my favorite movies from the MCU. The introduction of new Characters both good and bad also makes the movie more exciting. giving the characters more of a back story can also help audiences relate more to different characters better, and it connects a bond between the audience and actors or characters. Having seen the movie three times does not bother me here as it is as thrilling and exciting every time I am watching it. In other words, the movie is by far better than previous movies (and I do love everything Marvel), the plotting is splendid (they really do out do themselves in each film, there are no problems watching it more than once.</p> -->
    <hr>
  </div>
  

      </div>
</template>

<script>
import axios from 'axios'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'MovieReview',
  data () {
    return {
      reviews: [],
      isLogin: false
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
    getReview () {
      axios({
        method: 'get',
        url: `${API}/api/v1/community/${this.$route.params.id}/review/`,
        headers: this.setToken()
      })
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }

  },
  created () {
    this.getReview()
    if (this.$store.state.token) {
      this.isLogin = true
    }
  } 
}
</script>

<style>

</style>