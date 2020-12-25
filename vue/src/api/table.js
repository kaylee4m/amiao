// import request from '@/utils/request'
import axios from 'axios'

export function getList(params) {
  // return request({
  //   // url: '/vue-admin-template/table/list',
  //   url: '/camera_before',
  //   method: 'get',
  //   params
  // })
  axios.get('http://localhost:8080/camera_before')
    .then(function(response) {
      console.log('===========')
      console.log(response)
    })
    .catch(function(error) {
      console.log(error)
    })
}
