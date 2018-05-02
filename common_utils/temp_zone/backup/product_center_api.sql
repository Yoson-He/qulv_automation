CREATE TABLE `product_center_api` (
     `id` bigint(50) NOT NULL AUTO_INCREMENT COMMENT '接口ID',
      `api_code` int(50) DEFAULT NULL COMMENT '接口编号',
      `api_type` int(5) NOT NULL DEFAULT '0' COMMENT '接口类型：0、q-boss；1、官网；2、最海岛；3、app',
      `api` varchar(100) DEFAULT NULL COMMENT '接口名',
      `key_word` varchar(255) DEFAULT NULL COMMENT '关键字',
      `host` varchar(100) NOT NULL COMMENT '请求主机名',
      `path` varchar(100) DEFAULT NULL COMMENT '接口路径',
      `url` varchar(100) DEFAULT NULL COMMENT '请求地址',
      `method` varchar(10) DEFAULT NULL COMMENT '请求方法',
      `headers` varchar(50) DEFAULT NULL COMMENT '请求头',
      `parameters_type` varchar(5) DEFAULT NULL COMMENT '传参类型：query；path；body',
      `path_params` varchar(100) DEFAULT NULL COMMENT '请求path值',
      `query_params` varchar(100) DEFAULT NULL COMMENT '请求query值',
      `body_params` varchar(100) DEFAULT NULL COMMENT '请求body值',
      `case_level` varchar(10) DEFAULT NULL COMMENT '用例等级(0-请求校验；1-字段校验；2-权限校验；3-场景校验；4-数据校验)',
      `expected_results` varchar(100) DEFAULT NULL COMMENT '预期结果',
      `test_results` varchar(100) DEFAULT NULL COMMENT '测试结果',
      `http_code` varchar(5) DEFAULT NULL COMMENT 'http状态码',
      `http_response` varchar(100) DEFAULT NULL COMMENT '返回值',
      `err_code` varchar(5) DEFAULT NULL COMMENT '错误码',
      `error_info` varchar(100) DEFAULT NULL COMMENT '错误信息',
      `test_status` varchar(2) DEFAULT NULL COMMENT '返回值',
      `create_by` varchar(255) NOT NULL COMMENT '创建者',
      `update_by` varchar(255) DEFAULT NULL COMMENT '更新者',
	  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	  `update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
      `remark` varchar(255) DEFAULT NULL COMMENT '备注',
      `state` bigint(1) DEFAULT '1' COMMENT '状态(0-无效，1-有效)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;