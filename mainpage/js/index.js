window.onload = function () {
	var a1 = document.getElementById("a1");
	var a2 = document.getElementById("a2");
	var a3 = document.getElementById("a3");
	var a4 = document.getElementById("a4");
	var a5 = document.getElementById("a5");
	var btn = document.getElementById("btn");
	var output = document.getElementById("output");
	var another = document.getElementById("another");
	var yon = document.getElementById("yon");
	var copy = document.getElementById("copy");

	btn.onclick = function () {
		if (a3.value == "" && a4.value == "" && a5.value == "") {
			var result =
				"https://sub-converter.geniucker.top/sub?url=" +
				a1.value +
				"&interval=" +
				a2.value;
		} else {
			result =
				"https://sub-converter.geniucker.top/sub?url=" +
				a1.value +
				"&zjuport=" +
				a3.value +
				"&zjusocksuser=" +
				a4.value +
				"&zjusockspassword=" +
				a5.value;
		}
		output.value = result;
	};

	copy.onclick = function () {
		output.select();
		document.execCommand("copy");
	};
};
