%global library python-consul
%global module consul

# sdist doesn't contains tests yet, also python-consul tests
# require pytest-twisted which is not packaged yet.
%global with_tests 0

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{module}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Python client for Consul (http://www.consul.io/)

License:        MIT
URL:            https://github.com/cablehead/python-consul
Source0:        https://files.pythonhosted.org/packages/source/p/%{library}/%{library}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
 
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%endif

%description
Python client for Consul.io

%package -n     python2-%{module}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{module}}
 
Requires:       python2-requests >= 2.0
Requires:       python2-six >= 1.4
Requires:       python2-tornado
# consul's treq client not available as python-treq is not packaged yet
#Requires:       python-treq
%description -n python2-%{module}
Python client for Consul.io

%if 0%{?with_python3}
%package -n     python3-%{module}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{module}}
 
Requires:       python3-requests >= 2.0
Requires:       python3-six >= 1.4
Requires:       python3-aiohttp
Requires:       python3-tornado
# consul's treq client not available as python3-treq is not packaged yet
#Requires:       python3-treq
%description -n python3-%{module}
Python client for Consul.io
%endif


%prep
%autosetup -n %{library}-%{version}

# Let's handle dependencies ourseleves
sed -i '/tests_require/d' setup.py

# Remove bundled egg-info
rm -rf %{library}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
# aio.py is not compatible with python2 and is not supported.
rm -rf %{buildroot}/%{python2_sitelib}/%{module}/aio.py*

%if 0%{?with_python3}
%py3_install
%endif


%if 0%{?with_tests}
%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif
%endif

%files -n python2-%{module}
%license LICENSE
%doc README.rst

%{python2_sitelib}/%{module}
%{python2_sitelib}/python_consul-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{module}
%license LICENSE
%doc README.rst

%{python3_sitelib}/%{module}
%{python3_sitelib}/python_%{module}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Aug 10 2017 Yatin Karel <ykarel@redhat.com> - 0.7.1-1
- Initial package.
