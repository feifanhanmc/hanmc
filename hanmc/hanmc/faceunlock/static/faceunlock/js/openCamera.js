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
	
		var dataUrl = aCanvas.toDataURL("image/png");	// 'data:image/jpeg;base64,/9j/4AA	QSk...(base64编码)...'
		$.ajax({
			type: 'POST',
			url: 'add_faceset/',
			data: {dataUrl: dataUrl},
			// success: function(){
			// 	alert('设置成功');
			// 	window.location.href="index/";
			// }
		});
	});
}