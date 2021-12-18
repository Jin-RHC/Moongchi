<template>
		<div class="buster-light">

  <div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					<h1> Review detail</h1>          
					<ul class="breadcumb">
						<li class="active"><a href="#">Community</a></li>
						<li> <span class="ion-ios-arrow-right"></span> Review </li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
<!-- Review detail section-->
<div class="page-single">
	<div class="container">
		<div class="row">
			<div class="col-md-9 col-sm-12 col-xs-12">
				<div class="blog-detail-ct">
          <h1 style="text-align: center;">{{ movieTitle }}</h1>		
        <hr>

        <form class="row">
          <div class="sb-search">
            <h4 for="exampleFormControlInput1" style="margin-bottom: 1em;">Review Title</h4>
            <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="리뷰 제목" v-model.trim="reviewTitle">
          </div>
          <br>
          <div class="form-group">
            <h4 for="exampleFormControlTextarea1" style="margin-bottom: 1em;">Review Content</h4>
            <textarea style="overflow-y: scroll;height: 250px; resize: none; font-size: 18px font-weight:500;" class="form-control" id="exampleFormControlTextarea1" rows="3" v-model.trim="reviewContent" placeholder="리뷰 내용"></textarea>
          </div>
          <br>
   
          <div class="modal-footer rv-hd">
            <a @click.prevent="$router.go(-1)" href="#" class="redbtn" style="background-color: #666;" >Close</a>

            <a v-show="!this.$route.params.reviewId" @click.prevent="addReview" href="#" class="redbtn" style="background-color: #3b4890; margin-left: 5px;">Create</a>
            <a v-show="this.$route.params.reviewId" @click.prevent="updateReview" href="#" class="redbtn" style="background-color: #3b4890; margin-left: 5px;">Edit</a>
          </div>
        </form>


				</div>
			</div>
			<div class="col-md-3 col-sm-12 col-xs-12" style="position: sticky; top: 100px;">
				<community-sidebar></community-sidebar>
			</div>
		</div>
	</div>
</div>
<!-- end of  blog detail section-->
		</div>
</template>

<script>
import axios from 'axios'
import CommunitySidebar from './CommunitySidebar.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { CommunitySidebar, },
  name: 'ReviewForm',
  data () {
    return {
      reviewTitle: this.$route.params.reviewId !== undefined ? this.$route.params.reviewTitle : "",
      reviewContent: this.$route.params.reviewId !== undefined ? this.$route.params.reviewContent : "",
      movieTitle: this.$route.params.movieTitle,
      movieId: this.$route.params.movieId
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    addReview () {
      if (this.reviewTitle && this.reviewContent) {
        const reviewData = {
          title: this.reviewTitle,
          content: this.reviewContent,       
        }
        axios({
          method: 'post',
          url: `${API}/api/v1/community/${this.$route.params.movieId}/review/`,
          data: reviewData,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res, '작성 성공!')
            this.$router.push({name: 'ReviewDetail', params: {reviewId: res.data.id}})
          })
          .catch(err => {
            console.log(err)
            this.$router.go(-2)
            alert('그렇게 길게 작성할 수 없습니다.')
          })
        
        this.reviewTitle = null
        this.reviewContent = null
        
        this.$router.push({ name: 'Community'})

      }
    },
    updateReview () {
      if (this.reviewTitle && this.reviewContent) {
        const reviewData = {          
          content: this.reviewContent,
          }

        axios({
          method: 'put',
          url: `${API}/api/v1/community/${this.$route.params.movieId}/review/${this.$route.params.reviewId}/`,
          data: reviewData,
          headers: this.setToken()
        })

          .then(res => {
            console.log(res)
            this.$router.push({name: 'ReviewDetail', params: {reviewId: this.$route.params.reviewId}})
        })
          .catch(err => {
            console.log(err)
            alert('수정할 권한이 없습니다.')
          })
    }
  }
  },
  created () {
    
  }
}
</script>

<style>
textarea {
height: 160px;
}
</style>