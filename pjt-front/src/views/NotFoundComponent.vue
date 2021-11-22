<template>

<body>
<!--end of preloading-->

<div class="page-single-2">
	<div class="container">
		<div class="row">
			<div class="middle-content">
				<a href="index-2.html"><img class="md-logo" src="images/logo1.png" alt=""></a>
				<img src="images/uploads/err-img.png" alt="">
				<h1>Page not found</h1>
				<a @click.prevent="$router.push({ name: 'Home' })"  href="#" class="redbtn">go home</a>
			</div>
		</div>
	</div>
</div>
</body>

</template>

<script>
export default {
    name: 'NotFoundComponent',
}
</script>

<style>

</style>