

const http = require("https");

// function myFunction() {

const options = {
	"method": "GET",
	"hostname": "api.ambeedata.com",
	"port": null,
	"path": "/latest/by-city?city=Delhi",
	"headers": {
		"x-api-key": "mqoZ9hQjIi3ZqydD8W3lU7fGnXJ5ndJI44sAUusN",
		"Content-type": "application/json"
	}
};

const req = http.request(options, function (res) {

	res.setEncoding('utf8');

	const chunks = [];

	res.on("data", function (chunk) {
		chunks.push(chunk);
		// chunks.push(chunk.toString('utf8'));
	});

	

	res.on("end", function () {

		console.log("chunkssssssssssss",chunks)
		const body = Buffer.concat(chunks);

		console.log(typeof(chunks))
		// console.log(chunks[0])

		// $.ajax({
		// 	method: "POST",
		// 	url: "/api_data",
		// 	data: ody.toString()
		// })
		// .done(function(response){
		// 	console.log(response)
		// })
		// .fail(function(){
		// 	console.log(response)
		// })

		// console.log(body.toString());
		// var new_o = JSON.stringify(body.toString())

		var dict = body

		console.log(dict)
		// console.log(dict["message"]);
		// console.log(typeof (dict))
		// console.log(typeof(body.toString()))
		// var za = body.parse(body.contents).bpi.USD.rate_float;
		// var za1 = JSON.parse(new_o.contents).stations.PM10;
		// var za2 = JSON.parse(new_o.contents).stations.NO2;
		// var za3 = JSON.parse(new_o.contents).stations.Ozone;
		// var za4 = JSON.parse(new_o.contents).stations.SO2;
		// var za5 = JSON.parse(new_o.contents).stations.AQI;
		// var za6 = JSON.parse(new_o.contents).stations.AQI;
		// var za7 = JSON.parse(new_o.contents).stations.updatedAt;

		// console.log(za)
		// console.log(za2)
		// console.log(za3)
		// console.log(za4)
		// console.log(za5)
		// console.log(za6)
		// console.log(za7)

	});
});

req.end();

// }
 