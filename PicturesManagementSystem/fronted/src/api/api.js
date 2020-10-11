import axios from 'axios';
export const test = 'http://127.0.0.1:8000';

// 登录
export const login = params => { return axios.post(`${test}/api/user/login`, params).then(res => res.data); };
//主页--所有项目评论总数
export const getCommentsList = (headers, params) => {// 获取項目列表
    return axios.get(`${test}/v1/comments/all_commentslist`, { params: params, headers:headers}).then(res => res.data); };
//子页面--单个页面评论详情
export const getComments= (headers, params) =>{
    return axios.get(`${test}/v1/comments/comments_detail`, { params: params, headers:headers}).then(res => res.data); };


//我写的

// 上传图片
export const uploadImg =  (headers, form) => {
    return axios.post(`${test}/pictures/uploadImg`,  form, { headers:headers}).then(res => res.data);};
// 获取图片
export const getImage = (headers,params) => {
    return axios.get(`${test}/pictures/getImage`, {params: params,headers:headers}).then(res => res.data); };
// 搜索图片
export const searchImage = (headers,params) => {
    return axios.get(`${test}/pictures/searchImage`, {params: params,headers:headers}).then(res => res.data); };



