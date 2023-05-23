window.onload = function () {
	var url = document.getElementById("inp-url");
	var interval = document.getElementById("inp-interval");
	var btn = document.getElementById("btn");
	var output = document.getElementById("output");
	var copy = document.getElementById("copy");
	output.value = "";
	
	btn.onclick = function () {
		var result = window.location.protocol + "//" + window.location.host;
		if (url.value != "") {
			result += "/sub?url=" + encodeURIComponent(url.value);
		}
		else {
			output.value = "订阅链接不能为空哦";
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
		output.value = result;
	};

	copy.onclick = function () {
		output.select();
		document.execCommand("copy");
		navigator.clipboard.writeText(output.value);
		alert("复制成功！")
	};
};
