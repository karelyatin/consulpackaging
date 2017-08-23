%global pypi_name treq
# doc build disabled as it requires python-incremental(under package review)
# https://bugzilla.redhat.com/show_bug.cgi?id=1484331
%global with_doc 0

Name:           python-%{pypi_name}
Version:        17.8.0
Release:        1%{?dist}
Summary:        A requests-like API built on top of twisted.web's Agent

License:        MIT/X
URL:            https://github.com/twisted/treq
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
%if 0%{?with_doc}
BuildRequires:  python2-sphinx
BuildRequires:  python2-incremental
%endif
BuildRequires:  python2-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
treq is an HTTP library inspired by requests but written on top of Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests when using Twisted.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
#Requires:       python-incremental
Requires:       python2-requests >= 2.1.0
Requires:       python2-six
Requires:       python2-twisted >= 16.3.0
Requires:       python2-attrs
%description -n python2-%{pypi_name}
treq is an HTTP library inspired by requests but written on top of Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests when using Twisted.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
#Requires:       python3-incremental
Requires:       python3-requests >= 2.1.0
Requires:       python3-six
Requires:       python3-twisted >= 16.3.0
Requires:       python3-attrs
%description -n python3-%{pypi_name}
treq is an HTTP library inspired by requests but written on top of Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests when using Twisted.

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        treq documentation
%description -n python-%{pypi_name}-doc
Documentation for treq
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
%if 0%{?with_doc}
# generate html docs 
export PYTHONPATH=src
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html 
%endif

%changelog
* Fri Aug 11 2017 ykarel <ykarel@redhat.com> - 17.8.0-1
- Initial package.
