%define module starlette-context
%define oname starlette_context

Name:		python-starlette_context
Version:	0.5.1
Release:	1
Summary:	Middleware for Starlette that allows you to store and access the context data of a request
License:	MIT
Group:		Development/Python
URL:		https://starlette-context.readthedocs.io
Source0:	https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)

%description
Middleware for Starlette that allows you to store and access the context data of a request. Can be used with logging so logs automatically use request headers such as x-request-id or x-correlation-id.

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
