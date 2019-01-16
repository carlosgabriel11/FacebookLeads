const express = require('express')
const bodyParser = require('body-parser')
const request = require('request')
const app = express()

const token = process.env.FB_VERIFY_TOKEN
const access = process.env.FB_ACCESS_TOKEN

app.set('port', (process.env.PORT || 5000))

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

app.get('/', function(req, res){
	res.send('Hello Youtube!')
})

app.get('/webhook', function(req, res){
	if(req.query['hub.verify_token'] ===
		token){
			res.send(req.query['hub.challenge'])
		}

	res.send('No Entry')
})

app.post('/webhook', function (req, res){
	var data = req.body;

	//make sure this is a page subscription
	if(data.object === 'page'){

		//iterate over each entry - there may me muliple if batched
		data.entry.forEach(function(entry){
			var pageID = entry.id;
			var timeOfEvent = entry.time;

			//iterate over each messaging event
			entry.messaging.forEach(function(event){
				if(event.message){
					receivedMessage(event);
				}
				else{
					console.log("Webhook received unknown event: ", event);
				}
			});
		});

		//assume all went well
		//
		//you must send back a 200, within 20 seconds, to let us know
		//you've successfully received a callback. Otherwise, the request
		//will timeout and we will keep trying to resend.
		res.sendStatus(200);
	}
});

function receivedMessage(event){
	//putting a stub now, we'll expand it in the following steps
	//console.log("message data: ", event.message);

	var senderID = event.sender.id;
	var recipientID = event.recipient.id;
	var timeOfMessage = event.timestamp;
	var message = event.message;

	console.log("Received message for user %d and page %d at %d with message: ", senderID, recipientID, timeOfMessage);
	console.log(JSON.stringify(message));

	var messageId = message.mid;

	var messageText = message.text;
	var messageAttachments = message.attachments;

	if(messageText) {
		//if we receive a text message, check to see if it matched a keyword
		//and send back the example. Otherwise, just echo the text we received

		switch(messageText){
			case 'generic':
				sendGenericMessage(senderID);
				break;

			case 'telefone':
				sendTextMessage(senderID, "5512345678");
				break;

			default:
				sendTextMessage(senderID, messageText);
		}
	}
	else if (messageAttachments){
		sendTextMessage(senderID, "Message with attachment received");
	}
}

function senedGenericMessage(recipientID, messageText){
	//to be expanded later
}

function sendTextMessage(recipientId, messageText){
	var messageData = {
		recipient: {
			id:recipientId
		},
		message: {
			text:messageText
		}
	};

	callSendAPI(messageData);
}

function callSendAPI(messageData){
	request({
		uri: 'https://graph.facebook.com/v2.6/me/messages',
		qs: { access_token: access},
		method: 'POST',
		json: messageData
	}, function(error, response, body){
		if(!error && response.statusCode == 200){
			var recipientId = body.recipient_id;
			var messageId = body.message_id;

			console.log("Sucessfully sent genetic message with id %s to recipient %s",
				messageId, recipientId);
		} else{
			console.error("Unable to send message.");
			console.error(response);
			console.error(error);
		}
	})
}

app.listen(app.get('port'), function(){
	console.log('running on port', app.get('port'))
})