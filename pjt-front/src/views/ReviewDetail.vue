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
					<h1> {{ item.title }} </h1>
          <div style="display: flex; justify-content: space-between;">
						        <star-rating :rating="3" :star-size="15" :read-only="true"></star-rating>

						<span class="right-it time" style="font-weight: bold; font-size: 1em;">조회 0 | 추천 {{ item.like_users_count }} | 댓글 {{ item.comment_set.length }} </span>
          </div>
          <hr>
					<div style="display: flex; justify-content: space-between;">
						<a @click.prevent="$router.push({ name: 'UserProfile', params: {username: item.user.username }})" href=""><div class="time" style=" font-weight: bold; font-size: 1em;">{{ item.user.username }}</div></a>
						<span class="time">{{ createdAt }}</span>
					</div>
					<br>

					<p>관련 영화: <a @click.prevent="$router.push({ name: 'MovieDetail', params: {id: item.movie.id }})" href=""> {{ item.movie.title }} </a></p>
					<img :src="`https://image.tmdb.org/t/p/original${item.movie.poster_path}`" alt="">
					<!-- <a href=""><font-awesome-icon :icon="['fas', 'thumbs-up']" /></a>
					<a href=""><font-awesome-icon :icon="['fas', 'thumbs-down']" /></a> -->
					<p>{{ item.content }}</p>

					<!-- <a href=""><font-awesome-icon :icon="['fas', 'star']" size="3x" :style="{ color: '' }" /></a> -->
					<div style="display: flex; justify-content: center;">
						<div style="display: flex; flex-direction: column;">
								<a @click.prevent="addReviewLike" href="" style=""><font-awesome-icon icon='arrow-up' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 13px; font-size: 1.5em;">{{item.like_users.length}}</div>
						</div>
						<div style="display: flex; flex-direction: column;">
								<a @click.prevent="addReviewDislike" href="" style="margin-left: 20px;"><font-awesome-icon icon='arrow-down' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 33px; font-size: 1.5em;">{{item.dlike_users.length}}</div>
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
						<span>
							<a @click.prevent="updateReview" href=""><button>수정</button></a>
							<a @click.prevent="deleteReview" href=""><button>삭제</button></a>
						</span>
					</div>
					<!-- comment items -->
					<comment-items :comments="comments"></comment-items>
					<!-- comment form -->
          <comment-form v-show="isLogin" @noti-comment="getData"></comment-form>
					<textarea type="text" placeholder="로그인 하세요" disabled v-show="!isLogin"></textarea>
					
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
import axios from 'axios'

import CommentForm from '../components/Community/CommentForm.vue'
import CommentItems from '../components/Community/CommentItems.vue'
import CommunitySidebar from '../components/Community/CommunitySidebar.vue'

const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  components: { CommunitySidebar, CommentItems, CommentForm, StarRating },
  name: 'ReviewDetail',
  data () {
    return {
      comments: null,
			item: null,
			isLogin: false,

			content: null,

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
		addReviewLike () {
			 axios({
        method: 'post',
        url: api + `${this.item.movie.id}/review/${this.$route.params.reviewId}/like/`,        
        headers: this.setToken()
      })
				.then(res => {
					console.log(res)
					this.getData()
				})
				.catch(err => {
					console.log(err)
					alert('로그인하세요')
				})

		},
		addReviewDislike () {
			axios({
        method: 'post',
        url: api + `${this.item.movie.id}/review/${this.$route.params.reviewId}/dlike/`,        
        headers: this.setToken()
      })
				.then(res => {
					console.log(res)
					this.getData()
				})
				.catch(err => {
					console.log(err)
					alert('로그인하세요')
				})
		},
		getData () {
			axios({
				method: 'get',
				url: api + `review/${this.$route.params.reviewId}/`				
			})
				.then(res => {
					this.item = res.data
					this.comments = res.data.comment_set,
					this.content = res.data.content
				})
		},
		deleteReview () {
			axios({
				method: 'delete',
				url: api + `${this.item.movie.id}/review/${this.$route.params.reviewId}/`,
				headers: this.setToken()				
			})
				.then(res => {
					console.log(res)
					this.$router.push({ name: 'Community'})
				})
				.catch(err => {
					console.log(err)
					alert('삭제할 수 없습니다.')
				})
		},
		updateReview () {  
			this.$router.push(
				{ name: 'ReviewForm', 
					params: 
						{	reviewId: this.$route.params.reviewId, 
							movieTitle: this.item.movie.title, 
							movieId: this.item.movie.id,
							reviewTitle: this.item.title,
							reviewContent: this.item.content
						}
				}
			)
		}


  },
	created () {
		this.getData()
		if (this.$store.state.token) {
			this.isLogin = true
		}
	},
	computed: {
    createdAt () {
      return this.item.updated_at.slice(0, 10) + '   ' + this.item.updated_at.slice(11, 19)
    }
  }
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