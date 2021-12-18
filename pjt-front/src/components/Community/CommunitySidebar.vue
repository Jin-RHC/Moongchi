<template>
  <div class="sidebar">
    <div class="sb-search sb-it">
      <h4 class="sb-title">Search</h4>
      <input @keydown.enter="searchReview" :value="searchKeyword" @input="changeKeyword" type="text" placeholder="Enter keywords">
    </div>
    <div class="sb-recentpost sb-it">
      <h4 class="sb-title">Most Popular Movies</h4>
     
        <div class="recent-item" v-for="(topMovie, idx) in topMovies" :key="idx">
          <span>{{`0${idx+1}`}}</span><h6><a @click.prevent="$router.push({ name: 'MovieDetail', params: {id: topMovie.id }})" href="#" style="white-space: pre-line; word-break:break-all; text-overflow: ellipsis; overflow: hidden;">{{ topMovie.title }}</a></h6>
          <h5>{{ Math.round(topMovie.rating_average * 10) / 10 }}</h5>
        </div>
     
    </div>
    <div class="sb-recentpost sb-it">
      <h4 class="sb-title">most popular review</h4>
      <li class="recent-item" v-for="(topReview, index) in topReviews" :key="index">
        <span>{{`0${index+1}`}}</span><h6><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: topReview.id }})" href="#" style="white-space: pre-line; word-break:break-all; text-overflow: ellipsis; overflow: hidden;">{{ topReview.title }}</a></h6>
      </li>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios'
const API = process.env.VUE_APP_BACKEND_URL
export default {
  name: 'CommunitySidebar',
  data () {
    return {
      searchKeyword: null,
      topReviews: null,
      topMovies: null,
    }
  },
  methods: {
    searchReview () {
      if (this.searchKeyword.length) {
        this.$router.push({ name: 'CommunitySearch', query: {query: `${this.searchKeyword}` }}).catch(()=>{})
      }      
      
    },
    getTopReview () {
      axios({
        method: 'get',
        url: `${API}/api/v1/community/sidebar-reviews/`,
      })
      .then(res => {
        // console.log(res.data)
        this.topReviews = res.data
        
      })
      .catch(err => {
        console.log(err)
        // alert('검색에 실패했습니다.')
      })
    },
    getTopMoives () {
      axios({
        method: 'get',
        url: `${API}/api/v1/community/sidebar-movies/`,
      })
        .then(res => {
          // console.log(res.data)
          this.topMovies = res.data
          
        })
        .catch(err => {
          console.log(err)
          // alert('검색에 실패했습니다.')
        })
    },
    changeKeyword (e) {
      this.searchKeyword = e.target.value
    }
  },
  created () {
    this.getTopReview()
    this.getTopMoives()
  },

}
</script>

<style>

</style>