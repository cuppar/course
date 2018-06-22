$(document).ready(function () {
  let panel = $('.wrap-5-main')
  $.ajax({
    type: 'get',
    url: 'http://127.0.0.1:8080/listNews',
    success: function (response) {
      if (response['success'] === true) {
        let news = response['result']
        $.each(news, function (index, aNew) {
          let html = '<pre><a href="#">'
          let title = aNew['title']
          let body = aNew['body']
          let catagoryId = aNew['category_id']
          html += 'title: ' + title + ' \tbody: ' + body + ' \t分类: ' + catagoryId + '</a></pre><br>'
          panel.append(html)
        })
      }
    }
  })
})