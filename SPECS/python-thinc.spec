# Created by pyp2rpm-3.1.3
%global pypi_name thinc

Name:           python-%{pypi_name}
Version:        5.0.8
Release:        1%{?dist}
Summary:        Learn sparse linear models

License:        MIT
URL:            https://github.com/spacy-io/thinc
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
 thinc: Learn supersparse multiclass models thinc is a Cython library for
learning models with millions of parameters and dozens of classes. It drives ,
a pipeline of very efficient NLP components. I've only used thinc from Cython;
no real Python API is currently available.

%package -n     python2-%{pypi_name}
Summary:        Learn sparse linear models
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-numpy >= 1.7
Requires:       python-murmurhash < 0.27
Requires:       python-murmurhash >= 0.26
Requires:       python-cymem < 1.32
Requires:       python-cymem >= 1.30
Requires:       python-preshed < 0.47
Requires:       python-preshed >= 0.46
%description -n python2-%{pypi_name}
 thinc: Learn supersparse multiclass models thinc is a Cython library for
learning models with millions of parameters and dozens of classes. It drives ,
a pipeline of very efficient NLP components. I've only used thinc from Cython;
no real Python API is currently available.

%package -n     python3-%{pypi_name}
Summary:        Learn sparse linear models
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-numpy >= 1.7
Requires:       python3-murmurhash < 0.27
Requires:       python3-murmurhash >= 0.26
Requires:       python3-cymem < 1.32
Requires:       python3-cymem >= 1.30
Requires:       python3-preshed < 0.47
Requires:       python3-preshed >= 0.46
%description -n python3-%{pypi_name}
 thinc: Learn supersparse multiclass models thinc is a Cython library for
learning models with millions of parameters and dozens of classes. It drives ,
a pipeline of very efficient NLP components. I've only used thinc from Cython;
no real Python API is currently available.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 5.0.8-1
- Initial package.