import os

from resemble import Resemble

Resemble.api_key(os.getenv('RESEMBLE_API_KEY'))

page = 1
page_size = 100

clip = Resemble.v2.projects.all(page, page_size)
projects = clip['items']
print(projects)

project_uuid = '25022e82' # Earth's default project
voice_uuid = 'c54347f8' # Junior
callback_uri = 'https://webhook.site/a5aa7c50-d5ed-4f34-9b0e-5202165e6f72'
body = 'This is a sync test'

clip = Resemble.v2.clips.create_async(
  project_uuid,
  voice_uuid,
  callback_uri,
  body,
  title=None,
  sample_rate=None,
  output_format=None,
  precision=None,
  include_timestamps=None,
  is_public=None,
  is_archived=None
)

print(clip)
