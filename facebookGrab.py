
def facebookGrab(profile):
	"""Get an access token from facebook and run: <export facebookAcessToken = 'your token'> in the command line."""
	import facebook
	import requests
	import os
	from index import havenSentiment
	import json

	results = []
	access_token = os.environ.get('facebookAcessToken')	
	user = profile
	graph = facebook.GraphAPI(access_token)
	app_id = os.environ.get('facebookAppId')
	app_secret = os.environ.get('facebookAppSecret')


	# Extend the expiration time of a valid OAuth access token.
	# extendedAccessToken = graph.extend_access_token(app_id, app_secret)
	# print extendedAccessToken
	profile = graph.get_object(user)
	posts = graph.get_connections(profile['id'], 'posts')



	# Wrap this block in a while loop so we can keep paginating requests until
	# finished.
	for i in range(5):
	    try:
	        # Perform some action on each post in the collection we receive from
	        # Facebook.
	        [results.append(post['message']) for post in posts['data']]
	        # Attempt to make a request to the next page of data, if it exists.
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        # When there are no more pages (['paging']['next']), break from the
	        # loop and end the script.
	        break
	return havenSentiment(json.dumps(results))

if __name__ == '__main__':
	print facebookGrab('BillGates')
