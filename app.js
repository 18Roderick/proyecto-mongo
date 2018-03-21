const http = require('http');
const request = require('request');
var urls = [
	"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Nicotiana%20tabacum",
	"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Escherichia%20coli",
	"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Cannabis%20sativa",
	"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Botryococcus%20braunii"
]
var options = {
	url : urls[0],
	headers:{
		"Accept": "application/json"
	}
}

request(options, (error, response, body) => {
	console.log('error:', error); // Print the error if one occurred
	//console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
	console.log('body:', body); // Print the HTML for the Google homepage.
	body.forEach( (data ) => {
		console.log(data)
	})
})