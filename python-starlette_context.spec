Name:		python-starlette_context
Version:	0.4.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/starlette_context/starlette_context-%{version}.tar.gz
Summary:	Middleware for Starlette that allows you to store and access the context data of a request. Can be used with logging so logs automatically use request headers such as x-request-id or x-correlation-id.
URL:		https://pypi.org/project/starlette_context/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Middleware for Starlette that allows you to store and access the context data of a request. Can be used with logging so logs automatically use request headers such as x-request-id or x-correlation-id.

%files
%{py_sitedir}/starlette_context
%{py_sitedir}/starlette_context-*.*-info
