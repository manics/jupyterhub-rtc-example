# Configuration file for jupyterhub.

# Insecure! Dummy authenticator accepts any password
c.JupyterHub.authenticator_class = 'dummy'

# 3 users, 2 are placed in group "rtc"
c.Authenticator.allowed_users = set([
  'user-1',
  'user-2',
  'user-3'
])
c.JupyterHub.load_groups = {
  'rtc': [
    'user-1',
    'user-2',
  ]
}

# Allow users in group "rtc" to access the servers of other users in that group
c.JupyterHub.load_roles = [
  {
    'name': 'rtc-group',
    'description': 'can access other users servers in rtc group',
    'scopes': ['access:servers!group=rtc'],
    'groups': ['rtc'],
  },
]

# Insecure! just for easy testing
c.JupyterHub.spawner_class = 'simple'

# singleuser-server: jupyterlab with rtc enabled
c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.args = ['--collaborative']

# Debug logging?
# c.Application.log_level = 'DEBUG'
# c.Spawner.debug = True
