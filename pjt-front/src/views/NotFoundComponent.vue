<template>

<body>
<!--end of preloading-->

<div class="page-single-2">
	<div class="container">
		<div class="row">
			<div class="middle-content">
				<!-- <a href="index-2.html"><img class="md-logo" src="images/logo1.png" alt=""></a> -->
				<img src="images/uploads/err-img.png" alt="" style="margin-top: 200px;">
				<h1>페이지를 찾을 수 없습니다ㅠ</h1>
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