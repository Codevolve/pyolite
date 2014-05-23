import re


class Repo(object):
  def __init__(self, path):
    self.path = path

  def replace(self, pattern, string):
    with open(str(self.path), 'r+') as f:
      content = f.read()
      content = re.sub(pattern, string, content)
      f.seek(0)
      f.write(content)
      f.truncate()

  @property
  def users(self):
    users = []

    with open(str(self.repo_config)) as f:
      config = f.read()
      for match in re.compile('=( *)(\w+)').finditer(config):
        users.append(match.group(2))

    return users

  def write(self, string):
    with open(self.path) as f:
      f.write(string)
