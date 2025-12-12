Name:		python-ip-associations-python-novaclient-ext
Version:	0.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/ip-associations-python-novaclient-ext/ip_associations_python_novaclient_ext-%{version}.tar.gz
Summary:	Adds Rackspace ip_associations support to python-novaclient
URL:		https://pypi.org/project/ip-associations-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Adds Rackspace ip_associations support to python-novaclient

%files
%{py_sitedir}/ip_associations_python_novaclient_ext.py
%{py_sitedir}/ip_associations_python_novaclient_ext-*.*-info
