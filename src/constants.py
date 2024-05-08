from sys import platform

seperator = None
if platform == 'Windows':
    seperator = '\\'
else:
    seperator = '/'

core_tf_path = seperator.join(['.', 'src', 'core', 'terraform', 'example-component'])
core_helm_path = seperator.join(['.', 'src', 'core', 'helm', 'example-component'])
docs_path = seperator.join(['.', 'docs'])
environments_staging_common = seperator.join(['.', 'environments', 'staging', 'common'])
environments_staging_k8s_projects = seperator.join(['.', 'environments', 'staging', 'example-project', 'example-component-k8s'])
environments_staging_tf_projects = seperator.join(['.', 'environments', 'staging', 'example-project', 'example-component-terraform'])
environments_production_common = seperator.join(['.', 'environments', 'production', 'common'])
environments_production_k8s_projects = seperator.join(['.', 'environments', 'production', 'example-project', 'example-component-k8s'])
environments_production_tf_projects = seperator.join(['.', 'environments', 'production', 'example-project', 'example-component-terraform'])
projects_k8s_path = seperator.join(['.', 'src', 'projects', 'example-project', 'k8s', 'example-component'])
projects_tf_path = seperator.join(['.', 'src', 'projects', 'example-project', 'terraform', 'example-component'])
