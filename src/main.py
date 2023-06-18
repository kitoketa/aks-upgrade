#!/usr/bin/env python

from os import environ
import subprocess
from subprocess import PIPE

def main():
    name = environ.get('INPUT_NAME')
    resource_group = environ.get('INPUT_RESOURCE_GROUP')
    kubernetes_version = environ.get('INPUT_KUBERNETES_VERSION')
    control_plane_only = environ.get('INPUT_CONTROL_PLANE_ONLY', False)
    no_wait = environ.get('INPUT_NO_WAIT', False)
    node_image_only = environ.get('INPUT_NODE_IMAGE_ONLY', False)

    ACCOUNT_LIST = [
        'az',
        'account',
        'list'
    ]
    print('run account list')
    result = subprocess.run(ACCOUNT_LIST, stdout=PIPE, stderr=PIPE, text=True)
    print(result.stdout)

    # ACCOUNT_SET = [
    #     'account',
    #     'set',
    #     '--subscription', '1e6bd428-8625-4f07-bb44-f3f6a2dd5315'
    # ]
    # print('run account set')
    # cli.invoke(ACCOUNT_SET)

    # AKS_GET_CREDENTIALS = [
    #     'aks',
    #     'get-credentials',
    #     '--resource-group', resource_group,
    #     '--name', name
    # ]
    # print('run aks get-credentials')
    # cli.invoke(AKS_GET_CREDENTIALS)

    # AKS_UPGRADE = [
    #     'aks',
    #     'upgrade',
    #     '--name', name,
    #     '--subscription', '1e6bd428-8625-4f07-bb44-f3f6a2dd5315',
    #     '--resource-group', resource_group,
    #     '--kubernetes-version', kubernetes_version,
    #     # '--control_plane_only',
    #     # '--no_wait',
    #     # '--node_image_only',
    #     '--yes'
    # ]
    # print('run aks upgrade')
    # cli.invoke(AKS_UPGRADE)

    # TODO エラー処理

if __name__ == '__main__':
    main()
