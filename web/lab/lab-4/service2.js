var mysql = require('mysql');
var pool  = mysql.createPool({
    connectionLimit : 50,
    host: 'localhost',
    user: 'root',
    database: 'WebDb'
});

pool.query('SELECT * from category', function (error, results, fields) {
    if (error) throw error;
    console.log('The solution is: ', results);
});