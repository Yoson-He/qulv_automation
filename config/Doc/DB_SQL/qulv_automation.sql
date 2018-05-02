CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `pro_api` (
  `api_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '接口ID',
  `api_name` varchar(45) NOT NULL COMMENT '接口名',
  `meun_id` int(11) NOT NULL,
  `api_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '接口类型：0 未定义；1 新增；2 删除；3 修改；4 查询；5 其他',
  `method` tinyint(1) NOT NULL COMMENT '请求类型：0 get；1 post',
  `path` varchar(100) DEFAULT NULL COMMENT '接口地址',
  `headers` varchar(50) DEFAULT NULL COMMENT '请求头',
  `uri_params` varchar(100) DEFAULT NULL COMMENT 'uri',
  `req_params` varchar(100) DEFAULT NULL COMMENT '传参',
  `req_body` varchar(1000) DEFAULT NULL COMMENT '请求体',
  `remark` varchar(1000) DEFAULT NULL COMMENT '备注',
  `created_by` varchar(45) NOT NULL COMMENT '创建人',
  `updated_by` varchar(45) DEFAULT NULL COMMENT '更新人',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `state` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态(0-无效，1-有效)',
  PRIMARY KEY (`api_id`),
  UNIQUE KEY `api_id_UNIQUE` (`api_id`),
  UNIQUE KEY `api_name_UNIQUE` (`api_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='接口基础信息';

CREATE TABLE `pro_case` (
  `case_id` int(11) NOT NULL AUTO_INCREMENT,
  `case_name` varchar(45) NOT NULL,
  `api_id` int(11) NOT NULL,
  `meun_id` int(11) NOT NULL,
  `level` tinyint(1) NOT NULL COMMENT '用例等级: 0 接口访问测试；1 接口基础测试（,边界分析，参数组合,异常情况）；2 业务功能测试；3 性能测试；4 安全测试',
  `pre_condition` varchar(45) DEFAULT NULL COMMENT '前置条件',
  `uri_params_value` varchar(100) DEFAULT NULL,
  `req_params_value` varchar(100) DEFAULT NULL COMMENT '传参',
  `req_body_value` varchar(1000) DEFAULT NULL,
  `expected_result` varchar(1000) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `created_by` varchar(45) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(45) DEFAULT NULL,
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `state` tinyint(1) NOT NULL DEFAULT '1' COMMENT '接口状态：0 禁用；1 可用 ',
  PRIMARY KEY (`case_id`),
  UNIQUE KEY `case_id_UNIQUE` (`case_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

CREATE TABLE `pro_result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) NOT NULL,
  `api_id` int(11) NOT NULL,
  `pass_or_fail` varchar(20) NOT NULL COMMENT '是否通过：1  PASS, 0 FAIL',
  `status_code` varchar(45) NOT NULL,
  `url` varchar(500) NOT NULL,
  `headers` varchar(500) NOT NULL,
  `actual_result` varchar(500) NOT NULL COMMENT '实际结果',
  `response_body` varchar(1000) NOT NULL,
  `expected_result` varchar(500) NOT NULL COMMENT '预期结果',
  `created_by` varchar(45) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`result_id`),
  UNIQUE KEY `result_id_UNIQUE` (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='测试结果';

CREATE TABLE `pro_task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(45) NOT NULL,
  `case_list` varchar(1000) NOT NULL,
  `result_list` varchar(1000) DEFAULT NULL,
  `remark` varchar(1000) DEFAULT NULL COMMENT '备注',
  `created_by` varchar(45) NOT NULL COMMENT '创建人',
  `updated_by` varchar(45) DEFAULT NULL COMMENT '更新人',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `state` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态(0-无效，1-有效)',
  PRIMARY KEY (`task_id`),
  UNIQUE KEY `task_id_UNIQUE` (`task_id`),
  UNIQUE KEY `task_name_UNIQUE` (`task_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `q_boss_meun` (
  `menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `sys_name` varchar(45) NOT NULL,
  `main_module` varchar(45) NOT NULL,
  `module` varchar(45) NOT NULL,
  `sub_module` varchar(45) NOT NULL,
  `created_by` varchar(45) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(45) DEFAULT NULL,
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `state` tinyint(1) NOT NULL DEFAULT '1' COMMENT '接口状态：0 禁用；1 可用 ',
  PRIMARY KEY (`menu_id`),
  UNIQUE KEY `menu_id_UNIQUE` (`menu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `sys_user` (
  `user_id` int(11) NOT NULL COMMENT '用户ID',
  `user_name` varchar(100) NOT NULL COMMENT '用户名',
  `realName` varchar(100) DEFAULT NULL COMMENT '真实姓名',
  `display_picture` varchar(128) DEFAULT NULL COMMENT '头像',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `email` varchar(100) DEFAULT NULL COMMENT '邮箱',
  `phone` varchar(100) DEFAULT NULL COMMENT '手机',
  `user_role` int(5) NOT NULL DEFAULT '0' COMMENT '用户角色：0、游客; 8、测试; 9、管理员admin',
  `level` int(5) DEFAULT NULL COMMENT '用户等级',
  `created_by` varchar(45) NOT NULL COMMENT '创建人',
  `updated_by` varchar(45) DEFAULT NULL COMMENT '更新人',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '更新时间',
  `remark` varchar(1000) DEFAULT NULL COMMENT '备注',
  `state` tinyint(1) DEFAULT '1' COMMENT '状态(0-禁用，1-启用)',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `id_UNIQUE` (`user_id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息';
