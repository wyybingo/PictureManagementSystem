<template>
    <el-row class="container">
        <el-col :span="24" class="header">
            <el-col :span="10" class="logo" :class="collapsed?'logo-collapse-width':'logo-width'">
<!--               默认展示左边的：sysName： 自动化测试平台 ，collapsed时啥都不展示 -->
               <router-link to="/commentsList" style='text-decoration: none;color: #FFFFFF;'>{{collapsed?'':sysName}}
                </router-link>
            </el-col>
            <el-col :span="8" style="padding-left: 20px">
<!--              中间分隔：此处控制点击滑动展开还是收起-->
                <div class="tools" @click.prevent="collapse">
                    <i class="fa fa-align-justify"></i>
                </div>
            </el-col>
<!--   和上面的中间分隔格式一样，在头像右侧，点击后展示登录情况-->
            <el-col :span="2" class="menu-right">
                <div class="tools"  @click="showCont">
                    <i class="fa fa-align-justify"></i>
                </div>
            </el-col>
<!--          我的头像部分，设置hover上去调用 dropdown-->
            <el-col :span="8" class="userinfo">
                <el-dropdown trigger="hover">
                    <span class="el-dropdown-link userinfo-inner">
                    {{sysUserName}}
                    <img src="../../assets/userphoto.jpg"/>   <!--            注意这里是../..   路径一定要修改好-->
					          </span>
                   <el-dropdown-menu slot="dropdown">
                       <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </el-col>

        </el-col>


        <el-col :span="24" class="main">
            <aside :class="collapsed?'menu-collapsed':'menu-expanded'">     <!--              左边导航菜单：折叠功能-->
                <!--导航菜单  $route.path ：当前路由对象的路径-->
                <el-menu :default-active="$route.path" class="el-menu-vertical-demo" @open="handleopen"
                         @close="handleclose" @select="handleselect"
                         unique-opened router v-if="!collapsed">      <!-- 单个激活，并以index作为path进行路由跳转-->
<!--               从template开始：动态路由到子组件，将不可见的路径隐藏-->
                    <template v-for="(item,index) in $router.options.routes" v-if="!item.hidden">
                        <el-submenu :index="index+''" v-if="!item.leaf">
                           <!--用element ui 的title进行solt分发菜单-->
                            <template slot="title"><i :class="item.iconCls"></i>{{item.name}}</template>
                           <!--item.name和item.children.name来配置菜单栏和子菜单栏的名称-->
                            <el-menu-item v-for="child in item.children" :index="child.path" :key="child.path"
                                          v-if="!child.hidden">{{child.name}}
                            </el-menu-item>
                        </el-submenu>
                        <el-menu-item v-if="item.leaf&&item.children.length>0" :index="item.children[0].path"><i
                                :class="item.iconCls"></i>{{item.children[0].name}}
                        </el-menu-item>
                    </template>
                </el-menu>
                <!--导航菜单-折叠后-->
                <ul class="el-menu el-menu-vertialc-demo collapsed" v-show="collapsed" ref="menuCollapsed">
                    <li v-for="(item,index) in $router.options.routes" v-if="!item.hidden" class="el-submenu item">
                        <template v-if="!item.leaf">
                            <div class="el-submenu__title" style="padding-left: 20px;" @mouseover="showMenu(index,true)"
                                 @mouseout="showMenu(index,false)"><i :class="item.iconCls"></i></div>
                            <ul class="el-menu submenu" :class="'submenu-hook-'+index" @mouseover="showMenu(index,true)"
                                @mouseout="showMenu(index,false)">
                                <li v-for="child in item.children" v-if="!child.hidden" :key="child.path"
                                    class="el-menu-item" style="padding-left: 40px;"
                                    :class="$route.path==child.path?'is-active':''" @click="$router.push(child.path)">
                                    {{child.name}}
                                </li>
                            </ul>
                        </template>
                        <template v-else>
                            <!--<li class="el-submenu">-->
                            <!--<div class="el-submenu__title el-menu-item" style="padding-left: 20px;height: 56px;line-height: 56px;padding: 0 20px;" :class="$route.path==item.children[0].path?'is-active':''" @click="$router.push(item.children[0].path)"><i :class="item.iconCls"></i></div>-->
                            <!--</li>-->
                        </template>
                    </li>
                </ul>
            </aside>


<!--          Element-UI实现面包屑导航：右上角的路径导航：a>b   -->
<!--          $route.name	当前路径名字-->
<!--          $route.matched	：数组，包含当前匹配的路径中所包含的所有片段所对应的配置参数对象。-->
            <section class="content-container">
                <div class="grid-content bg-purple-light">
                    <el-col :span="24" class="breadcrumb-container">
                        <strong class="title">{{$route.name}}</strong>
                        <el-breadcrumb separator="/" class="breadcrumb-inner">
                            <el-breadcrumb-item v-for="item in $route.matched" :key="item.path">
                                {{ item.name }}
                            </el-breadcrumb-item>
                        </el-breadcrumb>
                    </el-col>
                    <el-col :span="24" class="content-wrapper">
                        <transition name="fade" mode="out-in">
                            <router-view></router-view>
                        </transition>
                    </el-col>
                </div>
            </section>

<!--          右上角点击： 展示网站的浏览情况-->
            <aside style="border-left:1px solid #e6e6e6;overflow: auto" v-if="show">
                <div class="item">
                    <h4 style="margin-left: 10px">使用情况</h4>
                    <nx-data-tabs :option="easyDataOption"></nx-data-tabs>
                </div>
                <!--<div class="item">-->
                <!--<h4>带数字的展示</h4>-->
                <!--<nx-data-icons :option="easyDataOption1"></nx-data-icons>-->
                <!--</div>-->
            </aside>
        </el-col>
    </el-row>
</template>

<script>
    // import {VisitorNumber} from '../api/api'
    import nxDataDisplay from '@/components/nx-data-display/nx-data-display'
    import nxDataCard from '@/components/nx-data-card/nx-data-card'
    import nxDataTabs from '@/components/nx-data-tabs/nx-data-tabs'
    import nxDataIcons from '@/components/nx-data-icons/nx-data-icons'
    import nxGithubCorner from '@/components/nx-github-corner'

    export default {
        components: {
            nxDataDisplay,
            nxDataCard,
            nxDataTabs,
            nxDataIcons,
            nxGithubCorner

        },
        data() {
            return {

                show: false,

                easyDataOption: {
                    span: 20,
                    data: [
                        {
                            title: '登录统计',
                            subtitle: '123',
                            count: 0,
                            allcount: 0,
                            text: '今日登录',
                            color: 'rgb(49, 180, 141)',
                            key: '登'
                        },
                        {
                            title: '查询评论列表统计',
                            subtitle: '实时',
                            count: 0,
                            allcount: 0,
                            text: '今日查询',
                            color: 'rgb(56, 161, 242)',
                            key: '评'
                        },
                        {
                            title: '查询评论详情统计',
                            subtitle: '实时',
                            count: 0,
                            allcount: 0,
                            text: '今日查询',
                            color: 'rgb(117, 56, 199)',
                            key: '详'
                        },
                        {
                            title: '导出统计',
                            subtitle: '实时',
                            count: 0,
                            allcount: 0,
                            text: '今日导出',
                            color: 'rgb(59, 103, 164)',
                            key: '导'
                        },


                    ]
                },

                easyDataOption1: {
                    color: 'rgb(63, 161, 255)',
                    span: 4,
                    data: [
                        {
                            title: '今日登录',
                            count: 22139,
                            icon: 'iconfont el-icon-yandongtongji'
                        },
                    ]
                },

                sysName: '照片管理系统',
                collapsed: false,
                sysUserName: 'admin',
                // sysUserAvatar: '',
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                }
            }
        },
        methods: {


            showCont: function () {
                alert("ok")

                this.show = !this.show;

            },

            VisitorNumber() {

                this.listLoading = true;
                let self = this;
                // let params = {
                //     project_id: this.$route.params.project_id,
                //     page: self.page,
                //     name: self.filters.name,
                //
                // };
                let headers = {
                    Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))
                };
                VisitorNumber(headers).then(_data => {
                    let {msg, code, data} = _data;
                    self.listLoading = false;
                    if (code === '999999') {
                        self.VisitorNumbers = data.data
                        console.log(self.VisitorNumbers)
                        self.easyDataOption.data[0].count = Number(self.VisitorNumbers[0].count)
                        self.easyDataOption.data[0].allcount = Number(self.VisitorNumbers[0].dayCount)
                        self.easyDataOption.data[1].count = Number(self.VisitorNumbers[10].count)
                        self.easyDataOption.data[1].allcount = Number(self.VisitorNumbers[10].dayCount)
                        self.easyDataOption.data[2].count = Number(self.VisitorNumbers[11].count)
                        self.easyDataOption.data[2].allcount = Number(self.VisitorNumbers[11].dayCount)
                        self.easyDataOption.data[3].count = Number(self.VisitorNumbers[18].count)
                        self.easyDataOption.data[3].allcount = Number(self.VisitorNumbers[18].dayCount)

                    } else {
                        self.$message.error({
                            message: msg,
                            center: true,
                        })
                    }
                });


            },

            onSubmit() {
                console.log('submit!');
            },
            handleopen() {
                //console.log('handleopen');
            },
            handleclose() {
                //console.log('handleclose');
            },
            handleselect: function (a, b) {
            },

            //退出登录
            logout: function () {
                var _this = this;
                this.$confirm('确认退出吗?', '提示', {
                    //type: 'warning'
                }).then(() => {
                    sessionStorage.removeItem('token');
                    _this.$router.push('/login');
                }).catch(() => {

                });
            },
            //折叠导航栏
            collapse: function () {
                this.collapsed = !this.collapsed;
            },
            showMenu(i, status) {
                this.$refs.menuCollapsed.getElementsByClassName('submenu-hook-' + i)[0].style.display = status ? 'block' : 'none';
            }
        },
        mounted() {
            var user = sessionStorage.getItem('username');
            if (user) {
                name = JSON.parse(user);
                this.sysUserName = name || 'admin';    //  初始进入加载，如果登录成功，则获取 name展示在右上角
//				this.sysUserAvatar = '../assets/user.png';
            }
            this.VisitorNumber();

        }
    }

</script>

<style lang="scss">
    @import '../../styles/data-card';
    @import '../../styles/data-display';
    @import '../../styles/data-icons';
    @import '../../styles/data-tabs';
</style>


<style scoped lang="scss">
    @import '../../styles/vars';

    .container {
        position: absolute;
        top: 0px;
        bottom: 0px;
        width: 100%;

        .header {
            height: 60px;
            line-height: 60px;
            background: $color-primary;
            color: #fff;

            .userinfo {
                text-align: right;
                /*padding-right: 35px;*/
                float: right;

                .userinfo-inner {
                    cursor: pointer;
                    color: #fff;

                    img {
                        width: 40px;
                        height: 40px;
                        border-radius: 20px;
                        margin: 10px 0px 10px 10px;
                        float: right;
                    }
                }
            }

            .menu-right {
                text-align: right;
                padding-right: 25px;
                float: right;
            }

            .el-col-2 {
                width: 5%;
            }

            .logo {
                //width:230px;
                height: 60px;
                font-size: 22px;
                padding-left: 20px;
                padding-right: 20px;
                border-color: rgba(238, 241, 146, 0.3);
                border-right-width: 1px;
                border-right-style: solid;

                img {
                    width: 40px;
                    float: left;
                    margin: 10px 10px 10px 18px;
                }

                .txt {
                    color: #fff;
                }
            }

            .logo-width {
                width: 230px;
            }

            .logo-collapse-width {
                width: 60px
            }

            .tools {
                /*padding: 0px 23px;*/
                /*width: 14px;*/
                height: 60px;
                line-height: 60px;
                cursor: pointer;
            }
        }

        .main {
            display: flex;
            // background: #324057;
            position: absolute;
            top: 60px;
            bottom: 0px;
            overflow: hidden;
            margin-left: 0px;

            aside {
                flex: 0 0 230px;
                width: 230px;
                // position: absolute;
                // top: 0px;
                // bottom: 0px;
                .el-menu {
                    height: 100%;
                }

                .collapsed {
                    width: 60px;

                    .item {
                        position: relative;
                    }

                    .submenu {
                        position: absolute;
                        top: 0px;
                        left: 60px;
                        z-index: 99999;
                        height: auto;
                        display: none;
                    }

                }
            }

            .menu-collapsed {
                flex: 0 0 60px;
                width: 60px;
            }

            .menu-expanded {
                flex: 0 0 230px;
                width: 230px;
            }

            .content-container {
                // background: #f1f2f7;
                flex: 1;
                // position: absolute;
                // right: 0px;
                // top: 0px;
                // bottom: 0px;
                // left: 230px;
                overflow-y: scroll;
                padding: 20px;

                .breadcrumb-container {
                    //margin-bottom: 15px;
                    .title {
                        width: 200px;
                        float: left;
                        color: #475669;
                    }

                    .breadcrumb-inner {
                        float: right;
                    }
                }

                .content-wrapper {
                    background-color: #fff;
                    box-sizing: border-box;
                }
            }
        }
    }


    .text-muted {
        margin-top: 1rem;
        margin-bottom: 1rem;

    }

    .demo-i-circle-custom h1 {
        color: #3f414d;
        font-size: 28px;
        font-weight: normal;
    }

    .demo-i-circle-custom p {
        color: #657180;
        font-size: 14px;
        margin: 10px 0 15px;
    }

    .demo-i-circle-custom span {
        display: block;
        padding-top: 15px;
        color: #657180;
        font-size: 14px;
    }

    /*  .demo-i-circle-custom:before{
           content: '';
           display: block;
           width: 80px;
           height: 1px;
           margin: 0 auto;
           background: #e0e3e6;
           position: relative;
           top: 100px;
       };*/
    .demo-i-circle-custom span i {
        font-style: normal;
        color: #3f414d;
    }
</style>
