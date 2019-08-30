import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_terraform_user_created(host):
    user = host.user("terraform")
    assert user.name == "terraform"
    assert "terraform" in user.groups


def test_is_terraform_bin_installed(host):
    command = host.run("terraform -version")
    assert "Terraform v" in command.stdout


def test_is_awscli_bin_installed(host):
    command = host.run("aws --version")
    # trick to work in both ubuntu and centos
    assert ("aws-cli" in command.stdout) or ("aws-cli" in command.stderr)
