<template>
  <!-- <div class="video-container"> -->
    <iframe :src="url" frameborder="0" id="video" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
  <!-- </div> -->
</template>

<script>
export default {
  name: 'MovieTrailer',
  props: {
    url: String
  }
}
</script>

<style scoped>
  .video-container { 
    /* position: relative; */
    /* overflow: hidden; */
    /* padding-top: 56.25%; */

  }
  #video {   
    /* display: block;   
    border: none;   
    height: 60vh;
    width: 70vw; */
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }
</style>