from ansible.module_utils.basic import AnsibleModule
import psutil, socket

def main():
    module = AnsibleModule(argument_spec={})
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    result = {
        "hostname": hostname,
        "ip": ip_address,
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk
    }

    module.exit_json(changed=False, ansible_facts=result)

if __name__ == '__main__':
    main()