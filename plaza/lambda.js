let AWS = require('aws-sdk');
exports.handler = function(event, context, callback) {

	console.log("Event: " + JSON.stringify(event));
	console.log("Context: " + JSON.stringify(context));

	callback(null,'Successfully executed');
}