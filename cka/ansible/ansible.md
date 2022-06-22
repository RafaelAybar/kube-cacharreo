# Configuración de los entornos

## Requisitos mínmos:

- Ansible 5.7.1, con `ansible-core 2.12.5`
- Dos máquinas virtuales con Ubuntu Server con direcciones IP estáticas, en este caso 192.168.1.7 para el control plane y 192.168.1.9 para el worker. (pendiente de migrar a  Vagrant)

## Comandos de ansible:

`ansible-playbook -i inventario -K main.yml`

## Instalación de Cálico:

[Documentación oficial](https://projectcalico.docs.tigera.io/getting-started/kubernetes/quickstart)