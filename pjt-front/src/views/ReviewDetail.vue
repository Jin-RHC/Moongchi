<template>
		<div class="buster-light">

  <div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					<h1> Review detail</h1>
					<ul class="breadcumb">
						<li class="active"><a @click.prevent="$router.push({ name: 'Community' })" href="#">Community</a></li>
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
					<h1> {{ reviewTitle }} </h1>
          <div style="display: flex; justify-content: space-between;">
						<star-rating :rating="3" :star-size="15" :read-only="true"></star-rating>

						<span class="right-it time" style="font-weight: bold; font-size: 1em;">조회 0 | 추천 {{ item.like_users_count }} | 댓글 {{ commentsCount }} </span>
          </div>
          <hr>
					<div style="display: flex; justify-content: space-between;">
						<a @click.prevent="$router.push({ name: 'UserProfile', params: {username: author }})" href=""><div class="time" style=" font-weight: bold; font-size: 1em;">{{ author }}</div></a>
						<span class="time">{{ createdAt }} | <a @click.prevent="reportReview" href=""><span class="time"> 신고 </span></a></span>
					</div>					
					<br>

					<p>관련 영화: <a @click.prevent="$router.push({ name: 'MovieDetail', params: {id: item.movie.id }})" href=""> {{ movieTitle }} </a></p>
					<img :src="`https://image.tmdb.org/t/p/original${posterPath}`" alt="">
					<!-- <a href=""><font-awesome-icon :icon="['fas', 'thumbs-up']" /></a>
					<a href=""><font-awesome-icon :icon="['fas', 'thumbs-down']" /></a> -->
					<p>{{ item.content }}</p>

					<!-- <a href=""><font-awesome-icon :icon="['fas', 'star']" size="3x" :style="{ color: '' }" /></a> -->
					<div style="display: flex; justify-content: center;">
						<div style="display: flex; flex-direction: column;">
								<a @click.prevent="addReviewLike" href="" style=""><font-awesome-icon icon='arrow-up' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 13px; font-size: 1.5em;">{{item.like_users_count}}</div>
						</div>
						<div style="display: flex; flex-direction: column;">
								<a @click.prevent="addReviewDislike" href="" style="margin-left: 20px;"><font-awesome-icon icon='arrow-down' size="3x" :style="{ color: '' }"/></a>
								<div style="display: inline; margin-left: 33px; font-size: 1.5em;">{{item.dlike_users_count}}</div>
						</div>
							
						
					</div>
					<!-- share link -->
					<div class="flex-it share-tag">
						<div class="social-link">
							<h4>Share it</h4>
							<a href="https://ko-kr.facebook.com/zuck"><i class="ion-social-facebook"></i></a>
							<a href="https://twitter.com/jack"><i class="ion-social-twitter"></i></a>
							<a href="https://www.pinterest.co.kr/"><i class="ion-social-pinterest"></i></a>
							<a href="https://kr.linkedin.com"><i class="ion-social-linkedin"></i></a>
						</div>
						<span v-if="same">
							<a @click.prevent="updateReview" href=""><button class="redbtn" style="background:grey;">수정</button></a>
							<a @click.prevent="deleteReview" href=""><button class="redbtn">삭제</button></a>
						</span>
					</div>
					<!-- comment items -->
					<comment-items :comments="item.comment_set" :is-login="isLogin" @noti-comment="getData" @noti-comment-count="getCommentsCount"></comment-items>
					<!-- comment form -->
          <comment-form v-show="isLogin" @noti-comment="getData"></comment-form>
					<textarea type="text" placeholder="로그인이 필요합니다." disabled v-show="!isLogin" style="margin-top: 20px;"></textarea>
					
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
import jwt_decode from "jwt-decode";

import CommentForm from '../components/Community/CommentForm.vue'
import CommentItems from '../components/Community/CommentItems.vue'
import CommunitySidebar from '../components/Community/CommunitySidebar.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { CommunitySidebar, CommentItems, CommentForm, StarRating },
  name: 'ReviewDetail',
  data () {
    return {
			item: [],
			commentsCount: 0,
			isLogin: false,
			same: false,
			author: null,
			createdTime: null,
			reviewTitle: '',
			movieTitle: '',
			posterPath: ''
    }
  },
  methods: {
		getData () {
			axios({
				method: 'get',
				url: `${API}/api/v1/community/review/${this.$route.params.reviewId}/`				
			})
				.then(res => {
					this.item = res.data
					this.comments = res.data.comment_set
					this.content = res.data.content
					this.author = res.data.user.username
					this.createdTime = res.data.updated_at
					this.reviewTitle = res.data.title
					this.movieTitle = res.data.movie.title
					this.posterPath = res.data.movie.poster_path
					console.log(this.item)
					const token = this.$store.state.token
					const decoded = jwt_decode(token)
					// console.log(this.isLogin)
					if (decoded) {
						this.isLogin = true
						if (decoded.username === this.item.user.username) {
							this.same = true
						} else {
							this.same = false
						}
					} else {
						this.isLogin = false
					}			
					return

					// console.log(this.isLogin)
					})
				.catch(err => {
					console.log(err)
					this.$router.push({ name: 'Home'})
					// alert('존재하지 않는 게시물입니다.')
				})
		},    
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
        url: `${API}/api/v1/community/${this.item.movie.id}/review/${this.$route.params.reviewId}/like/`,        
        headers: this.setToken()
      })
				.then(res => {
					console.log(res)
					this.getData()
				})
				.catch(err => {
					console.log(err)
					alert('로그인이 필요합니다.')
				})

		},
		addReviewDislike () {
			axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.item.movie.id}/review/${this.$route.params.reviewId}/dlike/`,        
        headers: this.setToken()
      })
				.then(res => {
					console.log(res)
					this.getData()
				})
				.catch(err => {
					console.log(err)
					alert('로그인이 필요합니다.')
				})
		},		
		deleteReview () {
			axios({
				method: 'delete',
				url: `${API}/api/v1/community/${this.item.movie.id}/review/${this.$route.params.reviewId}/`,
				headers: this.setToken()				
			})
				.then(res => {
					console.log(res)
					this.$router.push({ name: 'Community'})
				})
				.catch(err => {
					console.log(err)
					alert('삭제할 권한이 없습니다.')
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
		},
		reportReview () {
			axios({
				method: 'post',
				url: `${API}/api/v1/reports/review/${this.$route.params.reviewId}/`,
				headers: this.setToken()				
			})
				.then(res => {
					console.log(res)
					alert('신고가 접수되었습니다.')
				})
				.catch(err => {
					console.log(err)
					alert('이미 신고한 게시물입니다.')
				})
		},
		getCommentsCount (data) {
			this.commentsCount = data
		},
		checkLogin () {
			const token = this.$store.state.token
			const decoded = jwt_decode(token)
			// console.log(this.isLogin)
			if (decoded) {
				this.isLogin = true								
			} else {
				this.isLogin = false
			}			
			return			
		}


  },	
	created () {	
		this.getData()		
	},	
	computed: {
    createdAt () {
			let dataTime = ''
			if (this.createdTime) {
				dataTime = this.createdTime.slice(0, 10) + '   ' + this.createdTime.slice(11, 19)
			}
      return dataTime
    },
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