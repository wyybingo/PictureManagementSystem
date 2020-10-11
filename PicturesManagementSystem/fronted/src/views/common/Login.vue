<template>
  <div class="homeBox">

<!--    头部展示-->
     <div>
            <div class="title0">时光墙</div>
            <div class="title1">照片管理平台</div>

        </div>

<!-- 输入框外部边框设计-->

    <el-form :model="loginForm"   ref="LoginForm"  :rules="loginRule" label-position="left" label-width="0px" class="login-form">
      <div class="head-info">
                <label class="lbl-1"> </label>
                <label class="lbl-2"> </label>
                <label class="lbl-3"> </label>
            </div>

<!-- 输入框--交互部分-->
      <el-form-item prop="username">
        <input type="text"  v-model.trim="loginForm.username"  auto-complete="on"  placeholder="请输入用户名"  class="input" ></input>
      </el-form-item>

       <el-form-item prop="password">
        <input type="text"  v-model.trim="loginForm.password"  auto-complete="on"  placeholder="请输入密码" ></input>
      </el-form-item>

      <el-button  class="button red"  :loading="logining"  @click="submit">点击登录</el-button>
<!--  @click.native.prevent    给vue组件绑定事件时候，必须加上native ，不然不会生效（监听根元素的原生事件，使用 .native 修饰符）-->

    </el-form>
    </div>

</template>





<script>
  import { login} from '../../api/api';
    export default {
        name: "Login",
        data() {
            return{
                logining:false,   //登录按钮初始时不进行 loading
                loginForm:{     //
                    username:'',
                    password:''

                },
                loginRule:{
                    username: [
                        { required: true, message: '请输入账号', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' }
                    ]
                },
        }
          },
        methods:{
            submit(){
                this.$refs.LoginForm.validate((valid) => {    //先对输入进行校验
                    if (valid) {
                        this.logining = true;
                        var params={username: this.loginForm.username,
                                    password:this.loginForm.password};
                        login(params).then(_data => {  //请求接口
                            this.logining = false;
                            let { msg, code, data } = _data;  // 接口返回的为_data数据
                            // alert(_data);
                            console.log(_data);
                            if (code === '999999') {   //如果响应正确，则将用户名和token存到session中，data的json数据中有 first_name和key字段
                                sessionStorage.setItem('user_name', JSON.stringify(data.username));
                                sessionStorage.setItem('token', JSON.stringify(data.key));
                                sessionStorage.setItem('uid',JSON.stringify(data.uid))
                                console.log(this.$route.query.url);
                                if (this.$route.query.url) {   //查看url路由是否
                                    this.$router.push(this.$route.query.url);
                                } else {
                                    this.$router.push('/');  // ！！！！！之后要改这个
                                        }
                            } else {
                                this.$message.error({
                                    message: msg,
                                    center: true
                                })
                            }
                        });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }

      });
            },


         }
    }
</script>





<style lang="scss" scoped>

     .forgot  a{
  font-size: 13px;
  font-weight: 500;
  color: #F45B4B;
  display: inline-block;
  padding: 0px 7px 0px 0px;
}
.forgot  a:hover{
  color: #818181;
}
.forgot input[type="submit"] {
  background: #F45B4B;
  color: #FFF;
  font-size: 17px;
  font-weight: 400;
  padding: 8px 7px;
  width: 20%;
  display: inline-block;
  cursor: pointer;
  border-radius: 6px;
  -webkit-border-radius: 19px;
  -moz-border-radius: 6px;
  -o-border-radius: 6px;
  margin: 0px 20px 0px 0px;
  outline: none;
  border: none;
}
.forgot input[type="submit"]:hover {
	background:#818181;
	transition: 0.5s all;
  -webkit-transition: 0.5s all;
  -moz-transition: 0.5s all;
  -o-transition: 0.5s all;
}
.forgot {
  text-align: right;
  margin: 30px 20px 0px 0px;
}


    .input { padding: 5px; margin: 0; border: 1px solid #beceeb; }
    .clear { display: none; position: absolute; width: 16px; height: 16px; margin: 10% 0 20% 0; background: url('../../assets/close.png');}
    .input::-ms-clear { display: none; }
    .input:valid + .clear { display: inline; }

    .button.red {
      font-size: 30px;
      color: #fff;
      outline: none;
      border: none;
      background: #3ea751;
      width: 100%;
      padding: 18px 0;
      margin-top:30px;
      border-bottom-left-radius: 15px;
        -webkit-border-bottom-left-radius: 15px;
        -moz-border-bottom-left-radius: 15px;
        -o-border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        -webkit-border-bottom-right-radius: 15px;
        -moz-border-bottom-right-radius: 15px;
        -o-border-bottom-right-radius: 15px;
        cursor: pointer;
    }


    .button.red:hover {
        background: #ff6700;
        border-bottom-left-radius: 15px;
        -webkit-border-bottom-left-radius: 15px;
        -moz-border-bottom-left-radius: 15px;
        -o-border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        -webkit-border-bottom-right-radius: 15px;
        -moz-border-bottom-right-radius: 15px;
        -o-border-bottom-right-radius: 15px;
        transition: 1s all;
        -webkit-transition: 1s all;
        -moz-transition: 1s all;
        -o-transition: 1s all;
    }

    .homeBox {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0px;
        background: url('../../assets/bg1.jpg')  no-repeat;
        background-size: cover;
        overflow-y:auto;
        overflow-x:hidden;
    }




    .login-container {
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
      position: absolute;
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    /*margin: 180px auto;*/
      /*margin-top: 10%;*/
      /*right: 50px;*/
    width: 300px;
    padding: 35px 35px 15px 35px;
    background: #23305a;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
      z-index: 1000;
    float: right;
    right: 4%;
    top: 25%;
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #2ec0f6;
    }
    .remember {
      margin: 0px 0px 35px 0px;
        color: #eaeaea;
    }
    }
    .img-login {
        margin-top: -35%;
        width: 100%;
        height: auto;
    }
    .title0 {
        position: relative;
        width: 100%;
        margin: 5% auto 0 auto;
        text-align: center;
        color: #ff6700;
        font-size: 50px;
        line-height: 40px;
        z-index: 1000;
    }
    .title1 {
        position: relative;
        width: 100%;
        text-align: center;
        color: #EE7700;
        font-size: 30px;
        line-height: 100px;
        z-index: 1000;
    }
        .platform{
        position: relative;
        width: 100%;
        margin: 5% auto 0 auto;
        text-align: center;
        color: #ff6700;
        font-size: 40px;
        line-height: 40px;
        z-index: 1000;
    }
    .tyg-div {
        color: #2ec0f6;
        z-index: -1000;
        float: left;
        position: absolute;
        left: 5%;
        top: 20%;
        font-size: 30px;
        list-style-type:none
    }
    .lun-container{
        width: 210px;
        height:140px;
        position: relative;
        font-size: 32px;
        color: #FFFFFF;
        text-align: center;
        line-height: 90px;
        margin: 200px auto;
        margin-bottom: 0px;
        margin-top:48%;
        perspective: 1000px;
        z-index: 1000;
    }
    .carouse{
        transform-style:preserve-3d;

    }
    .carouse div{
        display: block;
        position: absolute;
        width: 140px;
        height: 90px;
    }

    .carouse .pic1{
        transform: rotateY(0deg) translateZ(160px);
    }
    .carouse .pic2{
        transform: rotateY(120deg) translateZ(160px);
    }
    .carouse .pic3{
        transform: rotateY(240deg) translateZ(160px);
    }

    /*=== 下一个动画 ===*/
    @keyframes to-scroll1 {
        0%{
            transform: rotateY(0deg);
        }

        33%{
            transform: rotateY(-120deg);

        }
        66%{
            transform: rotateY(-240deg);

        }
        100%{
            transform: rotateY(-360deg);

        }

    }
    #carouse1{
        animation: to-scroll1  10s ease infinite;
        /*animation-fill-mode: both;*/
    }

    body{
	background: url(../../assets/bg1.jpg) no-repeat 0px 0px;
	font-family: 'Open Sans', sans-serif;
	background-size:cover;
	-webkit-background-size:cover;
	-moz-background-size:cover;
	-o-background-size:cover;
	min-height:1050px;
    }

    .wrap{
        margin: 0 auto;
        width: 80%;
    }

    body a,form li,input[type="submit"],input[type="text"],.sixth-login input[type="submit"],.third-login input[type="submit"]{
        transition: 0.1s all;
        -webkit-transition: 0.1s all;
        -moz-transition: 0.1s all;
        -o-transition: 0.1s all;
    }


    /*--close--*/
    .close{
    background: url('../../assets/close.png') no-repeat 0px 0px;
      cursor: pointer;
      width: 20px;
      height: 20px;
      position: absolute;
      left: 20px;
      top: 20px;
      -webkit-transition: color 0.2s ease-in-out;
      -moz-transition: color 0.2s ease-in-out;
      -o-transition: color 0.2s ease-in-out;
      transition: color 0.2s ease-in-out;
    }
    /*--/close--*/
    h1 {
        font-family: 'Exo 2', sans-serif;
          text-align: center;
          padding-top: 4em;
          font-weight: 400;
          color: #2B2B36;
          font-size: 2em;
    }
    .login-form {
        background: #2b2b36;
        position: relative;
        width: 30%;
        margin:1% auto;
        text-align: center;
        border-radius: 15px;
        -webkit-border-radius: 15px;
        -moz-border-radius: 15px;
        -o-border-radius: 15px;
    }
    .head img {
        width: 100%;
    }

    .avtar img {
      margin: 2em 0 0;
    }
    #circle {
        width: 100px;
        height: 100px;
        background: red;
        -moz-border-radius: 50px;
        -webkit-border-radius: 50px;
        border-radius: 50px;
    }

    .logo img {
        margin: 2em 0 0;
        background-color: #ff6700;
        border-radius:10px;
    }

    .head-info {
      padding: 5px 0;
      text-align: center;
      font-weight: 600;
      font-size: 2em;
      color: #fff;
      background: #23232e;
      height: 50px;
        border-top-left-radius: 10px;
        -webkit-border-top-left-radius: 10px;
        -moz-border-top-left-radius: 10px;
        -o-border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        -webkit-border-top-right-radius: 10px;
        -moz-border-top-right-radius: 10px;
        -o-border-top-right-radius: 10p
    }
    input[type="text"] {
          width: 70%;
          padding: 1em 2em 1em 3em;
          color: #9199aa;
          font-size: 18px;
          outline: none;
          background: url(../../assets/adm.png) no-repeat 10px 15px;
          border: none;
          font-weight: 100;
          border-bottom: 1px solid#484856;
          margin-top: 2em;
    }
     input[type="password"]{
          width: 70%;
          padding: 1em 2em 1em 3em;
          color: #dd3e3e;
          font-size: 18px;
          outline: none;
          background: url(../../assets/key.png) no-repeat 10px 23px;
          border: none;
          font-weight: 100;
          border-bottom: 1px solid#484856;
     }
    .key {
       background: url(../../assets/pass.png) no-repeat 447px 17px;

    }
    input[type="submit"]{
      font-size: 30px;
      color: #fff;
      outline: none;
      border: none;
      background: #3ea751;
      width: 100%;
      padding: 18px 0;
      border-bottom-left-radius: 15px;
        -webkit-border-bottom-left-radius: 15px;
        -moz-border-bottom-left-radius: 15px;
        -o-border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        -webkit-border-bottom-right-radius: 15px;
        -moz-border-bottom-right-radius: 15px;
        -o-border-bottom-right-radius: 15px;
        cursor: pointer;
    }
    input[type="submit"]:hover {
        background:#ff6700;
        border-bottom-left-radius: 15px;
        -webkit-border-bottom-left-radius: 15px;
        -moz-border-bottom-left-radius: 15px;
        -o-border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        -webkit-border-bottom-right-radius: 15px;
        -moz-border-bottom-right-radius: 15px;
        -o-border-bottom-right-radius: 15px;
        transition: 1s all;
        -webkit-transition: 1s all;
        -moz-transition: 1s all;
        -o-transition: 1s all;
    }
    label.lbl-1 {
      background: #6756ea;
      width: 20px;
      height: 20px;
      display: block;
      float: right;
      border-radius: 50%;
      margin: 16px 10px 0px 0px;
    }

    .all_list_brands_title_details_btn{
    width: 30px;
    height: 30px;
    text-align: center;
    font-size: 12px;
    line-height: 1.428571429;
    border-radius: 15px;
    margin-top: 30px;
    margin-left: 30px;
    float:left;
    background-color: red;
    border: 1px solid #d5d5d5;
}



    label.lbl-2 {
      background: #ea569a;
      width: 20px;
      height: 20px;
      display: block;
      float: right;
      border-radius: 50%;
       margin: 16px 10px 0px 0px;
    }
    label.lbl-3 {
      background: #f1c85f;
      width: 20px;
      height: 20px;
      display: block;
      float: right;
      border-radius: 50%;
      margin: 16px 10px 0px 0px;
    }
    /*--copyrights--*/
    .copy-rights{
        text-align: center;
        margin-top: 8em;
    }
    .copy-rights p{
        color:#FFF;
        font-size: 1em;
        line-height:1.8em;
    }
    .copy-rights p a{
        color:#ff2a75;
        -webkit-transition: all 0.3s ease-out;
        -moz-transition: all 0.3s ease-out;
        -ms-transition: all 0.3s ease-out;
        -o-transition: all 0.3s ease-out;
        transition: all 0.3s ease-out;
        text-decoration:none;
    }
    .copy-rights p a:hover{
        color:#3faa53;
        text-decoration:none;
            transition: 0.1s all;
        -webkit-transition: 0.1s all;
        -moz-transition: 0.1s all;
        -o-transition: 0.1s all;
    }
    /*--/copyrights--*/
    /*--start-responsive-design--*/
    @media (max-width:1440px){
        .key {
          background: url(../../assets/pass.png) no-repeat 376px 17px;
        }

        body {
          min-height: 811px;
        }
    }
    @media (max-width:1366px){
        .key {
          background: url(../../assets/pass.png) no-repeat 358px 19px;
        }
        .copy-rights {
          margin-top: 3em;
        }
        body {
          min-height: 768px;
        }
    }
    @media (max-width:1280px){
        .key {
           background: url(../../assets/pass.png) no-repeat 336px 18px;
        }
        body {
          min-height: 711px;
        }
        .copy-rights {
          margin-top: 0.5em;
        }
    }
    @media (max-width:1024px){
        .login-form {
          width: 37%;
        }
        .key {
           background: url(../../assets/pass.png) no-repeat 339px 18px;
        }
        .copy-rights {
          margin-top: 3em;
        }
        h1 {
          padding-top: 2em;
        }
        body {
          min-height: 675px;
        }
    }
    @media (max-width:768px){
        .login-form {
          width: 50%;
            margin: 12% auto 0 auto;
        }
        .key {
          background: url(../../assets/pass.png) no-repeat 342px 18px;
        }
        body {
          min-height: 929px;
        }
    }
    @media (max-width:640px){
        .login-form {
          width: 60%;
          margin: 20% auto 0 auto;
        }
        .key {
          background: url(../../assets/pass.png) no-repeat 342px 19px;
        }
    }
    @media (max-width:480px){
        .login-form {
          width: 80%;
        }
    }
    @media (max-width:320px){
        h1 {
          padding-top: 1em;
          font-size: 1.5em;
        }
        .login-form {
          width: 90%;
          margin: 10% auto 0 auto;
        }
        input[type="text"] {
          width: 62%;
          padding: 1.2em 2em .5em 2.5em;
          font-size: 17px;
          margin-top: .5em;
        }
        input[type="password"] {
            width: 62%;
            padding: 1.2em 2em .5em 2.5em;
            font-size: 17px;
            margin-top: .5em;
            margin-bottom: 2em;
              background: url(../../assets/key.png) no-repeat 8px 23px;
        }
        .key {
          background: url(../../assets/pass.png) no-repeat;
          position: relative;
          margin:1% auto;
        }
        .avtar img {
          margin: 1.1em 0 0;
        }
        .head-info {
          height: 35px;
          }
        label.lbl-1 {
          margin: 8px 10px 0px 0px;
        }
        label.lbl-2 {
          margin: 8px 10px 0px 0px;
        }
        label.lbl-3 {
          margin: 8px 10px 0px 0px;
        }
        .close {
          left: 16px;
          top: 13px;
        }
        .copy-rights {
          margin-top: 2em;
        }
        body {
            min-height: 504px;
        }
        input[type="submit"] {
          font-size: 28px;
          padding: 10px 0;
        }
    }
</style>

