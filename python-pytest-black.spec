#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin to enable format checking with black
Summary(pl.UTF-8):	Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
Name:		python-pytest-black
# keep 0.3.x here for python2 support
Version:	0.3.12
Release:	7
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-black/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-black/pytest-black-%{version}.tar.gz
# Source0-md5:	5c44840754f9edfb5c775768aa07990a
Patch0:		%{name}-pytest.patch
URL:		https://pypi.org/project/pytest-black/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest >= 3.5.0
BuildRequires:	python-toml
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pytest plugin to enable format checking with black
<https://github.com/ambv/black>.

%description -l pl.UTF-8
Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
<https://github.com/ambv/black>.

%prep
%setup -q -n pytest-black-%{version}
%patch -P 0 -p1

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_black" \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/pytest_black.py[co]
%{py_sitescriptdir}/pytest_black-%{version}-py*.egg-info
