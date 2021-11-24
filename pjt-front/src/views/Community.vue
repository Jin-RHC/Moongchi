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


        <!-- <ul class="pagination">
          <li class="icon-prev"><a href="#"><i class="ion-ios-arrow-left"></i></a></li>
          <li class="active"><a href="#">1</a></li>
					<li><a href="#">2</a></li>
					<li><a href="#">3</a></li>
					<li><a href="#">4</a></li>
					<li><a href="#">...</a></li>
					<li><a href="#">21</a></li>
					<li><a href="#">22</a></li>
					<li class="icon-next"><a href="#"><i class="ion-ios-arrow-right"></i></a></li>
        </ul> -->
			</div>


			<div class="col-md-3 col-sm-12 col-xs-12" style="position: sticky; top: 100px">
        <community-sidebar></community-sidebar>
		
			</div>
		</div>
	</div>
</div>
<!--end of  blog grid section-->
		</div>
</template>

<script>
import axios from 'axios'
import CommunitySidebar from '../components/Community/CommunitySidebar.vue'
import ReviewItem from '../components/Community/ReviewItem.vue'

const api = 'http://127.0.0.1:8000/api/v1/community/review/'


export default {
  components: { 
    CommunitySidebar,
    ReviewItem 
  },
  name: 'Community',
  data () {
    return {
      reviews: [],
    }
  },
	methods: {
    getReiviews ($state) {      
      axios({
				method: 'get',
				url: api
			})
				
				.then((res) => {   
        
        if (res.data.length) {
          // this.page += 1;
          // this.$store.dispatch('getMovies', this.page)
          this.reviews.push(...res.data)
					console.log(this.reviews)
          $state.loaded();
        } else {
          $state.complete();
        }

      });
    }
  },
	created () {
		this.getReiviews()
	}
}
</script>

<style>

</style>