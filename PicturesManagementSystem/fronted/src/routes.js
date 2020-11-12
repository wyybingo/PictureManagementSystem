const Login = () => import('./views/common/Login.vue')
const Home = () => import('./views/common/Home.vue');




const ProjectsList = () => import('./views/videos/ProjectsList.vue')
const UploadPicture = () => import('./views/pictures/Photo.vue')
const PicturesList = () => import('./views/pictures/PhotoList.vue')




// main.js中设定的登录跳转的path 就是在这里定义的
//  hidden:  项目是否展示出来      projectHidden：项目是否展开
let routes = [
  {
    path: '/login',
    component: Login,
    name: '',
    hidden: true,
    projectHidden: true
  },
  {
    path: '/home',
    component: Home,
    name: '所有文件',
    iconCls: 'fa fa-th-list',
    projectHidden: false,
    children: [
      {path: '/uploadPicture', component: UploadPicture, name: '图片', hidden: false,},
      {path: '/picturesList', component: PicturesList, name: 'gif', hidden: false,},
      {path: '/commentsDetail/project_id=:project_id', component: PicturesList, name: '视频', hidden: false,},

    ]

  },
  {
    path: '/project',
    component: Home,
    name: '智能分类',
    projectHidden: false,
    children: [
      {
        path: '/projectsList', component: ProjectsList, name: '时光轴', hidden: false,   //这个是所有项目评论列表
      },
      {
        path: '/projectsList', component: ProjectsList, name: '足迹', hidden: false,   //这个是所有项目评论列表
      },
      {
        path: '/projectsList', component: ProjectsList, name: '智能分类', hidden: false,   //这个是所有项目评论列表
      },
    ]
  }

]

export default routes;
