let configObj = require("../config.json");//读取配置文件
let mysql = require('mysql');
let pool  = mysql.createPool({
    connectionLimit : 50,
    host: configObj.mariaDbAddress,
    user: configObj.mariaDbUser,
    database: configObj.mariaDbDatabase,
    connectTimeout: 150000,
    password: 'root'
});

// 方法支持一种模式
// 只传入SQL语句和回调函数
exports.query = function (sql, C) {
    let params = [];
    let callback;

    // 如果用户传入了两个参数，就是SQL和callback
    if (arguments.length === 2 && typeof arguments[1] === 'function') {
        callback = C;
    } else {
        throw new Error('对不起，参数个数不匹配或者参数类型错误');
    }

    pool.query(sql, callback);


};