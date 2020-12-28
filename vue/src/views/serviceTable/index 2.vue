<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="Location">
        <template slot-scope="scope">
          {{ scope.ip }}
        </template>
      </el-table-column>
      <el-table-column label="URL" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Talnet_Status" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.params }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="opencv_state" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Service" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.service }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Operation" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.operation }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column> -->
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then((res) => {
        console.log(res)
      this.list = res.data.data;
      this.listLoading = false
      })
      // this.list=getList()
      // console.log (this.list)
    }
  }
}
</script>
