#!/usr/bin/python3
import ipaddress
import os
import socket
import subprocess
import sys

import yaml

# We store all params we need in a list
# Params stored: 0 External IP 1 Domain name 2 Namespace 3 Issuername
paramsList = [sys.argv[1].strip(), sys.argv[2].strip(), sys.argv[3].strip(), sys.argv[4].strip()]

# All namespaces
totalnamespaces = subprocess.run(['kubectl', 'get', 'namespaces', '-o', 'yaml'], stdout=subprocess.PIPE)
namespaces_yaml = yaml.safe_load(totalnamespaces.stdout)


def checknamespace():
    a = 0
    for item in namespaces_yaml["items"]:
        if item["metadata"]["name"] == paramsList[2]:
            a += 1
    if a == 0:
        print("The namespace " + paramsList[2] + " does not exists")
    return a


def checkissuer():
    a = 0
    b = 0
    # check if the issuer name matches with the yaml output
    # All issuers in given namespace
    totalissuers = subprocess.run(['kubectl', '-n', paramsList[2], 'get', 'issuers', '-o', 'yaml'],
                                  stdout=subprocess.PIPE)
    issuers_yaml = yaml.safe_load(totalissuers.stdout)

    for item in issuers_yaml["items"]:
        if item["metadata"]["name"] == paramsList[3]:
            b += 1
    if b == 0:
        a = 1
    return a


def checkip():
    a = 0
    try:
        ip = ipaddress.ip_address(paramsList[0])
    except ValueError:
        # print("The IP address " + paramsList[0] + " is wrong or not set")
        a = 1
    return a


def checkdomain():
    a = 0
    try:
        domain = socket.gethostbyname(paramsList[1])
    except ValueError:
        print("The domain  " + paramsList[1] + " is wrong or not set")
        a = 1
    return a


def check_certmanager_cdr():
    os.system("kubectl get CustomResourceDefinition | awk '{ print $1 }'")


def checkhelmdeploys():
    print("Your helm's deployments actually are \n ")
    os.system("helm list | grep -i deployed | awk '{ print $1, $8, $9, $11 }'")


def checkingress_host():
    totalingress = subprocess.run(['kubectl', '-n', paramsList[2], 'get', 'ingress', '-o', 'yaml'],
                                  stdout=subprocess.PIPE)
    ingress_yaml = yaml.safe_load(totalingress.stdout)


def checkstatefulsets():
    print("You have the following statefulsets deployed :")
    os.system("kubectl -n " + paramsList[2] + " get statefulsets.apps | awk '{if(NR>1)print $1, $2}'")


if checknamespace() != 0 and checkdomain() == 0 and checkip() == 0:

    checkstatefulsets()
    # All statefull
    if checkissuer() != 0:
        print("There is no match between introduced issuer and Kubernetes issuer")
    else:
        print("\n")
        # First check all ingress that matches with given domain and given namespace
        # checkingress_host()
checkhelmdeploys()
