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
export default {
  name: 'LoginForm',
  data () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/accounts/api/token/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.access)          
          this.$router.go()
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

}
</script>

<style scoped>



</style>