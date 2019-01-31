How to run playbook:
```sh
ansible-playbook deploy_chrony_birdpis.yml --limit "box1cam" -i inventory.yml -K
```
--limit limits which host the playbook should be run at. If not specified, all hosts in inventory will be used.
-i specifies which inventory to use
-l asks for sudo password

To execute a command on one or more boxes:
```sh
ansible -i inventory.yml all --limit='box1output,box2output,box2cam' -a "apt-get install gstreamer-1.0 -y " -K
```
