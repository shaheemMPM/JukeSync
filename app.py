from flask import Flask, Response, request
import os

app = Flask(__name__)


@app.route('/')
def index():
	return 'hello world'

@app.route('/video')
def video():
	video_path = '1.mp4'  # Adjust the path to your video file
	chunk_size = 1024 * 1024  # 1 MB (adjust as needed)

	# Check if the video file exists
	if not os.path.exists(video_path):
		return "Video file not found."

	# Retrieve the file size
	video_size = os.path.getsize(video_path)

	# Get the requested range from the HTTP headers
	range_header = request.headers.get('Range')
	if not range_header:
		return "Requires Range header", 400

	# Parse the range header
	start, end = range_header.replace('bytes=', '').split('-')
	try:
		start = int(start)
		end = int(end) if end else video_size - 1
	except ValueError:
		return "Invalid range values", 400
	
	if start < 0 or start >= video_size or end < start or end >= video_size:
		return "Invalid range values", 400

	# Calculate the content length for the response
	content_length = end - start + 1

	# Prepare the headers for the response
	headers = {
		'Content-Range': f'bytes {start}-{end}/{video_size}',
		'Accept-Ranges': 'bytes',
		'Content-Length': content_length,
		'Content-Type': 'video/mp4',
	}

	# Set the HTTP status code to 206 (Partial Content)
	response = Response(status=206, headers=headers)

	# Open the video file and seek to the start position
	with open(video_path, 'rb') as video_file:
		video_file.seek(start)

		# Stream the video data in chunks
		while start <= end:
			chunk = video_file.read(min(chunk_size, end - start + 1))
			response.stream.write(chunk)
			start += len(chunk)

	return response


if __name__ == '__main__':
	app.run(debug=True)
