DROP TABLE IF EXISTS tec_title;
CREATE TABLE tec_title (
  id bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  title varchar(256)  COMMENT '文章标题',
  title_type bigint(2) unsigned DEFAULT '1' COMMENT '文章类型 1python 2java',
  title_url VARCHAR(256)  COMMENT '对应url',
  level  bigint(2) unsigned DEFAULT '1' COMMENT 'level',
  parentid bigint(20) unsigned DEFAULT '1' COMMENT '父节点',
  createtime timestamp  DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updatetime timestamp  COMMENT '更新时间',
  createuser bigint(20) DEFAULT NULL,
  c1 varchar(32) DEFAULT NULL,
  c2 varchar(32) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1550010433 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tec_content;
CREATE TABLE tec_content (
  id bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  titleid bigint(20) unsigned DEFAULT '1' COMMENT '标题id',
  content text(20) COMMENT '内容',
  createtime timestamp  DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updatetime timestamp  COMMENT '更新时间',
  createuser bigint(20) DEFAULT NULL,
  c1 varchar(32) DEFAULT NULL,
  c2 varchar(32) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1550010433 DEFAULT CHARSET=utf8;