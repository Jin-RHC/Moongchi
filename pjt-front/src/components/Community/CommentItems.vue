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
      ></comment-item>


      <!-- <div v-if="comment.nestedcomment_set.length">
        <div v-for="(nestedcomment, i) in comment.nestedcomment_set" :key="i" class="reply" style="">
          <div class="author-infor" style="display: flex; justify-content: space-between;">
            <h6><a href="#">{{ nestedcomment.user }}</a></h6>
            <p style="white-space: pre-line; width: 500px;">{{ nestedcomment.content }}</p>

            <div class="flex-it2">
               <span class="time"> {{ nestedcomment.created_at.slice(0, 10) + '   ' + nestedcomment.created_at.slice(11, 19)}}</span>
              <a @click.prevent="likeOneLineComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
                <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineCommentLike }}</strong> 
              </a>
              <a @click.prevent="dislikeOneLineComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
                <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineCommentDislike }}</strong> 
              </a>
            </div>                    
          </div>
        </div>
      </div> -->
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