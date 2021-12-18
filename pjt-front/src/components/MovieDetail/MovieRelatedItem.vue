<template>
  <div class="movie-item-style-2" style="">        
      <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
      <div :class="{'mv-item-infor': size}" style="padding: 1em 1em;">
        <h3 style="margin-bottom: 20px;"><a @click.prevent="$router.push({ name: 'MovieDetail', params: { id: movie.id }})" href="#">{{ movie.title }} <span>({{movie.release_date.slice(0, 4)}})</span></a></h3>
        <p class="rate"><i class="ion-android-star" style="color: #f5b50a; font-size: 22px; margin-right: 5px;"></i><span>{{Math.round(movie.rating_average * 10) / 10}}</span> /10</p>
        <p class="describe">{{ movie.overview.slice(0, 250)}}...</p>
        <div>          
          <p>Genres: <span v-for="genre in genresList" :key="genre.id">  {{ genre }} |</span></p>
          <p class="run-time">Release: {{movie.release_date}}</p>
          <p>Country: {{ movie.country }}</p>
          <p class="run-time">Popularity: {{movie.popularity}}</p>
        </div>
        <!-- <p>Stars: <a href="#">Robert Downey Jr.,</a> <a href="#">Chris Evans,</a> <a href="#">  Chris Hemsworth</a></p> -->
      </div>
    </div>
</template>

<script>
export default {
  name: 'MovieRelatedItem',
  props: {
    movie: Object
  },
  data () {
    return {
      size: true
    }
  },
  methods: {
    handler () {
      if (window.innerWidth <= 767) {
        this.size = false
      } else {
        this.size = true
      }
    }
  },
  computed: {
    genresList () {
      const data = []
      const genreData = {
        12: '모험',
        14: '판타지',
        16: '애니메이션',
        18: '드라마',
        27: '공포',
        28: '액션',
        35: '코미디',
        36: '역사',
        37: '서부',
        53: '스릴러',
        80: '범죄',
        99: '다큐멘터리',
        878: 'SF',
        9648: '미스터리',
        10402: '음악',
        10749: '로맨스',
        10751: '가족',
        10752: '전쟁',
        10770: 'TV 영화'
      }
      this.movie.genres.forEach(movieGenre => {
        data.push(genreData[movieGenre])
      })
      return data
    },
  },
  created () {
    this.handler()
  },
  mounted () {
    window.addEventListener('resize', this.handler)
  }
}
</script>

<style>

</style>