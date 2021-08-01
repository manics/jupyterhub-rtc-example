# Configuration file for jupyterhub.
import os

# Insecure! Dummy authenticator accepts any password
c.JupyterHub.authenticator_class = 'dummy'

c.Authenticator.admin_users = set([
  'admin',
])

allowed_users = [
  'user-1',
  'user-2',
  'user-3',
]

load_groups = {}
load_roles = []
for user in allowed_users:
    # Group and role that allows server access to user
    access_group_name = f'rtc-access-{user}'
    load_groups[access_group_name] = []
    load_roles.append({
        'name': access_group_name,
        'description': f'RTC access to {user}',
        'scopes': [f'access:servers!user={user}'],
        'groups': [access_group_name],
    })

    # Role that allows user to manage who can access their servers by adding/removing users from the group
    manage_name = f'rtc-manage-{user}'
    load_roles.append({
        'name': manage_name,
        'description': f'Manage users in group {access_group_name}',
        'scopes': [f'groups!group={access_group_name}'],
        'users': [user],
    })


c.Authenticator.allowed_users = set(allowed_users)
c.JupyterHub.load_groups = load_groups
c.JupyterHub.load_roles = load_roles


# Insecure! just for easy testing
c.JupyterHub.spawner_class = 'simple'
c.SimpleLocalProcessSpawner.home_dir_template = os.path.join(os.getcwd(), 'homedirs', '{username}')

# singleuser-server: jupyterlab with rtc enabled
c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.args = ['--collaborative']

# Debug logging?
# c.Application.log_level = 'DEBUG'
# c.Spawner.debug = True
