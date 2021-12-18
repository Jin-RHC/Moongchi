<template>
  <div id="app">
    <!--preloading-->
    <div id="preloader">
        <img class="logo" src="./assets/뭉치.png" alt="" style="border-radius : 30%">
        <div id="status">
            <span></span>
            <span></span>
        </div>
    </div>
    <!--end of preloading-->
    <!-- <login-form></login-form>
    <signup-form></signup-form> -->


      
      <Header/>
      <router-view :key="$route.fullPath" />
      <Footer/>


  </div>
</template>


<script>
// import LoginForm from './components/Account/LoginForm.vue'
// import SignupForm from './components/Account/SignupForm.vue'
// import LoginForm2 from './components/Account/LoginForm2.vue'
import Footer from './components/Footer.vue'
import Header from './components/Header.vue'
export default {
  components: { 
    // SignupForm, 
    // LoginForm, 
    Footer,
    Header,

  },
  data () {
    return {
      clickLogin: true
    }
  },
  methods: {  
    // showModal () {
    //   this.$modal.show(
    //   LoginForm2,  
    //   { text: 'This text is passed as a property' },
    //   { draggable: true,
    //     adaptive: true,
    //     resizable: true,
    //     width: '400',
    //     height: '620',
    //     overlayTransition: 'opacity'
    //     },
    //   )
    // },
  }
} 


</script>

<style>



</style>
