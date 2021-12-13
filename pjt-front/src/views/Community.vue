<template>
<div class="buster-light">

<div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					
					<h1>Community</h1>
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
          <review-item v-for="(review, index) in reviews" :key="index" :review="review"></review-item>				
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

const api = 'http://127.0.0.1:8000/api/v1/community/review/'


export default {
  components: { 
    CommunitySidebar,
    ReviewItem,
		// InfiniteLoading 
  },
  name: 'Community',
  data () {
    return {
      reviews: [],
    }
  },
	methods: {
    getReviews () {      
      axios({
				method: 'get',
				url: api
			})
				
				.then((res) => {   
        
        if (res.data.length) {
          // this.page += 1;
          // this.$store.dispatch('getMovies', this.page)
					// console.log(res.data)
          this.reviews = res.data
          // $state.loaded();
					// console.log(this.reviews)
        } else {
          // $state.complete();
        }

      });
    }
  },
	created () {
		this.getReviews()		
	}
}
</script>

<style scoped>
.grid { 
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 20px;
  align-items: stretch;
  }
.grid > article {
  border: 1px solid #ccc;
  box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);
}
.grid > article img {
  max-width: 100%;
}
.text {
  padding: 0 20px 20px;
}
.text > button {
  background: gray;
  border: 0;
  color: white;
  padding: 10px;
  width: 100%;
  }
</style>