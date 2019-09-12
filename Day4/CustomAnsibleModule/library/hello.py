#/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str', required=True),
            
        )
    )

    #The changed flag can be used to indicate ansible
    #Was there a change done on the system.
    #If changed=True then it will show it in yello color otherwise green color
    result = dict(
        output="Hello " + module.params['msg'],
        changed=False  
    )

    #This will be used to report a success
    module.exit_json(**result)
    
    #This will be used to report a failure
    #module.fail_json(msg="Fatal error")


if __name__ == '__main__':
    main()
