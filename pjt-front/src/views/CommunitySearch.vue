<template>
<div class="buster-light">

<div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					
					<h1> Community - Reviews </h1>
					<ul class="breadcumb">
						<li @click.prevent="$router.push({name: 'Home'})" class="active"><a href="#">Home</a></li>
						<li><span class="ion-ios-arrow-right"></span> Community</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
<!-- blog grid section-->
<div class="page-single">
	<div class="container">
		<div class="row">
			<div class="col-md-9 col-sm-12 col-xs-12">
				<div class="row">
          <review-item v-for="(review, index) in reviews" :key="index" :review="review"></review-item>
				</div>        
			</div>


			<div class="col-md-3 col-sm-12 col-xs-12" style="position: sticky; top: 100px">
        <community-sidebar></community-sidebar>
		
			</div>
		</div>
	</div>
</div>
		<!-- <infinite-loading @infinite="getMovies"></infinite-loading> -->
		</div>
</template>

<script>
// import InfiniteLoading from 'vue-infinite-loading';
import axios from 'axios'
import CommunitySidebar from '../components/Community/CommunitySidebar.vue'
import ReviewItem from '../components/Community/ReviewItem.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { 
    CommunitySidebar,
    ReviewItem,
		// InfiniteLoading 
  },
  name: 'CommunitySearch',
  data () {
    return {
      reviews: [],
    }
  },
	methods: {
    getReview () {      
      axios({
				method: 'get',
				url: `${API}/api/v1/community/reviewsearch/${this.$route.query.query}/`
			})
				
				.then((res) => {   
          console.log(res)
          if (res.data.message === '검색 결과가 없습니다ㅠ') {
            // alert(`${res.data.message}`)
            // this.$router.push({ name: 'Community'})
          } else {
						this.reviews = res.data
					}       

      })
        

    },
  },
  created () {
    this.getReview()
  }
}
</script>

<style>

</style>