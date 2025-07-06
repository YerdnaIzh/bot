import requests
import config

def config_request(part_request, params=None):
	headers = {
		"accept": "application/json",
		"X-API-KEY": config.API_TOKEN
	}
	url = f'{config.BASE_URL}/v1.4/movie/{part_request}'
	response = requests.get(url, headers=headers, params=params)
	if response.status_code == 200:
		return response.json()
	else:
		return {'error': f'Error: {response.status_code}'}

def print_film(movie):
	title = movie['name']
	year = movie['name']
	description = movie['description']
	rating = movie['rating']['kp']
	poster_url = movie['poster']['url']

	message = (
	f"**{title}** ({year})\n"
	f"Rating: {rating}\n"
	f"Description: {description}\n"
	f"\n![Poster]({poster_url})"
	)

	return message


response = config_request("random")
print(response)
