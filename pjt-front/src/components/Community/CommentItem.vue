<template>
<div>

  <div style="display: flex;">
    <span></span>
    <div style="margin-right: 50px;">
      <h6><a @click.prevent="$router.push({ name: 'UserProfile', params: { username: comment.user.username }})" href="">{{ commentData.user.username }} </a></h6>
    </div>
    
    <p style="white-space: pre-line; width: 650px;">{{ commentData.content }}</p>
    <div style="">
      <span style="" class="time">{{ commentData.created_at.slice(0, 10) + '   ' + comment.created_at.slice(11, 19)}}</span> 
      <a @click.prevent="deleteComment" href="" class="time" style="border: thin solid;">X</a>
      <div style="display: flex; justify-content: end; margin-top: 20px;">
        <a @click.prevent="likeComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ commentLike }}</strong> 
        </a>
        <a @click.prevent="dislikeComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ commentDislike }}</strong> 
        </a>
      </div>
    </div>            
  </div>    
    <div v-show="nestedComments.length">
      <nested-comment-items 
        v-for="nestedComment in nestedComments" 
        :key="nestedComment.id"
        :nestedComment="nestedComment"
        :commentId="commentData.id"
        @noti-nested-comment-like="notiNestedComment"
        @noti-nested-comment-dislike="notiNestedComment"
      ></nested-comment-items>
    </div>    
</div>
</template>

<script>
import axios from 'axios'
import NestedCommentItems from './NestedCommentItems.vue'

const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  components: { NestedCommentItems },
  name: 'CommentItem',
  props: {
    comment: Object,
    
  },
  data () {
    return {
      nestedComments: this.comment.nestedcomment_set,
      commentData: this.comment
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
    likeComment () {
      axios({
        method: 'post',
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/like/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-like-comment')
        })
        .catch(err => {
          console.log(err)
        })
    },
    dislikeComment () {
      axios({
        method: 'post',
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/dlike/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-dislike-comment')
        })
        .catch(err => {
          console.log(err)
        })

    },
    deleteComment () {
      axios({
        method: 'delete',
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-dislike-comment')          
        })
        .catch(err => {
          alert('댓글을 지울 수 없습니다.')
          console.log(err)
        })
    },
    notiNestedComment () {
      this.$emit('noti-nested-comment-like-dislike')

    }
  },
  computed: {
    commentLike () {
      return this.comment.like_users.length
    },
    commentDislike () {
      return this.comment.dlike_users.length
    }
  }
}
</script>

<style>

</style>