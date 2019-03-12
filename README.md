# 201901upload_file
ajax上传文件和form+iframe上传文件
内容回顾：
1 django部分
　　1 什么是ORM？
		关系对象映射，ORM中创建一些对应关系：    
		类 -> 表
		字段 -> 列
		对象 -> 行
		开发者通过操作类和对象，内部讲起转化为对应的SQL语句再去执行。
	2 ORM和原生SQL的区别？
		执行效率高：原生SQL
		开发效率高：ORM
		兼容性好：指的是连接不同的数据库时，ORM会帮助用户自动翻译成为相应的SQL语句
	3 django的组件？
		-Form组件
		-Cookie和Session
		-用户认证
		-分页
		-CSRF
		-模板引擎
		django是一个大而全且组件丰富的框架.
2 git部分
	1 你们是基于git做协同开发？
		-每个人一个分支 master/dev/每个人
		-阶段性进行合并(1,2天或者一个小功能开发完毕)
	2 临时遇到bug？
		创建debug分支
	3 是否做代码的review？
		-创建review分支
		-组长
	4 如何给NB的项目贡献代码？
		-fork
		-pull request
3 其他部分
	1 PIL
		-python创建图片
		-画内容
	2 HTTPResponse 写字节
	3 
今日内容：
1 上传文件/上传头像
	a.定制上传按钮
	b.图片预览
		Dom和Jquery对象如何转换？
		dom -> jquery  
			let v = document.getElementById("avatarImg")
			$(v)
		jquery -> dom
			$("#avatar")[0]
		
		方式一:createObjectURL
					
		方式二:FileReader
		
		方式三:FormData
			图片预览，基于ajax上传文件   兼容性不太好
		方式四:Iframe(兼容性最好)
			1.iframe标签
				可以修改src，且页面不刷新
			2.form表单
				
			
2 CBV
3 中间件 

