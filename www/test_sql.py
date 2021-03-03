#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Greyrat'

# 对前面写的进行测试
# 安装好 MySQL 后， 第一步：从开始菜单打开 'MySQL Notifier 1.1.8' ，并在任务栏中开启它
# 第二步：开始菜单打开 'MySQL 5.6 Command Line Client' ，并输入安装时你设置的 root 密码
# 输密码的时候不会显示密码，你只管输，然后回车
# 第三步：把下面注释的代码复制到 SQL 命令行里，然后回车
# 这里初始化了一个名为 moe 的数据库表
'''
-- schema.sql
drop database if exists moe;
drop user if exists 'www-data'@'localhost';
create database moe;
use moe;
create user 'www-data'@'localhost' identified by 'www-data';
alter user 'www-data'@'localhost' identified with mysql_native_password by 'www-data';
grant select, insert, update, delete on moe.* to 'www-data'@'localhost';
create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
'''

# 第四步：把下面这部分代码放在 python 里跑
import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='moe')
    u = User(name='Test', email='test@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    orm.__pool.close()
    await orm.__pool.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

# 第五步：在 sql 命令行里输入 'SELECT * FROM users;'  然后回车（别漏了分号）
# 显示 test@qq.com 代表测试成功了
