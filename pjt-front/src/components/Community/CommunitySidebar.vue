<template>
  <div class="sidebar">
    <div class="sb-search sb-it">
      <h4 class="sb-title">Search</h4>
      <input @keydown.enter="searchReview" :value="searchKeyword" @input="changeKeyword" type="text" placeholder="Enter keywords">
    </div>
    <div class="sb-cate sb-it">
      <h4 class="sb-title">Categories</h4>
      <ul>
        <li><a href="#">전체 (50)</a></li>
        <li><a href="#">영화 리뷰 (38)</a></li>
        <li><a href="#">토론 (5)</a></li>
        <li><a href="#">자유 (7)</a></li>
        <!-- <li><a href="#"> (06)</a></li> -->
      </ul>
    </div>
    <div class="sb-recentpost sb-it">
      <h4 class="sb-title">most popular review</h4>
      <div class="recent-item">
        <span>01</span><h6><a href="#">Korea Box Office: Beauty and the Beast Wins Fourth</a></h6>
      </div>
      <div class="recent-item">
        <span>02</span><h6><a href="#">Homeland Finale Includes Shocking Death </a></h6>
      </div>
      <div class="recent-item">
        <span>03</span><h6><a href="#">Fate of the Furious Reviews What the Critics Saying</a></h6>
      </div>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios'
const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  name: 'CommunitySidebar',
  data () {
    return {
      searchKeyword: null,
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
        url: api + `review/`,
      })
      .then(res => {
        console.log(res)
        const topReview = res.data
        this.$emit('noti-community', topReview)
      })
      .catch(err => {
        console.log(err)
        // alert('검색에 실패했습니다.')
      })
    },
    changeKeyword (e) {
      this.searchKeyword = e.target.value
    }
  }
}
</script>

<style>

</style>