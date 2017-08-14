window.onload = function(){
	var aVideo=document.getElementById('video');
	var aCanvas=document.getElementById('canvas');
	var ctx=aCanvas.getContext('2d');

	 
	navigator.getUserMedia = navigator.getUserMedia ||	navigator.webkitGetUserMedia ||	navigator.mozGetUserMedia || navigator.msGetUserMedia;//获取媒体对象（这里指摄像头）
	navigator.getUserMedia({video:true}, gotStream, noStream);//参数1获取用户打开权限；参数二成功打开后调用，并传一个视频流对象，参数三打开失败后调用，传错误信息
	 
	function gotStream(stream) {
		video.src = URL.createObjectURL(stream);
		video.onerror = function () {
			stream.stop();
		};
		stream.onended = noStream;
		video.onloadedmetadata = function () {
			console.log('摄像头成功打开！');
		};
	}

	function noStream(err) {
		alert(err + '，换个浏览器试试');
	}

	document.getElementById("snap").addEventListener("click", function() {
		ctx.drawImage(aVideo, 0, 0, 640, 480);//将获取视频绘制在画布上

		// var image_base64 = aCanvas.toDataURL("image/png");	// 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'
		
		// var url = 'https://api-cn.faceplusplus.com/facepp/v3/detect';
		// var value = {'api_key' : 'FR2qXQzfPwSzjZNC1KSdQBiJD8h_sVIx',
  //               'api_secret' : '0M7jG1b4nxdp6eBH8nnirkcefUWD91C-',
  //               'image_base64' : image_base64,
  //               'return_attributes' : 'gender'
  //       }
		// var request;
		// if (window.XMLHttpRequest) {
		// 	request = new XMLHttpRequest();
		// } 
		// else {
		// 	request = new ActiveXObject('Microsoft.XMLHTTP');
		// }
		// request.open('PUT', url, true);
	 //    request.setRequestHeader('X-Custom-Header', value);
	 //    request.send();

	 //    if (request.readyState === 4) { // 成功完成
	 //        if (request.status === 200) {	// 判断响应结果:  
	 //            console.log(request.responseText);	// 成功，通过responseText拿到响应的文本:
	 //        } 
	 //        else {
	 //            console.log('code : ' + request.status);	// 失败，根据响应码判断失败原因:
	 //        }
	 //    } 
	});
}