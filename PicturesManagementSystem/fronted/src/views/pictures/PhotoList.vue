<!--<template>-->

<!--<div class="demo-image">-->
<!--  <div class="block" v-for="img in imageList" :key="fit">-->
<!--    <span class="demonstration">{{ pic_name }}</span>-->
<!--    <el-image-->
<!--      style="width: 200px; height: 200px;"-->
<!--      :src=img.src-->
<!--      :fit="fit"></el-image>-->
<!--  </div>-->
<!--  </div>-->

<!--  </template>-->


<!--<script>-->
<!--  export default {-->
<!--    data() {-->
<!--      return {-->
<!--        pic_name:"hello",-->
<!--        fits: ['fill', 'fill', 'fill', 'fill', 'fill'],-->
<!--        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'-->
<!--      }-->
<!--    },-->

<!--    getImage() {-->
<!--              this.listLoading = true;-->
<!--              let self = this;-->
<!--              let headers = {Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))};-->
<!--              var uid = parseInt(JSON.parse(sessionStorage.getItem('uid')));-->

<!--             console.log(uid)-->
<!--              var params={uid:uid}-->
<!--              getImage(headers,params).then((res) => {-->
<!--                  self.listLoading = false;-->
<!--                  let {msg, code, data} = res;-->
<!--                  if (code === '999999') {-->
<!--                    // self.total = data.total;-->
<!--                      self.imgList = data.data;-->
<!--                      self.imgList.forEach(function (img) {// 因为要上传多个文件，所以需要遍历-->
<!--                          console.log(img["title"])-->
<!--                          img.src = "http://10.235.208.36:8000"+img["original"];-->
<!--                          img.title = img["title"];-->
<!--                          img.w = 1920;//这是大图的宽-->
<!--                          img.h = 1080;-->
<!--                      });-->
<!--                      console.log(this.imgList)-->
<!--                      console.log(this.slide1)-->
<!--                    }-->
<!--                  else {-->
<!--                      self.$message.error({-->
<!--                        message: msg,-->
<!--                        center: true,-->
<!--                      })-->
<!--                  }-->
<!--              })-->
<!--          },-->
<!--  }-->
<!--</script>-->
