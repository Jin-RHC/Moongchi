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
          <h1 style="text-align: center;">{{ this.$route.params.title }}</h1>		
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
          <div class="form-group">
            <div class="form-check">
              <input class="form-check-input" type="radio" v-model="liked" value="true" name="liked_radio" id="defaultCheck1">
              <label class="form-check-label" for="defaultCheck1" >
                <span class="sb-title">
                  추천!
                </span>
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" v-model="liked" value="false" name="liked_radio" id="defaultCheck2">
              <label class="form-check-label" for="defaultCheck2">
                비추!!
              </label>
            </div>
          </div>
          <div class="modal-footer rv-hd">
            <a @click.prevent="$router.go(-1)" href="#" class="redbtn" style="background-color: #666;" >Close</a>
            <a @click.prevent="addReview" href="#" class="redbtn" style="background-color: #3b4890; margin-left: 5px;">Save</a>
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

import CommunitySidebar from './CommunitySidebar.vue'
export default {
  components: { CommunitySidebar, },
  name: 'ReviewForm',
  data () {
    return {      
      reviewTitle: null,
      reviewContent: null,
      liked: null,
    }
  },
  methods: {
    addReview () {
      if (this.reviewTitle && this.reviewContent && this.liked) {
        const reviewData = {
          title: this.reviewTitle,
          content: this.reviewContent,
          liked: this.liked,
          movieId: this.$route.params.movieId
        }
        // console.log(this.$route.params)
        this.$emit('deliver-review-data', reviewData)
        this.reviewTitle = null
        this.reviewContent = null
        this.liked = null
        this.$router.push({ name: 'Community', params: { datas: reviewData }})

      }
    }
  }
}
</script>

<style>
textarea {
height: 160px;
}
</style>