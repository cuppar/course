let express = require('express');
let app = express(); //加载express
// 设置启动端口
let port = 8080;
let bodyParser = require('body-parser');//加载form表单提交转换json模块

//用body parser 来解析post和url信息中的参数
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(bodyParser.json({limit: '50mb'}));

//加载SQL数据获取执行模块
let mdb = require("./local_modules/MariaDbHelper");
//加载SQL验证模块
let valid = require("./local_modules/antiSqlValid.js");
// =======================
// 路由 ================
// =======================
// 基础路由
app.get('/', function (req, res) {

    let sql = "select * from category";
    if (!valid.selectValid(sql)) {
        console.log('该方法只可以执行查询操作!');
    }
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({success: false, message: err.message});
                }
                return res.json({success: true, result: result});
            }
        );
    }
    catch (e) {
        return res.json({success: false, message: e.message});
    }
});


app.get('/News', function (req, res) {

    let sql = "select * from news";
    if (!valid.selectValid(sql)) {
        console.log('该方法只可以执行查询操作!');
    }
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({success: false, message: err.message});
                }
                return res.json({success: true, result: result});
            }
        );
    }
    catch (e) {
        return res.json({success: false, message: e.message});
    }
});

app.post('/addNews', function (req, res) {
    let title = req.body.title;
    let content = req.body.content;
    let catagoryId = req.body.catagoryId;

    let sql = "insert into News(Title,Body,createTime,catagoryId) values('" + title + "','" + content + "',now()," + catagoryId + ")"
    try {
        mdb.query(sql,
            function (err, result) {
                if (err) {
                    return res.json({success: false, message: err.message});
                }
                return res.json({success: true, result: result});
            }
        );
    }
    catch (e) {
        return res.json({success: false, message: e.message});
    }

});


// =======================
// 启动服务 ======
// =======================
app.listen(port);

