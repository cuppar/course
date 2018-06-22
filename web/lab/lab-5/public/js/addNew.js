let addNew = function () {
  $.ajax({
    type: 'post',
    url: 'http://127.0.0.1:8080/addNew',
    contentType: 'application/json',
    data: JSON.stringify({
      title: $('#title_input').val(),
      body: $('#body_input').val(),
      catagoryId: $('#catagoryId_input').val()
    }),
    success: function (res) {
      let addNewResultDiv=$('#addNewResult')
      if(res.success===true){
        addNewResultDiv.html('<h3>发布成功！</h3>\
        <br>\
        <a href="http://127.0.0.1:8080/">返回首页</a>\
        <p>细节: '+JSON.stringify(res.result)+'</p>')
      }else{
        addNewResultDiv.html('<h3>发布失败！</h3>\
        <br>\
        <a href="http://127.0.0.1:8080/">返回首页</a>\
        <p>细节: '+res.message+'</p>')
      }
    }
  })
}