<template>
     <div>

      <!-- 搜索框 -->
    <div>
     <el-input v-model="input"  size="small"  placeholder="请输入搜索的图片名称或分类名称"   style="width: 300px;margin-top:20px"></el-input>
      <el-button type="primary" size="small" @click="search">搜索</el-button>
    </div>
<!--    &lt;!&ndash; 搜索后的 &ndash;&gt;-->
<!--    <div v-if="searchData.length>0">-->
<!--      <ul v-for="(item, index) in searchData" :key="index">-->
<!--        <li>-->
<!--          <span>hello</span>-->

<!--        </li>-->
<!--      </ul>-->
<!--    </div>-->
<!--    &lt;!&ndash; 搜索前的 &ndash;&gt;-->
<!--    <div v-else>-->
<!--      <ul v-for="(item, index) in list" :key="index">-->
<!--        <li>-->
<!--          <span>hello</span>-->

<!--        </li>-->
<!--      </ul>-->
<!--    </div>-->

    <div>

        <el-upload
          :auto-upload="false"
          :file-list="fileList"
          :http-request="uploadSectionFile"
          :limit="3"
          :on-exceed="handleExceed"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          action=""
          class="upload-demo"
          list-type="picture"
          multiple
          ref="upload">
          <el-button size="small" slot="trigger" type="primary">上传图片</el-button>
          <el-button @click="submitUpload" size="small" style="margin-left: 10px;margin-top:23px" type="success">保存到服务器</el-button>
<!--          <el-button @click="getImage" size="small" style="margin-left: 10px;" type="success">查看图片列表</el-button>-->
          <el-table-column prop="imgList"></el-table-column>

          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>

        <vue-preview :slides="imgList"  @close="handleClose" class="preview"></vue-preview>



    </div>
       </div>
</template>

<script>
  import {
      uploadImg,getImage,searchImage
  }   from '../../api/api'
  export default {

      data() {
          return {
              input: "",
              fileList: [],
              imgList: [],
          }
      },
      methods: {

          uploadSectionFile(param) {
              this.fileList.push(param.file);
              console.log(this.fileList)

          },


          submitUpload() {
              this.$refs.upload.submit();
              if (this.fileList.length === 0) {
                  this.$message.error({
                      center: true,
                      message: "请选择文件"
                  })
                }
              else {
                  var form = new FormData();
                  let headers = {
                      "Content-Type": "application/json",
                      Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))
                  };
                  var uid = parseInt(JSON.parse(sessionStorage.getItem('uid')));
                  form.append('uid',uid)
                  this.fileList.forEach(function (file) {// 因为要上传多个文件，所以需要遍历

                      form.append('file', file);  //不要直接使用我们的文件数组进行上传，你会发现传给后台的是两个Object
                  });
                  console.log(form)
                  uploadImg(headers,form).then(_data => {

                      let {msg, code, data} = _data;
                      if (code === '999999') {
                          this.$message({
                              type: 'success',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else if (code === '999998') {
                          this.$message({
                              type: 'warning',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else if (code === '999996') {
                          this.$message({
                              type: 'warning',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else {
                          this.$message.error({
                              center: true,
                              message: msg
                          })
                      }
                  })

              }


          },

          handleRemove(file, fileList) {
                console.log(file, fileList);
          },
          handlePreview(file) {
                console.log(file);
          },

          handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
          },
          beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${file.name}？`);
          },


          handleClose() {
                console.log('close event')
          },


          getImage() {
              this.listLoading = true;
              let self = this;
              let headers = {Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))};
              var uid = parseInt(JSON.parse(sessionStorage.getItem('uid')));

             console.log(uid)

              var params={uid:uid}
              getImage(headers,params).then((res) => {
                  self.listLoading = false;
                  let {msg, code, data} = res;
                  if (code === '999999') {
                    // self.total = data.total;
                      self.imgList = data.data;
                      self.imgList.forEach(function (img) {// 因为要上传多个文件，所以需要遍历
                          console.log(img["title"])
                          img.src = img["original"];
                          img.alt = "picture1";
                          img.title = img["title"];
                          img.w = 1920;//这是大图的宽
                          img.h = 1080;
                      });
                      console.log(this.imgList)
                    }
                  else {
                      self.$message.error({
                        message: msg,
                        center: true,
                      })
                  }
              })
          },
        search() {
              this.listLoading = true;
              let self = this;
              let headers = {Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))};
              var uid = parseInt(JSON.parse(sessionStorage.getItem('uid')));
              var input=this.input
              var params={uid:uid,input:input}
              searchImage(headers,params).then((res) => {
                self.listLoading = false;
               let {msg, code, data} = res;
                      if (code === '999999') {
                          this.$message({
                              type: 'success',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else if (code === '999998') {
                          this.$message({
                              type: 'warning',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else if (code === '999996') {
                          this.$message({
                              type: 'warning',
                              center: true,
                              message: msg
                          })
                          this.$refs.upload.clearFiles()
                          this.fileList = []
                      }
                      else {
                          this.$message.error({
                              center: true,
                              message: msg
                          })
                      }
              })
          },



      },


    mounted() {
      this.getImage()
    }
  }

</script>



<style>
/*图片预览 缩略图*/
.preview figure {
  float: left;
  width: 300px;
  margin: 5px;
}

.preview figure img {
  width: 100%;
  height: 200px;
}

</style>
