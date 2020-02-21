var express = require('express');
var multer = require('multer');
var app = express();



app.use(express.static('upload'))
var storage = multer.diskStorage({
  destination:function(req,file,callback){
    callback(null,'./upload');
  },
  filename:function(req,file,callback){
    callback(null,file.originalname);
  }

});


var upload = multer({storage:storage}).single('myfile');

var type = "0"
var name = "0"
var hour = "0"
var minute = "0"


app.get('/schedule',function(req,res){
  var obj = {type: type, name: name, hour:hour, minute:minute}
  res.send(JSON.stringify(obj));
});

app.get('/set_schedule',function(req,res){
  type = req.query.type;
  name = req.query.name;
  hour = req.query.hour;
  minute = req.query.minute;
  res.send('ok');
});


app.get('/',function(req,res){
  res.sendFile(__dirname + "/index.html");
});
app.post('/upload',function(req,res){
  upload(req,res,function(err){
    if(err){
      return res.end('Error uploading file');
    }
    res.end('File is upload successfully');
  });
});

app.listen(8080,function(){
  console.log('server is running or port 8080');
});