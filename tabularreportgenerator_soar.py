import requests


def get_custom_list(connector, custom_list_name):
    phantom_base_url = connector.get_phantom_base_url()
    url = f"{phantom_base_url}rest/decided_list/{custom_list_name}/formatted_content?_output_format=csv&_fs=,&_rs=%0A"
    r = requests.get(url, verify=False)
    r.raise_for_status()
    custom_list = r.content.decode('utf-8-sig')
    return custom_list
