/**
 * Created by hezhenli on 2017/3/2.
 */
//判断是否有SQL注入
let sqlValid = function (sqlText) {
    let re = /select|update|delete|exec|count|'|;|>|<|%/i;
    return !re.test(sqlText);
};

//判断是否可以查询
let selectValid = function (sqlText) {
    return !(sqlText.toLowerCase().indexOf('select') < 0 || sqlText.toLowerCase().indexOf('insert') >= 0
    || sqlText.toLowerCase().indexOf('update') >= 0 || sqlText.toLowerCase().indexOf('delete') >= 0
    || sqlText.toLowerCase().indexOf('exec') >= 0);
};

//判断是否可以执行某个命令
let execValid = function (sqlText) {
    return ( sqlText.toLowerCase().indexOf('insert') >= 0 || sqlText.toLowerCase().indexOf('update') >= 0
    || sqlText.toLowerCase().indexOf('delete') >= 0 || sqlText.toLowerCase().indexOf('exec') >= 0);
};

exports.sqlValid = sqlValid;
exports.selectValid = selectValid;
exports.execValid = execValid;
