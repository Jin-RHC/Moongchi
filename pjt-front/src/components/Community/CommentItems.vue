<template>
  <!-- comment items -->
  <div class="comments">
    <h4 v-show="messageInfo.length">{{ messageInfo.length }} Comments</h4>

    <div class="cmt-item" v-for="(data, index) in messageInfo" :key="index">
      <!-- <img src="images/uploads/author.png" alt=""> -->
      <div class="author-infor">
        <div class="flex-it2">
          <h6><a href="#">user</a></h6> <span class="time"> - 27 Mar 2017</span>
        </div>
        <div class="flex-it2">
          <p style="white-space: pre-line;">{{ data.message }}</p>
        </div>
        <div style="display: block; float: right;">          
            <a style="" href=""><font-awesome-icon :icon="['far', 'thumbs-up']" />0</a>          
					  <a style="margin-left: 15px;" href=""><font-awesome-icon :icon="['far', 'thumbs-down']" />0</a>         
        </div>
        
        <div class="row">
          <p><a @click.prevent="isCommentForm = !isCommentForm" class="rep-btn" href="#">+ Reply</a></p>
        </div>
      </div>
      <div v-if="commentChild">
        <div v-for="i in 2" :key="i.i" class="reply" style="">
          <!-- <img src="images/uploads/author2.png" alt=""> -->
          <div class="author-infor">
            <div class="flex-it2">
              <h6><a href="#">Joss Whedon</a></h6> <span class="time"> - 27 Mar 2017</span>
            </div>
            <p style="white-space: pre-line;">Prince died not long after the 2016 Rock Hall ceremony, so this year's edition featured Lenny Kravitz and a full gospel choir performing a swamp-funk take on When Doves Cry.</p>
            <div style="display: block; float: right;">          
              <a style="" href=""><font-awesome-icon :icon="['far', 'thumbs-up']" />0</a>          
              <a style="margin-left: 15px;" href=""><font-awesome-icon :icon="['far', 'thumbs-down']" />0</a>         
            </div>          
          </div>
        </div>
      </div>
      <div v-if="isCommentForm">
        <comment-form></comment-form>  
      </div>   
      
    </div>

    <h4 v-show="!messageInfo.length" style="text-align: center;">등록된 댓글이 없습니다.</h4>

  </div>
</template>

<script>
import CommentForm from './CommentForm.vue'
export default {
  name: 'CommentItems',
  components: {
    CommentForm
  },
  props: {
    messageInfo: Array
  },
  data () {
    return {
      commentChild: true,
      isCommentForm: false,
    }
  },
  methods: {
    addComment () {

    }
  },
  watch: {
    messageInfo () {
      
    }
  }
}
</script>

<style>

</style>