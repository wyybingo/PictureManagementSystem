// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.



import Vue from 'vue';
import ElementUI from 'element-ui';
import App from './App.vue';

import 'element-ui/lib/theme-chalk/index.css'
import './assets/icon/iconfont.css'
import VueRouter from 'vue-router'
import store from './vuex/store'    //暂时不用
import Vuex from 'vuex'
import routes from './routes'


// Vue.config.productionTip = false   # 先注释掉

Vue.use(ElementUI);     // 这个需要在dist/static/index.html中引入什么内容
Vue.use(VueRouter);
Vue.use(Vuex);

import preview from 'vue-preview'



const router = new VueRouter({     //引入 routes.js下的  routes 路径定义，渲染VUE组件
  routes
});


// 登录后在sessionStorage中添加token的值，退出后清空
router.beforeEach((to, from, next) => {
  //NProgress.start();
  if (to.path === '/login') {  // 如果是登录
    sessionStorage.removeItem('token');   //  删除登录token
  }
  let token = JSON.parse(sessionStorage.getItem('token'));
  if (!token && to.path !== '/login') {
    console.log(to.path);
    next({ path: '/login', query: {url: to.path}})
  } else {
    next()
  }
  if (to.path === '/') {
    next({ path: '/home',})
  }
});

//解决路由报错问题：NavigationDuplicated

import Router from 'vue-router'

const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}





// let Highlight = {};
// Highlight.install = function (Vue, options) {
//     // 先有数据再绑定，调用highlightA
//     Vue.directive('highlightA', {
//         inserted: function(el) {
//             let blocks = el.querySelectorAll('pre code');
//             for (let i = 0; i < blocks.length; i++) {
//               console.log(blocks)
//                 console.log(blocks[i])
//                 const item = blocks[i];
//                 console.log(item)
//                 hljs.highlightBlock(item);
//             };
//         }
//     });
//     // 先绑定，后面会有数据更新，调用highlightB
//     Vue.directive('highlightB', {
//         componentUpdated: function(el) {
//             let blocks = el.querySelectorAll('pre code');
//             for (let i = 0; i < blocks.length; i++) {
//                 const item = blocks[i];
//                 hljs.highlightBlock(item);
//             };
//         }
//     });
// };
//
// Vue.use(Highlight);

//router.afterEach(transition => {
//NProgress.done();
//});


 //暂时不用
// new Vue({
//   //el: '#app',
//   //template: '<App/>',
//   router,
//   store,
//   //components: { App }
//   render: h => h(App)
// }).$mount('#app');


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
