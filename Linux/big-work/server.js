let express = require('express')
let app = express()
let bodyParser = require('body-parser')
let fs = require('fs')
let cookieParser = require('cookie-parser')
let users = []
let msgs = []

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
  extended: true
}))
app.use(cookieParser())

fs.readFile('./user.json', function (err, data) {
  if (err) {
    console.log('read user.json err:', err)
    return
  }
  if (data != false) {
    console.log('user.json:', data)
    users = JSON.parse(data)
    console.log('parsed user.json:', users)
  }
})

fs.readFile('./msg.json', function (err, data) {
  if (err) {
    console.log('read msg.json err:', err)
    return
  }
  if (data != false) {
    console.log('msg.json:', data)
    msgs = JSON.parse(data)
    console.log('parsed msg.json:', msgs)
  }
})

app.use(function (req, res, next) {
  res.set({
    'Access-Control-Allow-Origin': '*'
  })
  res.set({
    'Access-Control-Allow-Headers': '*'
  })
  res.set({
    'Access-Control-Allow-Credentials': 'true'
  })
  next()
})

app.post('/login', function (req, res) {
  let login_success = false
  let username = req.body.username
  let password = req.body.password
  users.forEach(one => {
    if (one['username'] === username &&
      one['password'] === password) {
      login_success = true
    }
  })
  res_content = login_success ? {
    success: true,
    message: '登录成功',
    username: username
  } : {
    success: false,
    message: '用户名或密码错误'
  }
  console.log('res_content', res_content)
  return res.json(res_content)
})

app.post('/signup', function (req, res) {
  let samename = false
  let username = req.body.username
  let password = req.body.password
  users.forEach(one => {
    if (one['username'] === username) {
      samename = true
    }
  })
  if (!samename) {
    users.push({
      username: username,
      password: password
    })
    fs.writeFile('./user.json', JSON.stringify(users), function (err) {
      if (err) {
        console.log(err)
      }
    })
  }
  res_content = samename ? {
    success: false,
    message: '用户名已存在'
  } : {
    success: true,
    message: '注册成功'
  }
  console.log('res_content', res_content)
  return res.json(res_content)
})

app.post('/message', function (req, res) {
  let from = req.body.from
  let to = req.body.to
  let msg = req.body.msg
  let time = req.body.time
  let res_content = {}

  if (from != false && to != false && msg != false) {
    msgs.push({
      from: from,
      to: to,
      msg: msg,
      time: time
    })
    fs.writeFile('./msg.json', JSON.stringify(msgs), function (err) {
      if (err) {
        console.log('write msg.json err:', err)
        return
      }
    })
    res_content = {
      success: true,
      message: '留言成功'
    }
  } else {
    res_content = {
      success: false,
      message: '留言失败，请登录后同时填写留言内容及收信人'
    }
  }
  console.log(from + ' say ' + msg + ' to ' + to + ' in ' + new Date(time).toLocaleString())
  return res.json(res_content)
})

let server = app.listen(3000, function () {
  let host = server.address().address
  let port = server.address().port

  console.log('app listening at http://%s:%s', host, port)
})