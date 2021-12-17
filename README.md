# JupyterHub JupyterLab RTC demo

This is a demo of configuring JupyterHub to support [JupyterLab Real Time Collaboration](https://jupyterlab.readthedocs.io/en/stable/user/rtc.html).

See https://discourse.jupyter.org/t/plans-on-bringing-rtc-to-jupyterhub/9813/5

**WARNING: This uses unreleased features of JupyterHub. The configuration is only for demo purposes and is insecure.**


## Installation

Clone this repository:
```
git clone https://github.com/manics/jupyterhub-rtc-example.git
```

Install JupyterHub's dependencies including configurable-http-proxy:
```
cd jupyterhub-rtc-example
conda env create -n jupyterhub-rtc --file environment.yml
```
Activate the environment, then install JupyterHub from GitHub using pip:
```
conda activate jupyterhub-rtc
pip install git+https://github.com/jupyterhub/jupyterhub.git@main#egg=jupyterhub
```
(Last tested with `git+https://github.com/jupyterhub/jupyterhub.git@3800ceaf9edf33a0171922b93ea3d94f87aa8d91#egg=jupyterhub`)


## Run JupyterHub

Activate environment
```
conda activate jupyterhub-rtc
cd jupyterhub-rtc-example
```
Run JupyterHub:
```
jupyterhub --config jupyterhub_config.py
```


## Login

Go to http://localhost:8000 and login as `user-1` with any password.
You should be in JupyterLab.
Create a new Python notebook.

In a different browser or incognito window go to http://localhost:8000 and login as `user-2` with any password.
You should see your own JupyterLab separate from `user-1`.

Copy `user-1`'s JupyterLab notebook URL into `user-2`'s browser.
Click `Authorize` if prompted.
You should now have an RTC connection to `user-1`'s server!

If you logout, and login as `user-3`, you should *not* have access to anyone else's server.


## How this works

This uses JupyterHub's new [*Role Base Access Control (RBAC)*](https://jupyterhub.readthedocs.io/en/rbac/rbac/) which will be part of JupyterHub 2.
RBAC allows very fine-grained control of permissions in JupyterHub.
In this example users who are part of a group `rtc` are given the `access:servers` permission, which allows them to access the servers of any other user in the `rtc` group.

See `c.JupyterHub.load_roles` in [`jupyterhub_config.py`](./jupyterhub_config.py#L20).
