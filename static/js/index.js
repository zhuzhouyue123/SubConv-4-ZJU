window.onload = function () {
	var url = document.getElementById("inp-url");
	var interval = document.getElementById("inp-interval");
	var socksPort = document.getElementById("inp-socksPort");
	var socksUsername = document.getElementById("inp-socksUsername");
	var socksPassword = document.getElementById("inp-socksPassword");
	var btn = document.getElementById("btn");
	var output = document.getElementById("output");
	var copy = document.getElementById("copy");
	output.value = ""

	btn.onclick = function () {
		var result = window.location.protocol + "//" + window.location.host;
		if (url.value != "") {
			result += "/sub?url=" + url.value;
		}
		else {
			output.value = "订阅链接不能为空哦"
			return;
		}
		if (interval.value != "") {
			if (/^[1-9][0-9]*$/.test(interval.value)) {
				result += "&interval=" + interval.value;
			}
			else {
				output.value = "你输入的节点更新间隔不是正整数";
				return;
			}
		}
		if (socksPort.value != "") {
			if (/^[1-9][0-9]*$/.test(socksPort.value) && 1 <= socksPort.value && socksPort.value <= 65535) {
				result += "&zjuport=" + socksPort.value;
			}
			else {
				output.value = "你输入的端口号不是1~65535的整数";
				return;
			}
			if (socksUsername.value != "") {
				result += "&zjusocksuser=" + socksUsername.value;
			}
			if (socksPassword.value != "") {
				result += "&zjusockspasswd=" + socksPassword.value;
			}
		}
		output.value = result;
	};

	copy.onclick = function () {
		output.select();
		document.execCommand("copy");
		navigator.clipboard.writeText(output.value);
		alert("复制成功！")
	};
};
