from constants import (core_helm_path, core_tf_path, docs_path,
                       environments_production_common,
                       environments_production_k8s_projects,
                       environments_production_tf_projects,
                       environments_staging_common,
                       environments_staging_k8s_projects,
                       environments_staging_tf_projects,
                       projects_k8s_path,
                       projects_tf_path,
                       seperator)
from os import chdir, makedirs, path, system


def create_project(name: str):
    root_folder = seperator.join(['.', name])
    
    if path.exists(root_folder):
        print(f'Folder {root_folder} already exists!')
        return
    
    # system('git-crypt init')
    # with open(seperator.join(root_folder, '.gitattributes'), 'w') as f:
    #    f.write('./environments/**/*secrets* filter=git-crypt diff=git-crypt')
    
    try:
        makedirs(root_folder)
    except:
        print(f'Creating {root_folder} failed.')
        return
    
    paths = [core_helm_path,
                core_tf_path,
                docs_path,
                environments_production_common,
                environments_production_k8s_projects,
                environments_production_tf_projects,
                environments_staging_common,
                environments_staging_k8s_projects,
                environments_staging_tf_projects,
                projects_k8s_path,
                projects_tf_path]
    
    try:
        chdir(root_folder)
        for folder_path in paths:
            makedirs(folder_path)
    except:
        print('Failed to create subfolders.')
        return
    
    with open(seperator.join([core_helm_path, 'default-values.yaml']), 'w'): pass
    with open(seperator.join([core_tf_path, 'main.tf']), 'w'): pass
    
    with open(seperator.join([environments_production_common, 'values.yaml']), 'w'): pass
    with open(seperator.join([environments_production_common, 'secrets.yaml']), 'w'): pass
    with open(seperator.join([environments_staging_common, 'values.yaml']), 'w'): pass
    with open(seperator.join([environments_staging_common, 'secrets.yaml']), 'w'): pass
    
    with open(seperator.join([environments_production_k8s_projects, 'values.yaml']), 'w'): pass
    with open(seperator.join([environments_production_k8s_projects, 'secrets.yaml']), 'w'): pass
    with open(seperator.join([environments_production_tf_projects, 'values.tfvars']), 'w'): pass
    with open(seperator.join([environments_production_tf_projects, 'secrets.tfvars']), 'w'): pass
    with open(seperator.join([environments_staging_k8s_projects, 'values.yaml']), 'w'): pass
    with open(seperator.join([environments_staging_k8s_projects, 'secrets.yaml']), 'w'): pass
    with open(seperator.join([environments_staging_tf_projects, 'values.tfvars']), 'w'): pass
    with open(seperator.join([environments_staging_tf_projects, 'secrets.tfvars']), 'w'): pass
    
    with open (seperator.join([projects_k8s_path, 'deployment.yaml']), 'w'): pass
    with open (seperator.join([projects_tf_path, 'main.tf']), 'w'): pass
