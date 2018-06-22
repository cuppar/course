let mysql = require('mysql');
let connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    database: 'WebDb'
});

connection.connect();

connection.query("SELECT id,cname from category where id=2 or cname='热点新闻'", function (error, results, fields) {
    if (error) throw error;
    console.log('The solution is: ', results);
    console.log('The solution is: ', results[0].Cname);
});

connection.query("insert into News(Title,Body,createTime,catagoryId) values('测试新闻3','测试内容3',now(),1)", function (error, results, fields) {
    if (error) throw error;

});

connection.query("insert into News(Title,Body,createTime,catagoryId) values('测试新闻1','测试内容1',now(),1)", function (error, results, fields) {
    if (error) throw error;

});

connection.end();