// import request from '@/utils/request'
import axios from 'axios'

export async function getList(params) {
  // return request({
  //   // url: '/vue-admin-template/table/list',
  //   url: '/camera_before',
  //   method: 'get',
  //   params
  // })
  return axios.get('http://localhost:8080/camera_before')
    .then(function(response) {
      console.log(response)
      return response.data
    })
    .catch(function(error) {
      console.log(error)
    })
}
