# Configuración de los entornos

## Requisitos mínmos:

- Ansible 5.7.1, con `ansible-core 2.12.5`
- Dos máquinas virtuales con Ubuntu Server con direcciones IP estáticas, en este caso 192.168.1.7 para el control plane y 192.168.1.9 para el worker.

## Comandos de ansible:

`ansible-playbook -i inventario -K main.yml`