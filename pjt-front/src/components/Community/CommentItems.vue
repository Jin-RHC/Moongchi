<template>
  <!-- comment items -->
  <div class="comments">
    
    <h4 v-show="isComment">{{ commentsCount }} Comments</h4>

    <div class="" style="margin-top: 30px;">
      <!-- <img src="images/uploads/author.png" alt=""> -->
      <comment-item 
        v-for="(comment, index) in comments" 
        :key="index" 
        :comment="comment"        
        @noti-comment="getReviewData"
        :is-login="isLogin"
      ></comment-item>
      
      <div v-if="isCommentForm">
        <comment-form @noti-comment="getReviewData"></comment-form>  
      </div>   
      
    </div>

    <h4 v-show="!isComment" style="text-align: center;">등록된 댓글이 없습니다.</h4>
  </div>
</template>

<script>
// import axios from 'axios'
import CommentForm from './CommentForm.vue'
import CommentItem from './CommentItem.vue'

// const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  name: 'CommentItems',
  components: {
    CommentForm,
    CommentItem
  },
  props: {
    comments: Array,
    isLogin: Boolean
  },
  data () {
    return {      
      isCommentForm: false,
      commentsData: this.comments,
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
      this.$emit('noti-comment')
      this.$emit('noti-comment-count', this.commentsCount)			
		},

  },
  computed: {
    commentsCount () {
      if (this.comments) {
        let count = this.comments.length
        this.comments.forEach(comment => {
          count += comment.nestedcomment_set.length
        })
        return count
      } else {
        return 0
      }
    },
    isComment () {
      if (this.comments) {
        return true
      } else {
        return false
      }
    },    
  },
  created () {
    console.log(this.comments)
  }
}
</script>

<style>

</style>