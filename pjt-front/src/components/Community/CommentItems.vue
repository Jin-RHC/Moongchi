<template>
  <!-- comment items -->
  <div class="comments">
    
    <h4 v-show="comments.length">{{ comments.length }} Comments</h4>

    <div class="" style="margin-top: 30px;">
      <!-- <img src="images/uploads/author.png" alt=""> -->
      <comment-item 
        v-for="(comment, index) in comments" 
        :key="index" 
        :comment="comment"        
        @noti-like-comment="getReviewData"
        @noti-dislike-comment="getReviewData"
        @noti-nested-comment-like-dislike="getReviewData"
      ></comment-item>
      
      <div v-if="isCommentForm">
        <comment-form></comment-form>  
      </div>   
      
    </div>

    <h4 v-show="!comments.length" style="text-align: center;">등록된 댓글이 없습니다.</h4>
  </div>
</template>

<script>
import axios from 'axios'
import CommentForm from './CommentForm.vue'
import CommentItem from './CommentItem.vue'

const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  name: 'CommentItems',
  components: {
    CommentForm,
    CommentItem
  },
  props: {
    comments: Array
  },
  data () {
    return {      
      commentChild: true,
      isCommentForm: false,
      
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
    getReviewData () {
			axios({
				method: 'get',
				url: api + `review/${this.$route.params.reviewId}/`				
			})
				.then(res => {					
					this.comments = res.data.comment_set
				})
		},
    
  },
  computed: {
    
      
    }
}
</script>

<style>

</style>