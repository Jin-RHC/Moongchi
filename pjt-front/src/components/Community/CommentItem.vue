<template>
<div>

  <div style="display: flex; margin-top: 30px;">
    
    <div style="width: 100px;">
      <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: commentData.user.username }})" href=""><h6>{{ commentData.user.username }}</h6></a>
       
    </div>
    
    <p style="white-space: pre-line; width: 600px; padding: 0px">{{ commentData.content }}</p>
    <div style="">
      <div style="display: flex; justify-content: center;">
        <span style="" class="time">
          {{ commentData.created_at.slice(0, 10) + '   ' + commentData.created_at.slice(11, 19)}}
          <!-- 2000-01-15 -->
        </span>
        <a @click.prevent="deleteComment" href="" class="time" style="border: thin solid; height:50%">X</a>
      </div>
        <div style="display: flex; justify-content: end; margin-top:;">
          <a @click.prevent="reportComment" href=""><h6 class="time" style="margin-top: 5px; margin-right: 5px;">신고</h6></a>
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
        v-for="nestedComment in comment.nestedcomment_set" 
        :key="nestedComment.id"
        :nestedComment="nestedComment"
        :commentId="comment.id"
        @noti-nested-comment="notiNestedComment"        
      ></nested-comment-items>
    </div>    
  <a @click.prevent="openCommentForm" href="">답글</a>
  <form action="#" v-show="isNested">
   
    <div class="row">
      <div class="col-md-12">
        <textarea v-model.trim="nestedContent" name="message" id="" placeholder="주제와 무관한 댓글, 악플은 삭제될 수 있습니다."></textarea>
      </div>
    </div>
    <div style="display: flex; justify-content: end;">
      <a @click.prevent="leaveNestedComment" placeholder="submit" href=""><button>등록</button></a>
    </div>
  </form>
  <hr>
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
      // nestedComments: this.comment.nestedcomment_set,
      commentData: this.comment,
      nestedComments: this.comment.nestedcomment_set,
      isNested: false,
      nestedContent: '',
      name: this.comment.user.username

    }
  },
  methods: {
    getData () {
      axios({
      method: 'get',
      url: api + `review/${this.$route.params.reviewId}/`,      
    })
      .then(res => {
        console.log(res.data)
        this.commentData = res.data.comment_set
      })
    },
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
        url: api + `${this.$route.params.reviewId}/comment/${this.commentData.id}/like/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment-like')
          // this.getData()
        })
        .catch(err => {
          console.log(err)
          alert('로그인이 필요합니다.')
        })
    },
    dislikeComment () {
      axios({
        method: 'post',
        url: api + `${this.$route.params.reviewId}/comment/${this.commentData.id}/dlike/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment-dislike')
          // this.getData()
        })
        .catch(err => {
          console.log(err)
          alert('로그인이 필요합니다.')
        })

    },
    deleteComment () {
      axios({
        method: 'delete',
        url: api + `${this.$route.params.reviewId}/comment/${this.commentData.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment-delete')
          // this.getData()          
        })
        .catch(err => {
          alert('댓글을 삭제할 권한이 없습니다.')
          console.log(err)
        })
    },
    notiNestedComment () {
      this.$emit('noti-nested-comment')

    },
    openCommentForm () {
      this.isNested = !this.isNested
    },
    leaveNestedComment () {
      
      if (this.nestedContent.length) {
        const nestedContent = {
          content: this.nestedContent
        }
        axios({
        method: 'post',
        url: api + `${this.comment.id}/nestedcomment/`,
        data: nestedContent,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.nestedContent = ''
          this.$emit('noti-nested-comment') 
        })
        .catch(err => {
          console.log(err)
          alert('답글을 작성할 권한이 없습니다.')
        })
      }
    },
    reportComment () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/reports/comment/' + `${this.comment.id}/`,        
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          alert('신고가 접수되었습니다.')
        })
        .catch(err => {
          console.log(err)
          alert('이미 신고된 댓글입니다.')
        })
    }
    
  
  },
  computed: {
    commentLike () {
      return this.comment.like_users.length
    },
    commentDislike () {
      return this.comment.dlike_users.length
    },
    // commentData () {
    //   return this.comment
    // }
  },
  // created () {
  //   this.getData()
  // }
   
}

</script>

<style>

</style>