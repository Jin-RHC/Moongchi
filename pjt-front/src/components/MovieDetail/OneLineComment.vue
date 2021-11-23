<template>
    <!-- <h3>Best Marvel movie in my opinion</h3> -->
    <li style="display: flex; margin-top: 20px;">  

      <div>
        <star-rating :rating="oneLineComment.rating" :star-size="15" :read-only="true"></star-rating>
      </div>

      <div style="margin: 0 1em; width: 100%">
        
        <p style="white-space: pre-line;">{{ oneLineComment.content }}</p>
        
        <p class="time" >
          <a href="#" style="margin: 0 5px"> user </a> | <span style="margin: 0 5px;"> 2021.11.17 16:14 </span> | <a href="#" style="margin: 0 5px;">신고</a>
        </p>
        <div style="display: flex; justify-content: end;">
          <a @click.prevent="likeOneLineComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineCommentLike }}</strong> 
          </a>
          <a @click.prevent="dislikeOneLineComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineCommentDislike }}</strong> 
          </a>
        </div>
      <br>
      
      </div>
    </li>
</template>

<script>
import StarRating from 'vue-star-rating';

export default {
  name: 'OneLineComment',
  components: {
    StarRating

  },
  props: {
    oneLineComment: Object
  },
  data () {
    return {
      rating: 3,
      oneLineCommentLike: 0,
      oneLineCommentDislike: 0,
    }
  },
  methods: {
    likeOneLineComment () {
      this.oneLineCommentLike += 1
    },
    dislikeOneLineComment () {
      this.oneLineCommentDislike += 1
    }
  },
  computed: {

  }
}
</script>

<style>

</style>