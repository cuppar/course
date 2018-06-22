let express = require('express')
let app = express(); // 加载express

app.use(express.static(__dirname + '/public'))

// // 设置启动端口
let port = 8080
let bodyParser = require('body-parser'); // 加载form表单提交转换json模块

// 用body parser 来解析post和url信息中的参数
app.use(bodyParser.urlencoded({
    limit: '50mb',
    extended: true
}))
app.use(bodyParser.json({
    limit: '50mb'
}))

//中间件
app.use('*', function (req, res, next) {
    res.set('Access-Control-Allow-Origin', '*')
    res.set('Access-Control-Allow-Headers', '*')
    next()
})

// 加载SQL数据获取执行模块
let mdb = require('./local_modules/MariaDbHelper')
// 加载SQL验证模块
let valid = require('./local_modules/antiSqlValid.js')
// =======================
// 路由 ================
// =======================
// 基础路由
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/' + 'public/index.html')
})
app.get('/signUp', function (req, res) {
    res.sendFile(__dirname + '/' + 'public/signUp.html')
})
app.post('/addUser', function (req, res) {
    let sql = 'insert into user(user_id, user_name, password)\
      value(' + 0 + ', "' + req.body.username + '", "' + req.body.password + '")'
    mdb.query(sql, function (err, result) {
        if (err) {
            return res.json({
                success: false,
                message: err.message
            })
        }
        return res.json({
            message: '注册成功！',
            success: true,
            result: result
        })
    })
})
app.post('/login', function (req, res) {
    let sql = 'select user_name,password from user'
    let username_input = req.body.username
    let password_input = req.body.password

    resultObj = mdb.query(sql, function (err, result) {
        if (err) {
            return res.json({
                success: false,
                message: err.message
            })
        }
        let resultObj = {
            message: '登录失败，用户名或密码错误。',
            success: false
        }
        result.forEach((value, index, self) => {
            if (value['user_name'] == username_input &&
                value['password'] == password_input) {
                resultObj = {
                    message: '登录成功！',
                    success: true,
                    user: value['user_name']
                }
            }
        })
        return res.json(resultObj)
    })
})

app.get('/listNews', function (req, res) {
    let sql = 'select * from news'
    if (!valid.selectValid(sql)) {
        console.log('该方法只可以执行查询操作!')
    }
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({
                        success: false,
                        message: err.message
                    })
                }

                return res.json({
                    success: true,
                    result: result
                })
            }
        )
    } catch (e) {
        return res.json({
            success: false,
            message: e.message
        })
    }
})
app.get('/publish', function (req, res) {
    res.sendFile(__dirname + '/' + '/public/addNew.html')
})

app.post('/addNew', function (req, res) {
    let title = req.body.title
    let content = req.body.body
    let catagoryId = req.body.catagoryId

    let sql = 'insert into news(news_id,title,body,category_id)\
     values(' + 0 + ',"' + title + '","' + content + '",' + parseInt(catagoryId) + ')'
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({
                        success: false,
                        message: err.message
                    })
                }
                return res.json({
                    message: '发布成功！',
                    success: true,
                    result: result
                })
            }
        )
    } catch (e) {
        return res.json({
            success: false,
            message: e.message
        })
    }
})

app.post('/deleteNew', function (req, res) {
    let deleteId = req.body.deleteId

    let sql = "delete from news where id ='" + deleteId + "'"
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({
                        success: false,
                        message: err.message
                    })
                }
                return res.json({
                    success: true,
                    result: result
                })
            }
        )
    } catch (e) {
        return res.json({
            success: false,
            message: e.message
        })
    }
})

// =======================
// 启动服务 ======
// =======================
let server = app.listen(port, function () {
    let host = server.address().address
    let port = server.address().port
    console.log('服务启动，访问地址: http://%s:%s', host, port)
})