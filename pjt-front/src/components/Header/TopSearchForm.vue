<template>
  <!-- top search form -->
  <div class="top-search">
    <select v-model="category">
      <option value="movies">영화</option>
      <option value="others">기타</option>
    </select>
    <!-- <input @input="search" @keydown.enter="search" :value="searchKeyword" @input="changeKeyword" type="text" placeholder="검색어를 입력해 주세요"> -->
    <input @keydown.enter="searchEnter" :value="searchKeyword" @input="changeKeyword" type="text" placeholder="검색어를 입력해 주세요">
    </div>
</template>

<script>
export default {
  name: 'TopSearchForm',
  data () {
    return {
      category: 'movies',
      searchKeyword: null,
    }
  },
  methods: {
    search () {
      if (this.category === 'movies') {
        this.searchMovie()
      } else {
        this.searchReview()
      }
    },    
    searchMovie () {
      if (this.searchKeyword.trim().length >= 1) {
        this.$router.push({ name: 'MovieListSearch', query: {query: `${this.searchKeyword}` }}).catch(()=>{})        
      } 
      // this.searchKeyword = null    
      
    },
    searchReview () {
      if (this.searchKeyword.trim().length) {
        this.$router.push({ name: 'CommunitySearch', query: {query: `${this.searchKeyword}` }}).catch(()=>{})
      } 
      // this.searchKeyword = null     
      
    },
    searchEnter () {
      this.searchKeyword = null
    }, 


    changeKeyword (e) {
      this.searchKeyword = e.target.value
      this.search(this.searchKeyword)
      // if (this.searchKeyword.length >= 2) {
      //   this.search(this.searchKeyword)
      // }
    }
  }
}
</script>

<style>

</style>