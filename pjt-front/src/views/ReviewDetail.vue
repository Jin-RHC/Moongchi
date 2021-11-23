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
					<h1> 리뷰 제목 </h1>
          <div style="display: flex; justify-content: space-between;">
						        <star-rating :rating="3" :star-size="15" :read-only="true"></star-rating>

						<span class="right-it time" style="font-weight: bold; font-size: 1em;">조회 0 | 추천 0 | 댓글 0 </span>
          </div>
          <hr>
					<div style="display: flex; justify-content: space-between;">
						<span class="time" style=" font-weight: bold; font-size: 1em;">user</span><span class="time">2021-11-23</span>						
					</div>
					<br>

					<p>관련 영화: </p>
					<img src="images/uploads/blog-detail.jpg" alt="">
					<!-- <a href=""><font-awesome-icon :icon="['fas', 'thumbs-up']" /></a>
					<a href=""><font-awesome-icon :icon="['fas', 'thumbs-down']" /></a> -->
					

					<!-- <a href=""><font-awesome-icon :icon="['fas', 'star']" size="3x" :style="{ color: '' }" /></a> -->
					<div style="display: flex; justify-content: center;">
						<div style="display: flex; flex-direction: column;">
								<a href="" style=""><font-awesome-icon icon='arrow-up' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 13px; font-size: 1.5em;">0</div>
						</div>
						<div style="display: flex; flex-direction: column;">
								<a href="" style="margin-left: 20px;"><font-awesome-icon icon='arrow-down' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 33px; font-size: 1.5em;">0</div>
						</div>
							
						
					</div>
					<!-- share link -->
					<div class="flex-it share-tag">
						<div class="social-link">
							<h4>Share it</h4>
							<a href="#"><i class="ion-social-facebook"></i></a>
							<a href="#"><i class="ion-social-twitter"></i></a>
							<a href="#"><i class="ion-social-googleplus"></i></a>
							<a href="#"><i class="ion-social-pinterest"></i></a>
							<a href="#"><i class="ion-social-linkedin"></i></a>
						</div>
						<!-- <div class="right-it">
							<h4>Tags</h4>
							<a href="#">Gray,</a>
							<a href="#">Film,</a>
							<a href="#">Poster</a>
						</div> -->
					</div>
					<!-- comment items -->
					<comment-items :messageInfo="messageInfo"></comment-items>
					<!-- comment form -->
          <comment-form @get-message="deliverMessage"></comment-form>
					
					
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
import StarRating from 'vue-star-rating';


import CommentForm from '../components/Community/CommentForm.vue'
import CommentItems from '../components/Community/CommentItems.vue'
import CommunitySidebar from '../components/Community/CommunitySidebar.vue'
export default {
  components: { CommunitySidebar, CommentItems, CommentForm, StarRating },
  name: 'ReviewDetail',
  data () {
    return {
      messageInfo: [],
			data: null,
    }
  },
  methods: {
    deliverMessage (messageInfo) {
      this.messageInfo.push(messageInfo)
    }
  },	
}
</script>

<style scoped>
#cm { position:absolute; } 
.hc { width:200px; 
			left:0; right:0; 
			margin-left:auto; 
			margin-right:auto; 
		} 

.vc { 
			height:40px; 
			top: 0; 
			bottom:0; 
			margin-top:auto; 
			margin-bottom:auto; 
		} 



</style>