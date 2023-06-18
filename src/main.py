#!/usr/bin/env python

from os import environ
from azure.cli.core import get_default_cli

def main():
    name = environ.get('INPUT_NAME')
    resource_group = environ.get('INPUT_RESOURCE_GROUP')
    kubernetes_version = environ.get('INPUT_KUBERNETES_VERSION')
    control_plane_only = environ.get('INPUT_CONTROL_PLANE_ONLY', False)
    no_wait = environ.get('INPUT_NO_WAIT', False)
    node_image_only = environ.get('INPUT_NODE_IMAGE_ONLY', False)
    
    cli = get_default_cli()

    AKS_GET_CREDENTIALS = [
        'aks get-credentials',
        '--resource-group', resource_group,
        '--name', name
    ]
    cli.invoke(AKS_GET_CREDENTIALS)

    AKS_UPGRADE = [
        'aks upgrade',
        '--name', name,
        '--resource-group', resource_group,
        '--kubernetes-version', kubernetes_version,
        '--control_plane_only', control_plane_only,
        '--no_wait', no_wait,
        '--node_image_only', node_image_only,
        '--yes', 'True'
    ]
    cli.invoke(AKS_UPGRADE)

    # TODO エラー処理

if __name__ == '__main__':
    main()
