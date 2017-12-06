from fabric.api import run
from fabric.context_managers import env


#env.password = "PASSWORD"


def iso():
    run('date -u')


