<template>
<body>
  <div class="buster-light">
<div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					<h1>Hall of Fame</h1>
					<ul class="breadcumb">
						<li @click.prevent="$router.push({name: 'Home'})" class="active"><a href="#">Home</a></li>
						<li> <span class="ion-ios-arrow-right"></span> celebrities</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
<div class="page-single">
	<div class="container">
		<div class="row">
			<!-- <div class="col-md-12 col-sm-12 col-xs-12"> -->
        <celeb-item v-for="celeb in celebs" :key="celeb.id" :celeb="celeb"></celeb-item>

			<!-- </div> -->
		</div>
	</div>
</div>
		</div>
   
  
</body>
</template>

<script>
import axios from 'axios'
import CelebItem from '@/components/Celebs/CelebItem.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'Celebs',

  components: {
    CelebItem
  },
  data () {
    return {      
      celebs: [],
    }
  },
  methods: {

  },
  created () {
    axios({
      method: 'get',
      url: `${API}/api/v1/movies/celebs/`
    })
      .then((res) =>  {
        this.celebs = res.data
      })

  }

}
</script>

<style scoped>
body {
  overflow-y: scroll;
  scroll-behavior: smooth;
  scroll-snap-type: y mandatory;
}

section {
  scroll-snap-align: center;
}

</style>