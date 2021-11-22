<template>
  <div id="app">
    <!--preloading-->
    <!-- <div id="preloader">
        <img class="logo" src="images/logo1.png" alt="" width="119" height="58">
        <div id="status">
            <span></span>
            <span></span>
        </div>
    </div> -->
    <!--end of preloading-->
    <login-form></login-form>
    <signup-form></signup-form>
    <Header/>
    <router-view/>
    <Footer/>
  </div>
</template>


<script>
import LoginForm from './components/Account/LoginForm.vue'
import SignupForm from './components/Account/SignupForm.vue'
import Footer from './components/Footer.vue'
import Header from './components/Header.vue'
export default {
  components: { 
    Header, 
    SignupForm, 
    LoginForm, 
    Footer 
  },  
}



</script>

<style>



</style>
