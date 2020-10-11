<template>
    <section>
        <!--工具条-->
        <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
            <el-form :inline="true"  @submit.native.prevent>
                <el-row>
                    <el-form-item label="开始日期">
                        <el-date-picker type="datetime" v-model="startTime"  placeholder="选择日期"
                                        value-format="yyyy-MM-dd HH:mm:ss" format="yyyy-MM-dd HH:mm:ss"
                                        :picker-options="pickerBeginDateBefore"  tyle="width:40px ;">

                        </el-date-picker>
                    </el-form-item>
                    <el-form-item label="结束日期">
                        <el-date-picker type="datetime" v-model="endTime"  placeholder="选择日期"
                                        value-format="yyyy-MM-dd HH:mm:ss" format="yyyy-MM-dd HH:mm:ss"
                                        :picker-options="pickerBeginDateAfter" tyle="width:40px ;">
                    </el-date-picker>


                    </el-form-item>
                    <el-form-item label="星级：">
                    </el-form-item>
                    <el-form-item>
                        <el-checkbox-group v-model="checkList"  @change="refeshList">
                        <el-checkbox label="一星"></el-checkbox>
                        <el-checkbox label="二星"></el-checkbox>
                        <el-checkbox label="三星"></el-checkbox>
                        <el-checkbox label="四星"></el-checkbox>
                        <el-checkbox label="五星"></el-checkbox>
                        </el-checkbox-group>
                    </el-form-item>
                </el-row>
                <el-row>
                     <el-form-item>
                        <el-button type="primary"  icon="el-icon-search" @click="queryComments">查询</el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary"  icon="fa fa-download" @click="exportComments"> 导出</el-button>
                    </el-form-item>
                </el-row>

                <!--
                <el-form-item>
                    <el-button type="primary" @click="handleAdd">新增</el-button>
                </el-form-item> -->
            </el-form>
        </el-col>

        <!--列表-->
        <el-table :data="comments" highlight-current-row v-loading="listLoading"
                  stripe height="500px" style="width: 100%;">
            <!--
            <el-table-column type="selection" min-width="5%">
            </el-table-column> -->


            <el-table-column  prop="project_name" label="项目名称" min-width="15%" >

            </el-table-column>

            <el-table-column prop="updateTime" label="评论时间" min-width="22%" sortable>
            </el-table-column>
            <el-table-column prop="content" label="评论内容" min-width="30%">
            </el-table-column>
            <el-table-column prop="score" label="星级" min-width="10%" sortable>
            </el-table-column>
            <el-table-column  prop="userKey" label="userID" min-width="15%" >

            </el-table-column>

            <el-table-column prop="device" label="设备" min-width="16%">
            </el-table-column>
            <el-table-column prop="versionName" label="版本" min-width="16%">
            </el-table-column>


        </el-table>

        <!--工具条-->

        <el-col :span="24" class="toolbar">
            <!-- <el-button type="danger" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button>   -->
            <el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20"
                           :page-count="total" style="float:right;">
            </el-pagination>
        </el-col>


    </section>
</template>

<script>
    //import NProgress from 'nprogress'
    import {
        getProject, delProject, disableProject, enableProject,
        updateProject, addProject, getCommentsProjectList,getCommentsList,getExportCommentsList
    } from '../../api/api';
    // import ElRow from "element-ui/packages/row/src/row";
    export default {
        // components: {ElRow},
        data() {
            return {

                startTime:'',
                endTime:'',
                comments: [],
                project_name_str: '',
                total: 0,
                page: 1,
                listLoading: false,
                sels: [],//列表选中列
                starslist:'12345',
                checkList: ['一星','二星','三星','四星','五星'],
                 pickerBeginDateBefore: {disabledDate: (time) => {
                       let beginDateVal = this.endTime;
                       if (beginDateVal) {
                          return time.getTime() > beginDateVal;
                       }
                    }
                },
              pickerBeginDateAfter: {disabledDate: (time) => {
                   let beginDateVal =this.startTime;
                   if (beginDateVal) {
                      return time.getTime() < beginDateVal;
                   }
                }
             },
            }
        },
        methods: {
            // 获取项目列表
            getCommentsList(val) {
                this.listLoading = true;
                let self = this;

                let params = {page: self.page, project_id: this.$route.params.project_id,score:val,startTime:this.startTime,endTime:this.endTime};
                console.log(params)
                let headers = {Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))};
                getCommentsList(headers, params).then((res) => {
                        self.listLoading = false;
                    let {msg, code, data} = res;
                    if (code === '999999') {
                        self.total = data.total;
                        self.comments = data.data
                    }
                    else {
                        self.$message.error({
                            message: msg,
                            center: true,
                        })
                    }
                })
            },
            getCommentsByExportList(val) {
                this.listLoading = true;
                let self = this;
                let params = {page: 1, project_id: this.$route.params.project_id,score:val,startTime:self.startTime,endTime:self.endTime};
                let headers = {Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))};
                getExportCommentsList(headers, params).then((res) => {
                    self.listLoading = false;
                    let {msg, code, data} = res;
                    if (code === '999999') {
                        self.project_name_str = data.data[0].project_name
                        this.excelData  = data.data
                        require.ensure([], () => {
                            const { export_json_to_excel } = require('../../excel/Export2Excel'); //这里必须使用绝对路径
                            const tHeader = ['项目名称','评论时间', '评论内容', '星级','设备','版本']; // 导出的表头名
                            const filterVal = ['project_name','updateTime','content', 'score','device','versionName']; // 导出的表头字段名
                            const list = this.excelData;
                            const project_name_str = this.project_name_str;
                            const data = this.formatJson(filterVal, list);
                            let time1,time2 = '';
                            if(this.startTime !== '') {
                                time1 = this.startTime.substring(0,10)
                            }
                            if(this.endTime !== '') {
                                time2 = this.endTime.substring(0,10)
                            }
                            export_json_to_excel(tHeader, data, project_name_str+`评论导出[${time1}-${time2}]`);
                        })

                    }
                    else {
                        self.$message.error({
                            message: msg,
                            center: true,
                        })
                    }
                })
            },
            handleCurrentChange(val) {
                 this.page = val;
                  this.handleCheckedStarsChange(this.checkList);
                  this.getCommentsList(this.starslist);
            },
            //星级变化
            handleCheckedStarsChange(value) {
                //this.listLoading = true;
                if (value.length ==0){
                    alert("请先勾选某个星级再查询")
                    return;
                }
                let stars = ''
                for (let star in value) {
                   // let NetworkInterfaceInfo = star

                    if (value[star] =='一星'){
                        stars = stars+"1"
                    }
                    if (value[star] =='二星'){
                        stars = stars+"2"
                    }
                    if (value[star] =='三星'){
                        stars = stars+"3"
                    }
                    if (value[star] =='四星'){
                        stars = stars+"4"
                    }
                    if (value[star] =='五星'){
                        stars = stars+"5"
                    }
                }
                this.starslist = stars
                console.log(stars)
                //this.getCommentsList(stars)

              },
            //选择开始时间，清空结束时间
              changeTime(date){
                    this.endTime="";
                    this.pickerBeginDateAfter={
                      disabledDate(time) {  //开始时间-结束时间
                        return (time.getTime() < new Date(date).getTime());
                      }
                    }
              },
            //查询
            queryComments(value){
                   if((this.startTime =='' || this.startTime == null) && (this.endTime !='' || this.endTime !=null)){
                      alert("请输入开始时间和截止时间进行查询")
                      return;
                  }
                  if(((this.startTime =='' || this.startTime == null) && this.endTime !='' && this.endTime !=null)
                      || (this.startTime !='' && this.startTime !=null && (this.endTime ==''||this.endTime == null))){
                      alert("请同时输入开始时间、截止时间进行查询")
                      return;
                  }
                  if(this.startTime> this.endTime){
                      alert("开始时间大于截止时间，请重新输入")
                      return;
                  }
                  this.getStarslist();
                  this.getCommentsList(this.starslist);

            },
            //导出
            exportComments(value){
                if((this.startTime =='' || this.startTime == null) && (this.endTime !='' || this.endTime !=null)){
                     alert("请输入时间区间进行导出")
                     return;
                 }
                 if(((this.startTime =='' || this.startTime == null) && this.endTime !='' && this.endTime !=null)
                     || (this.startTime !='' && this.startTime !=null && (this.endTime ==''||this.endTime == null))){
                     alert("请同时输入开始时间、截止时间进行导出")
                     return;
                 }
                 if(this.startTime> this.endTime) {
                     alert("开始时间大于截止时间，请重新输入")
                     return;
                 }
                var dateBegin = new Date(this.startTime);
                var dateEnd = new Date(this.endTime);
                var dateDiff = dateEnd.getTime() - dateBegin.getTime();//时间差的毫秒数
                var dayDiff = Math.floor(dateDiff / (24 * 3600 * 1000));//计算出相差天数
                if (dayDiff >90){
                    alert("仅支持导出最长90天的评论数据")
                     return;
                }
                 this.$confirm('此操作将导出excel文件, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.getStarslist();
                    this.getCommentsByExportList(this.starslist);
                    //更新，修改下载文档至上面的查询接口
                    //this.excelData = this.comments //你要导出的数据list。
                    //this.export2Excel()
                }).catch(() => {

                });

            },
             export2Excel() {
                var that = this;
                require.ensure([], () => {
                    const { export_json_to_excel } = require('../../excel/Export2Excel'); //这里必须使用绝对路径
                    const tHeader = ['项目名称','评论时间', '评论内容', '星级','设备','版本']; // 导出的表头名
                    const filterVal = ['project_name','updateTime','content', 'score','device','versionName']; // 导出的表头字段名
                    const list = that.excelData;
                    const data = that.formatJson(filterVal, list);
                    let time1,time2 = ''
                    export_json_to_excel(tHeader, data, '提现管理excel');// 导出的表格名称，根据需要自己命名
                })
            },
            formatJson(filterVal, jsonData) {
                return jsonData.map(v => filterVal.map(j => v[j]))
            },
            getStarslist(){
                 let stars = ''
                 for (let star in this.checkList) {
                   // let NetworkInterfaceInfo = star

                    if (this.checkList[star] =='一星'){
                        stars = stars+"1"
                    }
                    if (this.checkList[star] =='二星'){
                        stars = stars+"2"
                    }
                    if (this.checkList[star]=='三星'){
                        stars = stars+"3"
                    }
                    if (this.checkList[star] =='四星'){
                        stars = stars+"4"
                    }
                    if (this.checkList[star] =='五星'){
                        stars = stars+"5"
                    }
                }
                this.starslist = stars
            },

            refeshList(value){
                this.handleCheckedStarsChange(value);
                this.getCommentsList(this.starslist);
            },
        },
        // 刚进入页面加载
        mounted() {
            //let params = {page: self.page, project_id: self.filters.project_id,score:'12345'};
            //this.getCommentsList('12345');
            this.startTime = this.$route.params.startTime;
            this.endTime = this.$route.params.endTime;
            this.getCommentsList('12345');
        }
    }

</script>

<style>

</style>
